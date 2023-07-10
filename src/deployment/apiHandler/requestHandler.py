from flask import Flask, jsonify, request
from flask_cors import CORS
from abc import ABC, abstractmethod

class RequestHandler(ABC):
    """
    Abstract class for handling the HTTP request and returning
    the result.
    """
    
    @abstractmethod
    def handle_request(self):
        """
        Handles the HTTP request and returns the result back
        to the frontend.


        Returns:
        JSON response: A JSON response containing the
        message to be returned.
        """
        pass

