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
