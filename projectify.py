from app import flaskApp, create_app, db
from app.config import DeploymentConfig
from flask_migrate import Migrate

flaskApp = create_app(DeploymentConfig)
migrate = Migrate(db, flaskApp)