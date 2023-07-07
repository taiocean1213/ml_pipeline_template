from flask import Flask, jsonify, request
from flask_cors import CORS

from apiHandler.corsSetup import CorsSetup
from apiHandler.messageGenerator import MessageGenerator
from apiHandler.flaskApp import FlaskApp
from apiHandler.requestHandler import RequestHandler 
from apiHandler.requestMethodHandler import RequestMethodHandler

class RequestListener:
    """
    Handles the HTTP request and returns the result.
    """
    def __init__(self, app_name: str, message: str) -> None:
        """
        Initializes a RequestListener object with the given app_name and message.

        Args:
            app_name (str): The name of the Flask application instance.
            message (str): The message to be returned.

        Returns:
            None
        """
        self.flask_app = FlaskApp(app_name)
        self.cors_setup = CorsSetup(self.flask_app.app)
        self.request_handler = RequestHandler(message)
        self.request_method_handler = RequestMethodHandler()
        self.message_generator = MessageGenerator(message)

        self.cors_setup.setup_cors()
    
    def handle_request(self) -> jsonify:
        """
        Handles the HTTP request and returns the result back to the frontend.

        Returns:
            JSON response: A JSON response containing the message to be returned.
        """
        if request.method == 'GET':
            received_message = self.request_method_handler.get_received_message()
        elif request.method == 'POST':
                        received_message = self.request_method_handler.get_received_message_json()

        returned_message = self.message_generator.generate_returned_message(received_message)
        
        return jsonify(message=returned_message)