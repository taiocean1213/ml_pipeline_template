import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from abc import ABC, abstractmethod

from apiHandler.requestHandler import RequestHandler

class RequestHandlerImpl(RequestHandler):
    """
    Implementation of RequestHandler interface.
    """

    def __init__(self, message_generator):
        """
        Initializes a RequestHandlerImpl object with the given 
        message_generator.

        Args:
            message_generator (MessageGenerator): The message 
            generator object.

        Returns:
            None
        """
        # Setting up Cross-Origin Resource Sharing for 
        # the Flask application
        self.message_generator = message_generator

    def handle_request(self) -> None:
        """
        Handles the HTTP request and returns the result 
        back to the frontend.

        Returns:
        JSON response: A JSON response containing the 
        message to be returned.
        """
        try:
            # Get the received message from the frontend
            received_message = self.get_received_message()
            
            # Log the received message
            logging.info(f"Received message: {received_message}")

            # Generate a returned message based on the received message
            returned_message = \
                self.message_generator\
                .generate_returned_message(received_message)

            # Return the returned message in JSON format
            return jsonify(message=returned_message) 
        
        except Exception as e:
            # Log any errors that occurred while handling the request
            logging.error(f"Error handling request: {str(e)}")
            
            # Return an error message in JSON format if there 
            # was an error handling the request
            return jsonify(
                error="An error occurred while handling the request."
                )
    
    def get_received_message(self) -> dict:
        """
        Retrieves the received message from the request query 
        parameters or JSON body.

        Returns:
            dict: The received message as a dictionary.
        """
        # Check the HTTP method of the request
        if request.method == 'GET':
            # If the method is GET, retrieve the 'username' 
            # parameter from the request query parameters
            return request.args.to_dict()
        
        elif request.method == 'POST':
            # If the method is POST, retrieve the 'username' 
            # value from the JSON body of the request
            return request.json
