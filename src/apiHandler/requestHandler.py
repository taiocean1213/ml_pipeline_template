from flask import Flask, jsonify, request
from flask_cors import CORS

class RequestHandler:
    """
    Responsible for handling the HTTP request and returning the result.
    """
    def __init__(self, message):
        """
        Initializes a RequestHandler object with the given message.

        Args:
            message (str): The message to be returned.

        Returns:
            None
        """
        self.message = message
    
    def handle_request(self):
        """
        Handles the HTTP request and returns the result back to the frontend.

        Returns:
            JSON response: A JSON response containing the message to be returned.
        """
        if request.method == 'GET':
            received_message = request.args.get('username')
        elif request.method == 'POST':
            received_message = request.json.get('username')

        print(received_message)

        if received_message is not None:
            returned_message = self.message + ' ' + received_message
        else:
            returned_message = self.message

        return jsonify(message=returned_message)
