import os
from requestListener import RequestListener

def main() -> None:
    # Define the name of the application
    app_name = 'ML_inference_api'
    
    # Define the name of the assets folder
    models_folder = 'assets/models/model.joblib'
    
    # Get the absolute path of the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get the absolute path of the parent directory (one level up)
    parent_dir = os.path.dirname(current_dir)
    
    # Construct the absolute path to the assets folder
    modelPath = os.path.join(parent_dir, models_folder)
    
    # Create an instance of the RequestListener class
    request_listener = RequestListener(app_name, modelPath)
    
    # Start the request listener
    request_listener.start()


if __name__ == '__main__':
    main()