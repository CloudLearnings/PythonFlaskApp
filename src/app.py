from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello_json')
def hello_json():
    message = {"message": "Hello, World!"}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
