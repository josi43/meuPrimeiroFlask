from flask import Flask


app = Flask(_name_)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__=='__main__':
    app.run(debug=True)