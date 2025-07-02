
from app.core.models.user_entity import User, db


def get_all_users(page: int, per_page: int) -> list:
    """
    Fetch all users with pagination.
    :param page: Page number for pagination.
    :param per_page: Number of users per page.
    :return: List of users for the specified page.
    """
    users = User.query.paginate(page=page, per_page=per_page)

    return users.items

def add_user(username: str, email: str) -> None:
    """
    Add a new user to the database.
    :param username: Username of the new user.
    :param email: Email of the new user.
    """
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

def delete_user(user_id: int) -> None:
    """
    Delete a user from the database.
    :param user_id: ID of the user to be deleted.
    """
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        raise ValueError(f"User with ID {user_id} does not exist.")