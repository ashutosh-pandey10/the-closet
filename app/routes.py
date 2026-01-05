from flask import request, jsonify, Blueprint
from .logger import logger
from models.processor import get_recommendations

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET"])
def index():
    return jsonify({"status_code": "201", "message": "Welcome to The Closet!"})

@bp.route("/search", methods=["POST"])
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