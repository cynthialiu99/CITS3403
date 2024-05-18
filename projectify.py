from app import create_app, db
from app.config import DeploymentConfig
from flask_migrate import Migrate

flaskApp = create_app(DeploymentConfig)
migrate = Migrate(flaskApp,db)

if __name__ == "__main__":
    flaskApp.run()
