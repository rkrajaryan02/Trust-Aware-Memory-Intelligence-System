import json

CHANGE_LOG_FILE = "storage/change_log.json"


def load_logs():
    try:
        with open(CHANGE_LOG_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_logs(logs):
    with open(CHANGE_LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)
