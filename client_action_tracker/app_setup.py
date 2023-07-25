import os
from typing import Tuple

import psycopg2
from flask import Flask
from flask_cors import CORS

from client_action_tracker.client_track_service import ClientTrackService
from client_action_tracker.datastore import Datastore
from client_action_tracker.utils import get_project_id


def create_app() -> Tuple[Flask, ClientTrackService]:
    print("Creating app")

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:3001", "https://www.simpleliftingapp.com"]}})

    db_config = {
        'dbname': os.environ.get('DB_NAME', 'client-metric-track'),
        'password': os.environ.get('DB_PASSWORD', None),
        'user': os.environ.get('DB_USER', 'postgres'),
        'port': os.environ.get('DB_PORT', '5432'),
        'host': os.environ.get('DB_HOST', 'localhost')
    }
    conn = psycopg2.connect(**db_config)

    datastore = Datastore(conn)
    service = ClientTrackService(datastore, get_project_id)

    return app, service
