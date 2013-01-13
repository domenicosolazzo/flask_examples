from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/_get_current_user')
def get_current_user():
    return jsonify( username="domenico",
        email="domenico@example.com",
        id=242
    )

if __name__ == '__main__':
    app.debug = True
    app.run()