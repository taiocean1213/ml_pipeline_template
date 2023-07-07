from flask import Flask, jsonify, request
from flask_cors import CORS

class RequestMethodHandler:
    """
    Responsible for handling the request method and retrieving the received message.
    """
    def get_received_message(self):
        """
        Retrieves the received message from the request query parameters.

        Returns:
            str: The received message.
        """
        return request.args.get('username')
    
    def get_received_message_json(self):
        """
        Retrieves the received message from the request JSON body.

        Returns:
            str: The received message.
        """
        return request.json.get('username')
