from flask import Flask

app = Flask(__name__)

@app.route("/")
def startseite():
   return "Hallo Herr Saadieh , ich bin Yazan und das ist meine erste Internetseite die ich am 12.12.2025 erstellt habe :) "

if __name__ == "__main__":
    app.run(debug=True)
