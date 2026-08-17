from flask import Flask, jsonify
import a2s

app = Flask(__name__)

IP = "95.135.1.25"
PORT = 9877


@app.route("/server")
def get_server():
    try:
        info = a2s.info((IP, PORT))

        return jsonify({
            "online": True,
            "server": info.server_name,
            "players": info.player_count,
            "max_players": info.max_players,
            "map": info.map_name
        })

    except Exception as e:
        return jsonify({
            "online": False,
            "error": str(e)
        })


@app.route("/")
def home():
    return "V Rising Server API is running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
