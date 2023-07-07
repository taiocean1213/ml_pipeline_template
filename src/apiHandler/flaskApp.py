from flask import Flask, jsonify, request
from flask_cors import CORS

class FlaskApp:
    """
    Responsible for initializing the Flask application instance.
    """
    def __init__(self, app_name):
        """
        Initializes a FlaskApp object with the given app_name.

        Args:
            app_name (str): The name of the Flask application instance.

        Returns:
            None
        """
        self.app = Flask(app_name)

