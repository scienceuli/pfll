from flask import Flask, render_template

app = Flask(__name__)

data_file = open('../Webscraping/vfll_links.txt', 'r')
data_list = data_file.readlines()


@app.route('/')
def home():
    return render_template("index.html", data_list = data_list)

if __name__ == "__main__":
    app.run(debug=True)
