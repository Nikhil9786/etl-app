from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route("/trigger-etl", methods=["POST"])
def trigger_etl():
    try:
        # Run ETL process using a subprocess
        subprocess.run(["./run_etl.sh"], check=True, shell=True)

        return jsonify({"message": "ETL process triggered successfully"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
