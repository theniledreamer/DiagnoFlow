<script>
    import { onMount } from 'svelte';
  
    let batches = [];
    let error = null;
    let loading = true;
  
    async function fetchBatches() {
      const apiUrl = 'https://jbib83ig7l.execute-api.us-east-2.amazonaws.com/dev/batches';
  
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
        }
        const data = await response.json();
        // Sort batches by batch_number descending
        batches = data.sort((a, b) => b.batch_number - a.batch_number);
      } catch (err) {
        error = err.message;
      } finally {
        loading = false;
      }
    }
  
    function groupByTestType(patients) {
      return patients.reduce((acc, patient) => {
        if (!acc[patient.test_type]) {
          acc[patient.test_type] = [];
        }
        acc[patient.test_type].push(patient);
        return acc;
      }, {});
    }
  
    import ExcelJS from 'exceljs';

  async function create96WellPlate(data, section, outputFilename = '96_well_plate.xlsx') {
    // Helper function to get the start column for the selected section
    function getStartColumn(section) {
        switch (section) {
            case 1:
                return 2; // Start at A1 (column 2, since column 1 is headers)
            case 2:
                return 5; // Start at E1
            case 3:
                return 10; // Start at J1
            default:
                throw new Error('Invalid section. Must be 1, 2, or 3.');
        }
    }

    // Validate the section input
    if (![1, 2, 3].includes(section)) {
        throw new Error('Invalid section. Please choose 1, 2, or 3.');
    }

    // Sort patients by test type
    data.patients.sort((a, b) => a.test_type.localeCompare(b.test_type));

    // Create a new workbook and worksheet
    const workbook = new ExcelJS.Workbook();
    const worksheet = workbook.addWorksheet('96-Well Plate');

    // Define rows (A-H) and columns (1-12)
    const rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    const cols = Array.from({ length: 12 }, (_, i) => i + 1);

    // Add column headers
    cols.forEach((col, index) => {
        worksheet.getCell(1, index + 2).value = col; // Column headers start at B1
    });

    // Add row headers
    rows.forEach((row, index) => {
        worksheet.getCell(index + 2, 1).value = row; // Row headers start at A2
    });

    const startColumn = getStartColumn(section);
    let patientIdx = 0;

    // Populate the cells with patient data
    for (let colIdx = startColumn; colIdx < startColumn + 3; colIdx++) { // 3 columns per section
        for (let rowIdx = 2; rowIdx <= 9; rowIdx++) { // Rows A-H (row 2 to row 9)
            if (patientIdx < data.patients.length) {
                const patient = data.patients[patientIdx];
                const ascNumber = patient.asc_number;
                const testType = patient.test_type;

                // Format cell value
                const cellValue = `ASC: ${ascNumber}\nType: ${testType}`;
                const cell = worksheet.getCell(rowIdx, colIdx);
                cell.value = cellValue;
                cell.alignment = { wrapText: true, horizontal: 'center' };

                patientIdx++;
            }
        }
    }

    // Save the workbook to a file
    const buffer = await workbook.xlsx.writeBuffer();
    const blob = new Blob([buffer], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = outputFilename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    console.log(`96-well plate saved as ${outputFilename}`);
}

function generateExtraction(batch) {
    const section = parseInt(prompt(`Generating extraction for batch ${batch.batch_number}.
Which section would you like to start with? (1, 2, or 3):`), 10);
    if (![1, 2, 3].includes(section)) {
        alert('Invalid section. Please choose 1, 2, or 3.');
        return;
    }
    console.log('Batch ID: ', batch._id);
    console.log(batch);

    // Call the create96WellPlate function
    create96WellPlate(batch, section).catch(console.error);
}
    onMount(() => {
      fetchBatches();
    });
  </script>
  
  <style>
    .highlight {
      background-color: yellow;
    }
    .batch-unit, .test-type-unit {
      border: 1px solid #ccc;
      margin: 10px;
      padding: 10px;
      border-radius: 5px;
    }
    button {
      margin-right: 5px;
    }
  </style>
  
  <main>
    <h1>Batches</h1>
  
    {#if loading}
      <p>Loading...</p>
    {:else if error}
      <p style="color: red;">Error: {error}</p>
    {:else}
      {#each batches as batch (batch._id)}
        <div class="batch-unit {batch.batch_number === batches[0].batch_number ? 'highlight' : ''}">
          <h2>Batch Number: {batch.batch_number}</h2>
          <p>Date: {batch.date}</p>
          <details>
            <summary>Patients by Test Type</summary>
            {#each Object.entries(groupByTestType(batch.patients)) as [testType, patients]}
              <div class="test-type-unit">
                <details>
                  <summary>{testType}</summary>
                  <ul>
                    {#each patients as patient}
                      <li>Ascension Number: {patient.asc_number}</li>
                      console.log(batch._id)
                    {/each}
                  </ul>
                </details>
              </div>
            {/each}
          </details>
          <button on:click={() => generateExtraction(batch)}>Generate Extraction</button>
          <button on:click={() => generateTestFiles(batch)}>Generate Test Files</button>
        </div>
      {/each}
    {/if}
  </main>
  