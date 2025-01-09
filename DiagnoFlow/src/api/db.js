import { MongoClient } from 'mongodb';

class PatientDB {
  constructor() {
    this.uri = "mongodb+srv://anha:qvYgxFlcTC65MWhM@anha.dm2ue.mongodb.net/patients?retryWrites=true&w=majority&appName=ANHA";
    this.client = new MongoClient(this.uri);
    this.dbName = 'patients';
    this.collectionName = 'patient_data';
  }

  async connectDB() {
    try {
      await this.client.connect();
      console.log("Connected to MongoDB");
    } catch (error) {
      console.error("Error connecting to MongoDB:", error);
      throw error;
    }
  }

  async uploadDocument(doc) {
    try {
      const db = this.client.db(this.dbName);
      const collection = db.collection(this.collectionName);
      const result = await collection.insertOne(doc);
      console.log("Document uploaded:", result);
      return result;
    } catch (error) {
      console.error("Error uploading document:", error);
      throw error;
    }
  }

  async getBatchNumber() {
    try {
      const db = this.client.db(this.dbName);
      const collection = db.collection(this.collectionName);
      const latestBatch = await collection.find({})
        .sort({ batchNumber: -1 })
        .limit(1)
        .toArray();

      console.log("Query result for latest batch:", latestBatch);

      const latestBatchNumber = latestBatch.length > 0 ? latestBatch[0].batchNumber : 0;
      console.log("Latest batch number:", latestBatchNumber);
      return latestBatchNumber;
    } catch (error) {
      console.error("Error fetching latest batch number:", error);
      throw error;
    }
  }
}



export default PatientDB;
