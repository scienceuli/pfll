from flask import Flask, render_template

app = Flask(__name__)
name = "Uli"

@app.route('/')
def home():
    return render_template("index.html", name = name)

if __name__ == "__main__":
    app.run(debug=True)
