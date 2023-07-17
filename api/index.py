from client_action_tracker.app_setup import create_app

app, service = create_app()
@app.route('/')
def home():
    return service.hello_world()
