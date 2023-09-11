from flask import Flask, render_template, jsonify
import pymongo
import os

app = Flask(__name__)

# Retrieve the MongoDB IP address from an environment variable
mongo_ip = os.environ.get("MONGODB_IP")

# Create a MongoDB client with the retrieved IP address
mongo_uri = f"mongodb://{mongo_ip}:27017"
mongo_client = pymongo.MongoClient(mongo_uri)

# Define a function to fetch database names
def get_database_names():
    return mongo_client.list_database_names()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello_json')
def hello_json():
    message = {"message": "Hello, World!"}
    return jsonify(message)

@app.route('/fetch_dbs')
def fetch_dbs():
    db_names = get_database_names()
    return jsonify({"databases": db_names})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
