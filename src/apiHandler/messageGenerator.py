from flask import Flask, jsonify, request
from flask_cors import CORS

class MessageGenerator:
    """
    Responsible for generating the returned message.
    """
    def __init__(self, message):
        """
        Initializes a MessageGenerator object with the given message.

        Args:
            message (str): The message to be returned.

        Returns:
            None
        """
        self.message = message
    
    def generate_returned_message(self, received_message):
        """
        Generates the returned message based on the received message.

        Args:
            received_message (str): The received message.

        Returns:
            str: The generated returned message.
        """
        if received_message is not None:
            returned_message = self.message + ' ' + received_message
        else:
            returned_message = self.message
        
        return returned_message
