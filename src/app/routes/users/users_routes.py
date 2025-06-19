import logging
from flask import Blueprint, render_template, request
from app.core.services.users_service import add_user, delete_user, get_all_users

users_bp = Blueprint("users_bp", __name__)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@users_bp.route("/home", methods=["GET"])
def fetch_all() -> render_template:
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("size", 10, type=int)
    logger.info("Fetching all users by page: %d and size: %d", page, per_page)
    users = get_all_users(page=page, per_page=per_page)
    return render_template("/users/list_user.html", users=users)


@users_bp.route("/users", methods=["POST"])
def add() -> tuple:
    json = request.get_json()
    username = json.get("username")
    email = json.get("email")
    logger.info("Creating new user: %s, %s", username, email)
    add_user(username=username, email=email)
    return f"User {username} created successfully", 201


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete(user_id) -> tuple:
    logger.info("Deleting user of id: %d", user_id)
    delete_user(user_id=user_id)
    return f"User {user_id} deleted successfully", 200
