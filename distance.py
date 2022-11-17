import numpy as np
from datetime import datetime
from flask import abort
from connexion.exceptions import OAuthProblem

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

tokens = "123321"

def apikey_auth(token, required_scopes = None):
    if token == tokens:
        return {} 
    else:
        raise OAuthProblem(f"Invalid token")
    

def get_distances(city_start, city_finish):
    distance = {}
    dist = 0
    distances = np.load(open("/Users/Xe/level_up/LevelUp_py1/project-API/matrix_distance", "rb"))
    if city_start in range(len(distances)) and city_finish in range(len(distances)):
        distance[dist] = {
            "dist": f"{distances[city_start, city_finish]}",
            "timestamp": get_timestamp()
        }
        if distances[city_start, city_finish] != 0:
            return distance[dist]
        else:
            abort(
                404,
                f'Distance between city "{city_start}" and city "{city_finish}" not found',
            )
    else:
        abort(
            422,
            f"Cities not found",
        )
