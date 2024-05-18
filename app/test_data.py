from app import create_app, db
from app.models import User
from app.config import TestConfig  # Import TestConfig

def add_test_data_to_db():
    app = create_app(config_class=TestConfig)  # Use the 'TestConfig' configuration
    with app.app_context():
        test_data = [
            User(id="01349324", name="Tom K", email="01349324@student.uwa.edu.au"),
            User(id="01349523", name="Jerome D", email="01349523@student.uwa.edu.au"),
            User(id="01349622", name="Cardi B", email="01349622@uwa.edu.au"),
            User(id="01349721", name="Taylor K", email="01349721@uwa.edu.au")
        ]
        db.session.bulk_save_objects(test_data)
        db.session.commit()
        print("Test data added to the database.")

if __name__ == "__main__":
    add_test_data_to_db()
