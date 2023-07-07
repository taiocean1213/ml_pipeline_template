from requestListener import RequestListener


if __name__ == '__main__':
    app_name = 'MyApp'
    message = 'Hello,'
    request_listener = RequestListener(app_name, message)
    request_listener.start()
