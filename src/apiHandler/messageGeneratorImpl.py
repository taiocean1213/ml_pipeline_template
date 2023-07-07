import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from abc import ABC, abstractmethod


from apiHandler.messageGenerator import MessageGenerator

class MessageGeneratorImpl(MessageGenerator):
    """
    Implementation of MessageGenerator interface.
    """

    def __init__(self, message):
        """
        Initializes a MessageGeneratorImpl object with the given message.

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
            # If a received message is provided, 
            # concatenate it with the self.message
            returned_message = self.message + ' ' + received_message
        else:
            # If no received message is provided, 
            # use only the self.message
            returned_message = self.message

        return returned_message
