# signup.py
import logging
from login import hash_password
from database import add_owner

def signup(username, password, restaurant_name):
    """
    Create a new user account and store it in the database.

    Parameters:
    - username (str): The username for the new user.
    - password (str): The password for the new user. (In a real-world scenario, this should be hashed.)
    - restaurant_name (str): The name of the restaurant associated with the new user.
    """
    try:
        hashed_password = hash_password(password)
        add_owner(username, hashed_password, restaurant_name)
        logging.info(f"User '{username}' signed up successfully.")
    except Exception as e:
        # Use the logging library for better control over logs
        logging.error(f"Error during signup: {e}")

# Example usage:
# signup("new_user", "new_password", "New Restaurant")
