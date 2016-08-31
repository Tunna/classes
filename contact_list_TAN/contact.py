contact_list = []

class Contacts(object):
	def __init__(self, first_name, last_name, mobile = "", work_number = "", email = "", twitter_handle = ""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile = mobile
		self.work_number = work_number
		self.email = email
		self.twitter = twitter_handle

	def send_text(self, message):
		if self.mobile:
			print "To: %s - %s" % (self.mobile, message)
		else:
			print "Nice try! Please add a mobile number to text."


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