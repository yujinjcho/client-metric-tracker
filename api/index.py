from flask import request
from werkzeug.exceptions import BadRequest

from client_action_tracker.app_setup import create_app

app, service = create_app()
@app.route('/')
def home():
    return service.hello_world()

@app.route('/test', methods=['POST'])
def test():
    service.create_test()
    return {'status': 'success'}, 200

@app.route('/events', methods=['GET', 'POST'])
def event():
    data = request.get_json()

    # TODO: move this to service
    events = []
    for event in data['events']:
        if not service.validate_event(event):
            return BadRequest(f'Invalid request body: {event}')
        # TODO: map project_id from api key
        event['project_id'] = '123e4567-e89b-12d3-a456-426614174000'
        events.append(event)

    service.create_events(events)
    return {'status': 'success'}, 200
