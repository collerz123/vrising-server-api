from flask import Flask, jsonify
from flask_cors import CORS
import a2s

app = Flask(__name__)
CORS(app)

SERVERS = [
    {
        "id": "hengoria",
        "ip": "95.135.1.25",
        "port": 9877
    },

    {
        "id": "blackvein",
        "ip": "208.115.248.90",
        "port": 9877
    }
]


def query_server(server):
    try:
        info = a2s.info((server["ip"], server["port"]))

        return {
            "id": server["id"],
            "online": True,
            "server": info.server_name,
            "players": info.player_count,
            "max_players": info.max_players,
            "map": info.map_name
        }

    except Exception as e:
        return {
            "id": server["id"],
            "online": False,
            "players": 0,
            "max_players": 0,
            "error": str(e)
        }


@app.route("/")
def home():
    return "V Rising Server API is running!"


@app.route("/servers")
def get_servers():
    results = []

    for server in SERVERS:
        results.append(query_server(server))

    return jsonify(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
