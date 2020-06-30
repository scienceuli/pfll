# data_app.py

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def html_table():
    df = pd.read_csv("data.csv")
    return render_template("table.html", table=df.to_html(classes="table table-hover", header="true"))


if __name__ == "__main__":
    app.run(debug=True)
