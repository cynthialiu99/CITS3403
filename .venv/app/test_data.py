from app import db
from app.models import *


tom = User(uwa_id= "01349324", name="Tom K", email="01349324@student.uwa.edu.au")
jerome = User(uwa_id = "01349523", name="Jerome D", email="01349523@student.uwa.edu.au")  	
cardi = User(staff_id = "01349622", name="Cardi B", email="01349622@uwa.edu.au")  	
taylor = User(staff_id = "01349721", name="Taylor K", email="01349721@uwa.edu.au")  

db.session.add_all([tom, jerome, cardi, taylor])
db.session.commit()