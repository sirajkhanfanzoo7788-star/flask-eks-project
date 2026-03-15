from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App running on Kubernetes!THIS APP DEPOYED BY SIRAJ AHMAD ,ALUMDULILLAH"

@app.route("/health")
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    #dgfhjkkjhgfdfghjkljhgfgjkjhgfgjkhjsdffgff