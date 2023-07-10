from flask import Flask, jsonify, request
from flask_cors import CORS

from apiHandler.corsSetup import CorsSetup
from apiHandler.messageGeneratorImpl import MessageGeneratorImpl
from apiHandler.flaskApp import FlaskApp
from apiHandler.requestHandlerImpl import RequestHandlerImpl

class RequestListener:
    """
    Handles the HTTP request and returns the result.
    """


    def __init__(self, app_name: str, message: str) -> None:
        """
        Initializes a RequestListener object with the
        given app_name and message.


        Args:
        app_name (str): The name of the Flask application instance.
        message (str): The message to be returned.


        Returns:
        None
        """
        self.app_name = app_name
        # Create an instance of MessageGeneratorImpl with the given message
        self.message_generator = MessageGeneratorImpl(message)
        # Create an instance of RequestHandlerImpl with the message generator
        self.request_handler = RequestHandlerImpl(self.message_generator)


    def start(self, host: str = "0.0.0.0", port: int = 5000):
        """
        Starts the Flask application and listens for incoming HTTP requests.

        Args:
        - host (str): The host IP address to bind the application to. Default is "0.0.0.0".
        - port (int): The port number to listen on. Default is 5000.

        Returns:
        None
        """
        # Create an instance of the Flask application
        app = FlaskApp(self.app_name).app
        # Setup CORS (Cross-Origin Resource Sharing)
        cors_setup = CorsSetup(app)
        cors_setup.setup_cors()

        @app.route('/', methods=['GET', 'POST'])
        def handle_request():
            # Call the handle_request method of the request_handler
            return self.request_handler.handle_request()

        # Run the Flask application
        app.run(host=host, port=port)

        return
