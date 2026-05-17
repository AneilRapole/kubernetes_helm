from flask import Flask
app = Flask(__name__)

@app.route("/order")
def order():
    return {"order": "Laptop", "price": 800}

app.run(host="0.0.0.0", port=5001)