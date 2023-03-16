from flask import Flask

app = Flask(__name__)

string_variable = "Hello World"

@app.route('/')
def get_string():
    return string_variable

if __name__ == '__main__':
    app.run(debug=True)