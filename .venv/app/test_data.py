from app import db
from app.models import *

group1 = Group()

tom = Student(uwa_id= "01349324", name="Tom K")
jerome = Student(uwa_id = "01349523", name="Jerome D")  	
cardi = Staff(staff_id = "01349622", name="Cardi B")  	
taylor = Staff(staff_id = "01349721", name="Taylor K")  

db.session.add_all([group1, tom, jerome, cardi, taylor])
db.session.commit()