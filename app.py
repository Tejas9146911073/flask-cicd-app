from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, CI/CD World! This is a simple Flask App."
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
