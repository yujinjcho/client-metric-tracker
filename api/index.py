from flask import request
from werkzeug.exceptions import BadRequest

from client_action_tracker.app_setup import create_app

app, service = create_app()
@app.route('/')
def home():
    return service.hello_world()

@app.route('/events', methods=['GET', 'POST'])
def event():
    data = request.get_json()

    api_key = request.headers.get('api-key')
    if not api_key:
        return {'status': 'error', 'description': 'no api key'}, 400

    events = data.get('events')
    if not events:
        raise BadRequest("Missing 'events' field")

    service.create_events(events, api_key)
    return {'status': 'success'}, 200
