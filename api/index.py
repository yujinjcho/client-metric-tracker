from client_action_tracker.app_setup import initialize_app

app = initialize_app()
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
