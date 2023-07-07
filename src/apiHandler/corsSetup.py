from flask import Flask, jsonify, request
from flask_cors import CORS

class CorsSetup:
    """
    Responsible for setting up Cross-Origin Resource Sharing (CORS).
    """
    def __init__(self, app):
        """
        Initializes a CorsSetup object with the given Flask application instance.

        Args:
            app (Flask): The Flask application instance.

        Returns:
            None
        """
        self.app = app
    
    def setup_cors(self):
        """
        Sets up Cross-Origin Resource Sharing (CORS) for the Flask application.

        Returns:
            None
        """
        CORS(self.app)
