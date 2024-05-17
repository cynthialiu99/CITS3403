from app import create_app, db
from app import flaskApp
from app.models import User

# Function to add test data to the database
def add_test_data_to_db():
    with flaskApp.app_context():
        test_data = [
            User(student_id= "01349324", name="Tom K", email="01349324@student.uwa.edu.au"),
            User(student_id = "01349523", name="Jerome D", email="01349523@student.uwa.edu.au"), 	
            User(staff_id = "01349622", name="Cardi B", email="01349622@uwa.edu.au"),  	
            User(staff_id = "01349721", name="Taylor K", email="01349721@uwa.edu.au")  
        ]
        db.session.bulk_save_objects(test_data)
        db.session.commit()
        print("Test data added to the database.")

# Run the function to add test data
if __name__ == "__main__":
    add_test_data_to_db()

