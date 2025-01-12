<script>
  let ascensionNumber = "";
  let selectedTest = "";
  let patientData = [];
  let currentAscension = "";

  const testTypes = ["ABR", "Mini RPP", "STI", "UTI", "RPP"];
  async function uploadPatients() {
    if (patientData.length === 0) {
        alert('No patients to upload.');
        return;
    }
    console.log("Batch number:", batchNumber);

    console.log(PatientDB.getBatchNumber+1)
    console.log(patientData)
    const prep = {
      batchNumber: batchNumber+ 1,
      patients: patientData,
      created_at: Date.now
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
      { ascensionNumber: currentAscension, testType: selectedTest },
    ];
    currentAscension = "";
    selectedTest = "";
  };

  const deletePatient = (ascensionNumber) => {
    patientData = patientData.filter((patient) => patient.ascensionNumber !== ascensionNumber);
  };

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
              <strong>{i + 1}. Ascension:</strong> {patient.ascensionNumber}<br />
              <strong>Test Type:</strong> {patient.testType}
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