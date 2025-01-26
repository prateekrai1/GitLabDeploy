from flask import Flask
from db import connect_to_mongodb
from insertMetadata import insert_metadata, fetch_metadata

app = Flask(__name__)
db_client = connect_to_mongodb()
@app.route('/insert-metadata')
def insert():
    return insert_metadata()

@app.route('/fetch-metadata')
def fetch():
    return fetch_metadata()

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()