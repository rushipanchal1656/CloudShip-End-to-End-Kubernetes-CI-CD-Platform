# This is the main application file for the CloudShip project. It defines a simple Flask web application with three routes: the home route ("/"), a health check route ("/health"), and a readiness check route ("/ready"). The health check route returns a JSON response indicating the application's health status and environment, while the readiness check route returns a JSON response indicating that the application is ready to serve requests. The application runs on host "

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Yes we did it 🫠 CloudShip 🚢 is smoothly running on Kubernetes!"

@app.route("/health")
def health():
    """Health check endpoint for Kubernetes readiness and liveness probes"""
    return jsonify({
        "status": "healthy",
        "environment": os.getenv("APP_ENV", "development")
    }), 200

@app.route("/ready")
def ready():
    """Readiness check endpoint"""
    return jsonify({"ready": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
