# Function definition to welcome the user after they've signed up.
def welcome_new_member(first_name, last_name, linkedin_name, favorite_language):
	full_name = f"{first_name} {last_name}";
	print(f"Welcome to Hispanic Hackers, {full_name}!")
	print(f"We're really glad to have you.")
	print(f"We'll notify you when we have new events about {favorite_language}!")
	return full_name

# Function definition to send a notification to remind admin to grant them access.
def notification_new_member(full_name):
	print(f"NOTIFICATION: {full_name} has just joined, welcome them.")

# Function call stores results from function 1 in a variable.
new_member_email = welcome_new_member("Timothy", "Hoang", "timothyhoang", "JavaScript")

# Function call uses results from one function in another function.
notification_new_member(new_member_email)