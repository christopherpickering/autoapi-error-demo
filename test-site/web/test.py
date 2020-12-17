from flask import Blueprint

test_bp = Blueprint("test_bp", __name__)

@test_bp.route("/")
def home():
    return "hi"