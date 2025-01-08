import mongoose from 'mongoose';

// MongoDB connection string with database name `patients`
const uri = "mongodb+srv://anha:qvYgxFlcTC65MWhM@anha.dm2ue.mongodb.net/patients?retryWrites=true&w=majority&appName=ANHA";

// Define the schema
const patientDataSchema = new mongoose.Schema({
  asc_number: { type: Number, required: true },
  test_type: { type: String, required: true },
  date: { type: Date, default: Date.now }
});

// Create a model and explicitly set the collection name to `patient_data`
const PatientData = mongoose.model('PatientData', patientDataSchema, 'patient_data');
module.exports = PatientData;


mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Connected to MongoDB"))
  .catch(err => console.error("Error connecting to MongoDB:", err));


  // Function to upload a single document
async function uploadDocument(doc) {
    try {
      const testDoc = new Test(doc);
      const result = await testDoc.save();
      console.log("Document uploaded:", result);
    } catch (error) {
      console.error("Error uploading document:", error);
    }
  }
  
// async function main() {
//   try {
//     // Connect to the MongoDB cluster
//     await mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });
//     console.log("Connected to MongoDB");

//     // Example: Create a new document
//     const patientDoc = new PatientData({
//       asc_number: 1234,
//       test_type: 'example',
//       date: new Date()
//     });

//     // Save the document to the database
//     await patientDoc.save();
//     console.log("Document saved:", patientDoc);
//   } catch (error) {
//     console.error("Error connecting to MongoDB or saving document:", error);
//   } finally {
//     // Close the connection to the MongoDB cluster
//     await mongoose.connection.close();
//     console.log("Connection closed");
//   }
// }

// main().catch(console.error);
