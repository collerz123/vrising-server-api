from flask import Flask, jsonify
from flask_cors import CORS
import a2s

app = Flask(__name__)
CORS(app)

SERVERS = [
    {
        "id": "hengoria",
        "ip": "95.135.1.25",
        "game_port": 9876,
        "query_port": 9877
    },
    {
        "id": "blackvein",
        "ip": "208.115.248.90",
        "game_port": 9876,
        "query_port": 9877
    }
]


def query_server(server):
    try:
        # Query the V Rising server using the query port
        info = a2s.info(
            (server["ip"], server["query_port"])
        )

        return {
            "id": server["id"],
            "ip": f'{server["ip"]}:{server["game_port"]}',
            "online": True,
            "server": info.server_name,
            "players": info.player_count,
            "max_players": info.max_players,
            "map": info.map_name
        }

    except Exception as e:
        return {
            "id": server["id"],
            "ip": f'{server["ip"]}:{server["game_port"]}',
            "online": False,
            "players": 0,
            "max_players": 0,
            "map": "",
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
    app.run(
        host="0.0.0.0",
        port=5000
    )
