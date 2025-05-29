from flask import Flask
from flask_cors import CORS
from routes import routes_blueprint

app = Flask(__name__)
CORS(app)
app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(debug=True)