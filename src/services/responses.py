import json

def get_json_status(result, status_code):
    return json.dumps(result), status_code, {'ContentType':'application/json'}


