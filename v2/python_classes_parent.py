# Parent Class (Base Class)
class Account:	
	# Initializer
	def __init__(self, first_name, last_name, email):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
	
	# Instance method
	def introduce_self(self):
		print(f"Hi, my name is {self.first_name}.")
		
	# Another instance method
	def rsvp_events(self, medium):
		print(f"{self.first_name} {self.last_name} sent an RSVP via {medium}.")		
	