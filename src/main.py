from flask import Flask
from requestListener import RequestListener

def main():
    # Create an instance of the RequestListener class
    requestListener = RequestListener("MyApp", "Hello")

    # Create the Flask application instance
    app = requestListener.flask_app.app

    # Define the route for handling the HTTP request
    @app.route('/', methods=['GET', 'POST'])
    def handle_request():
        return requestListener.handle_request()

    # Start the Flask application
    app.run()

if __name__ == '__main__':
    main()
