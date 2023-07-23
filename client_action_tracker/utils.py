import os

# For proto-type using env vars.
def get_project_id(api_key: str) -> str | None:
    keys_to_project_id_raw = os.environ.get('KEYS_TO_PROJECT_ID', None)
    if not keys_to_project_id_raw:
        return None

    keys_to_projects = dict(entry.split(":") for entry in keys_to_project_id_raw.split(","))
    return keys_to_projects.get(api_key, None)
