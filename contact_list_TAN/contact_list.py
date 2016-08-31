contact_list = []

class Contacts(object):
	def __init__(self, first_name, last_name, mobile = "", work_number = "", email = ""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile = mobile
		self.work_number = work_number
		self.email = email
	def send_text(self, message):
		print "To: %s - %s" % (self.mobile, message)
		


# contacts = {("Diana", "Banana") : {"mobile" : "415-555-3625", "email" : "diana@hackbright.com", "birthday" : 
# "february 21"}, ("Minnie", "Mouse") : {"mobile" : "415-666-6666", "email" : "mrsmickey@hackbright.com", "birthday" : 
# "february 14"}}

# def add_contact():
# 	pass

# def delete_contact():
# 	pass

# def change_name():
# 	pass

# def update_contact():
# 	pass




def main():

	contact_amy = Contacts("Amy", "Claussen", mobile = "345-567-7890", work_number = "555-666-8888", email = "amy@test.com")
	contact_list.append(contact_amy)

	contact_trushna = Contacts("trushna", "mehta", mobile = "123-562-1247", work_number = "332-125-8456", email = "trushna@test.com")
	contact_list.append(contact_trushna)

	contact_minnie = Contacts("Minnie", "Mouse", mobile = "415-666-6666", email = "mrsmickey@hackbright.com", work_number = "876-444-3333") 
	contact_list.append(contact_minnie)

	for info in contact_list:
		print info.first_name
		print info.last_name
		print info.mobile
		print info.work_number
		print info.email
		print ""

	for contact in contact_list:
		contact.send_text("Hella cool")



	

# "february 14"}



	# message_to_send = raw_input("What message do you want to send?")
	# amy.send_text(message_to_send)

# 	for i in range(len(contacts.keys())):
# 		print str(i +1) + ". " + str(contacts.keys()[i])
# 	input = int(raw_input("What entry do you want to update?")
# 		for i in len(contacts.keys():
# 			if input == i + 1


	# which name (key do you want)? (ignore updating the name for now)
	# which category do you want to update?
	# gimme what you want to update it with


if __name__ == '__main__':
	main()