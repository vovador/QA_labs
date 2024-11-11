import json
import os

def load_config(env):
    config_file = f"config/environments/{env}.json"
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file for {env} does not exist")
    with open(config_file, 'r') as file:
        return json.load(file)
