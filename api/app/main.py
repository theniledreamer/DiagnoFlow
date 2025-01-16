from fastapi import FastAPI, HTTPException, Query, Body
from . import createTest
from pydantic import BaseModel, Field
from typing import List
from fastapi.responses import StreamingResponse
import pandas as pd
import io
from datetime import date
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from datetime import date, datetime
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()

# MongoDB configuration
MONGO_URI = "mongodb+srv://ashahindev:0isIpHZ7PZtoSrFG@patientdata.4cocs.mongodb.net/?retryWrites=true&w=majority&appName=PatientData"
DATABASE_NAME = "ANHA"
COLLECTION_NAME = "PatientSampleData"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]



# Helper function to convert ObjectId to string
def object_id_to_str(doc):
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc



class PatientModel(BaseModel):
    asc_number: int
    test_type: str


class BatchModel(BaseModel):
    batch_number: int
    patients: List[PatientModel]
    date: date

    # Convert `date` to `datetime` during serialization
    def to_mongo_dict(self):
        data = self.dict()
        data["date"] = datetime.combine(self.date, datetime.min.time())  # Convert date to datetime
        return data



class BatchDBModel(BatchModel):
    id: str = Field(..., alias="_id")


# CRUD Endpoints

@app.post("/batches", response_model=BatchDBModel)
async def create_batch(batch: BatchModel):
    # Convert to a dictionary compatible with MongoDB
    batch_dict = batch.to_mongo_dict()
    result = await collection.insert_one(batch_dict)
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to create batch")
    created_batch = await collection.find_one({"_id": result.inserted_id})
    return object_id_to_str(created_batch)

@app.get("/batches/latest", response_model=int)
async def get_latest_batch_number():
    try:
        # Find the document with the highest batch_number
        latest_batch = await collection.find_one(
            sort=[("batch_number", -1)]  # Sort by batch_number in descending order
        )
        if not latest_batch:
            raise HTTPException(status_code=404, detail="No batches found")
        return latest_batch["batch_number"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving latest batch number: {e}")


# Read all batches
@app.get("/batches", response_model=List[BatchDBModel])
async def read_batches():
    batches = await collection.find().to_list(1000)
    return [object_id_to_str(batch) for batch in batches]


# Read a batch by ID
@app.get("/batches/{batch_id}", response_model=BatchDBModel)
async def read_batch(batch_id: str):
    try:
        batch = await collection.find_one({"_id": ObjectId(batch_id)})
        if not batch:
            raise HTTPException(status_code=404, detail="Batch not found")
        return object_id_to_str(batch)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid ID: {e}")


# Update a batch
@app.put("/batches/{batch_id}", response_model=BatchDBModel)
async def update_batch(batch_id: str, updated_batch: BatchModel):
    try:
        result = await collection.update_one({"_id": ObjectId(batch_id)}, {"$set": updated_batch.dict()})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Batch not found")
        batch = await collection.find_one({"_id": ObjectId(batch_id)})
        return object_id_to_str(batch)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid ID: {e}")


# Delete a batch
@app.delete("/batches/{batch_id}", response_model=dict)
async def delete_batch(batch_id: str):
    try:
        result = await collection.delete_one({"_id": ObjectId(batch_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Batch not found")
        return {"message": "Batch deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid ID: {e}")
    
import json
@app.post("/test-form/{test_type}")
async def get_test_form(
    test_type: str,
    patientData: List[dict] = Body(..., description="List of patients with test information")
):
    try:
        # Pass the JSON directly to the create_test function
        df = createTest.create_test(patientData=patientData, testType=test_type)

        # Convert the DataFrame to a CSV format in-memory
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)  # Move the buffer pointer to the beginning
        today_date = datetime.now().strftime("%Y-%m-%d")
        filename = f"{test_type}_{today_date}.csv"
        # Return the CSV file as a response
        return StreamingResponse(
            csv_buffer,
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating test form: {e}")