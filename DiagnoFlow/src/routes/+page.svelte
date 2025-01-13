<script>
  let ascensionNumber = "";
  let loading = false
  let selectedTest = "";
  let patientData = [];
  let currentAscension = "";
  const testTypes = ["ABR", "Mini RPP", "STI", "UTI", "RPP"];
  async function uploadPatients() {
    if (patientData.length === 0) {
        alert('No patients to upload.');
        return;
    }
    var batchNumber = await getBatchNumber()
    console.log("Batch number:", batchNumber);

    const prep = {
      batch_number: batchNumber + 1,
      patients: patientData,
      date: new Date().toISOString().split('T')[0],
    }
    var result = createBatch(prep)
    console.log(prep)
    console.log(result)
  };

  async function createBatch(batch) {
    loading = true
    var error = null; // Reset error before fetching
    var responseData = null; // Reset response data

    const apiUrl = 'https://jbib83ig7l.execute-api.us-east-2.amazonaws.com/dev/batches';

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(batch), // Send the batch object as JSON
      });

      if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
      }

      responseData = await response.json(); // Parse the JSON response
    } catch (err) {
      error = err.message; // Catch and store any errors
    } finally {
      loading = false; // Stop the loading state
    }
  }

  const addPatient = () => {
    if (ascensionNumber.trim() === "") {
      alert("Please enter an ascension number.");
      return;
    }

    if (patientData.find((patient) => patient.ascensionNumber === ascensionNumber)) {
      alert("Duplicate ascension number detected. Please enter a unique number.");
      return;
    }

    currentAscension = ascensionNumber;
    ascensionNumber = "";
  };

  const saveTestType = () => {
    if (!selectedTest) {
      alert("Please select a test type.");
      return;
    }

    patientData = [
      ...patientData,
      { asc_number: currentAscension, test_type: selectedTest },
    ];
    currentAscension = "";
    selectedTest = "";
  };

  const deletePatient = (ascensionNumber) => {
    patientData = patientData.filter((patient) => patient.ascensionNumber !== ascensionNumber);
  };
  async function getBatchNumber() {
    var loading = true; // Set loading to true while fetching
    var error = null; // Reset error before fetching
    var responseData = null; // Reset response data

    const apiUrl = 'https://jbib83ig7l.execute-api.us-east-2.amazonaws.com/dev/batches/latest';

    try {
      const response = await fetch(apiUrl, {
        method: 'GET', // Use 'POST' for a POST request
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
      }

      responseData = await response.json(); // Parse the JSON response
      console.log(responseData)
      return(responseData)
    } catch (err) {
      error = err.message; // Catch and store any errors
    } finally {
      loading = false; // Stop the loading state
    }
  }
</script>

<main>
  
  <!-- Left Pane: Data Entry -->
  <div class="left-pane">
    <h1>Data Entry</h1>

    <!-- Ascension Number Input -->
    {#if !currentAscension}
      <div>
        <label for="ascension">Ascension Number:</label>
        <input
          id="ascension"
          type="text"
          bind:value={ascensionNumber}
          placeholder="Enter ascension number"
        />
        <button on:click={addPatient} class="submit-button">Submit</button>
      </div>
    {/if}

    <!-- Test Type Selection -->
    {#if currentAscension}
      <div>
        <p>
          <strong>Ascension Number:</strong> {currentAscension}
        </p>
        <label for="test-type">Select Test Type:</label>
        <select id="test-type" bind:value={selectedTest}>
          <option value="" disabled selected>Choose a test type</option>
          {#each testTypes as test}
            <option value={test}>{test}</option>
          {/each}
        </select>
        <button class="submit-button" on:click={saveTestType}>Save</button>
      </div>
    {/if}
  </div>

  <!-- Right Pane: Display Data -->
  <div class="right-pane">
    <h2>Patient List</h2>
    {#if patientData.length > 0}
      <div class="patients-list">
        {#each patientData as patient, i}
          <div class="patient-item">
            <div class="patient-info">
              <strong>{i + 1}. Ascension:</strong> {patient.asc_number}<br />
              <strong>Test Type:</strong> {patient.test_type}
            </div>
            <button
              class="delete-button"
              on:click={() => deletePatient(patient.ascensionNumber)}
            >
              X
            </button>
          </div>
        {/each}
        <button class="submit-button" on:click={uploadPatients}>Upload Patients</button>

      </div>
    {:else}
      <p class="no-data">No patients added yet.</p>
    {/if}
  </div>
  <script>
      
  </script>
</main>


<style>
  body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  main {
    display: flex;
    height: 100vh;
  }

  .left-pane, .right-pane {
    padding: 20px;
  }

  .left-pane {
    width: 50%;
    background: #f7f7f7;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .right-pane {
    width: 50%;
    background: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  h1, h2 {
    margin-bottom: 20px;
    color: #333;
  }

  input, select{
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    font-size: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
  }

  button {
    background: #4CAF50;
    color: #fff;
    border: none;
    cursor: pointer;
    transition: background 0.3s ease;
  }

  button:hover {
    background: #45a049;
  }

  .patients-list {
    width: 80%;
    max-height: 70%;
    overflow-y: auto;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
  }

  .patient-item {
    background: #f9f9f9;
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .patient-info {
    flex-grow: 1;
  }

  .delete-button {
    background: #ff4d4d;
    color: white;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    padding: 5px 8px;
    font-size: 0.8rem;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: 100px;
  }

  .delete-button:hover {
    background: #ff0000;
  }

  .no-data {
    color: #888;
    font-style: italic;
  }
  .submit-button {
  width: 100%;
  background-color: green;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: darkgreen;
}
</style>