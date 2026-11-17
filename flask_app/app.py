import os
import sys

# Add project root directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from flask import Flask, render_template, request
from src.predict import predict_price

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        brand = request.form["brand"]
        cpu = request.form["cpu"]
        ram = int(request.form["ram"])
        storage = int(request.form["storage"])
        screen = float(request.form["screen"])
        performance = float(request.form["performance"])

        price = predict_price(
            brand,
            cpu,
            ram,
            storage,
            screen,
            performance
        )

        return render_template(
            "index.html",
            prediction=f"Predicted Laptop Price: ${price}"
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )