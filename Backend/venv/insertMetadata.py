from flask import Flask
from db import connect_to_mongodb

db_client = connect_to_mongodb()
def insert_metadata():
    if db_client:
        db = db_client['metadata']
        collection = db['metadata']
        document = {
            "name" : "metadata",
            "version":"1.0.0",
            "status": "active"
        }
        result = collection.insert_one(document)
        return f"inserted metadata with id {result.inserted_id}"
    else:
        return "Could not connect to MongoDB"

def fetch_metadata():
    if db_client:
        db = db_client['metadata']
        collection = db['metadata']
        result = collection.find_one({"name": "metadata"})
        if result:
            return f"Metadata: {result}"
        else:
            return "No metadata found"
    else:
        return "Could not connect to MongoDB"