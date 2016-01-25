import json

def build_json_response(result, status_code):
    return json.dumps(result), status_code, {'ContentType':'application/json'}
