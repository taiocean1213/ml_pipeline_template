import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from abc import ABC, abstractmethod


class MessageGenerator(ABC):
    """
    Abstract class for generating the returned message.
    """

    @abstractmethod
    def generate_returned_message(self, received_message):
        """
        Generates the returned message based on the received message.

        Args:
            received_message (str): The received message.

        Returns:
            str: The generated returned message.
        """
        pass
