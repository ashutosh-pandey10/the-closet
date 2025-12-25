from flask import Flask, request, jsonify
from logger import logger
from processor import get_recommendations


app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    # Here I am assuming I will get a json with all
    # the paramters/features value, which can be used to
    # run model to generate actual recommendations
    if request.is_json:
        try:
            data = request.get_json()
            recommendations = get_recommendations(data)
            return_data = {
                "status_code": "200",
                "message": "Recommendation generated",
                "items": recommendations["records"]
            }
            return jsonify(return_data)
        except Exception as exc:
            logger.info(f"Recommendation engine failed. Error : {exc}")
            return jsonify({"status_code":"500", "message":exc})

    return jsonify({"status_code": "422", "message":"Data passed is not JSON"})