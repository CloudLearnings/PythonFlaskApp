from flask import Flask, render_template, jsonify
import pymongo

app = Flask(__name__)

# Create a MongoDB client
mongo_client = pymongo.MongoClient("mongodb://172.17.0.2:27017")  # Replace <mongo_ip> with  actual IP address

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
    app.run(debug=True)
