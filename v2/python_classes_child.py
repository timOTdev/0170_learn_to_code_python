# Child class (Derived Class)
# Imports Account parent class into file
from python_classes_parent import Account

# Sets up a child class called Member
class Member(Account):
	# Child inherits all parents definitions without modification
	pass
		
	# Instance method
	def pay_dues(self, method):
		print(f"{self.email} is paid dues via {method}.")

# Make a new member
t = Member("Tim", "Hoang", "hispanichackersboard@gmail.com")

# Method to have pay dues
t.pay_dues("paypal")

# Inherited method for member to sign up for event
t.rsvp_events("meetup")

# Inherited method for member to self-introduce at event
t.introduce_self()
