from flask import Flask

app = Flask(__name__)

@app.route("/")
def startseite():
   return "Hallo Milano , ich bin Yazan und das ist meine erste Internetseite habibiii"

if __name__ == "__main__":
    app.run(debug=True)
