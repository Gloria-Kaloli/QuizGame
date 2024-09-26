from flask import Flask
from extensions import db
from routes import init_routes
import config
from flask_migrate import Migrate

app = Flask(__name__)

# Ensure the config object exists and contains the necessary configuration
app.config.from_object(config.Config)

# Initialize the database
db.init_app(app)

migrate = Migrate(app, db) 

# Initialize routes
init_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # This line is essential to create tables
    app.run(debug=True)

