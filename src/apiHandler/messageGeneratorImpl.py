# Importing necessary libraries
from sklearn.preprocessing import StandardScaler
from joblib import load
import numpy as np

# Importing the MessageGenerator interface from the messageGenerator module
from apiHandler.messageGenerator import MessageGenerator

# Creating a class that implements the MessageGenerator interface
class MessageGeneratorImpl(MessageGenerator):
    """
    Implementation of MessageGenerator interface.
    """
    def __init__(self, model_path:str) -> None:
        """
        Initializes a MessageGeneratorImpl object with the 
        given message and model path.

        Args:
            model_path (str): The path to the trained SVM model.

        Returns:
            None
        """
        self.message = 'Prediction indicates the number would be:'
        self.model = load(model_path)
        self.scaler = StandardScaler()
        return

    def generate_returned_message(self, received_message):
        """
        Generates the returned message based on the received message.

        Args:
            received_message (dict): The received json object as a dict.

        Returns:
            str: The generated returned message.
        """
        # Extracting necessary information from the received message
        username = received_message['username']
        bitmap_string = received_message['bitmap_string']
        
        # Converting the bitmap string to a list of integers
        bitmap_list = bitmap_string.split(',')
        bitmap_numbers = np.array([int(bit) for bit in bitmap_list]).reshape(-1)
        
        # Fit the scaler with data and transform the bitmap numbers
        bitmap_numbers = self.scaler.fit_transform([bitmap_numbers])
        
        # Predicting the inferred numbers using the trained model
        inferred_numbers = self.model.predict(bitmap_numbers)
        
        # Converting the inferred numbers to a string
        inferred_numbers_string = ''.join(str(num) for num in inferred_numbers)

        # Generating the returned message based on 
        # the username and inferred numbers
        if username is not None:
            returned_message = '@' + username + ' ' + self.message + ' ' + inferred_numbers_string
        else:
            returned_message = self.message + ' ' + inferred_numbers_string
        
        return returned_message
