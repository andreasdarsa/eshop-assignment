from flask import Flask
from flask_cors import CORS
from routes import routes_blueprint

app = Flask(__name__)
CORS(app)
# CORS helps "communication" between frontend and backend

app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(debug=True)