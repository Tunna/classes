import contact

contact_list = []

def add_new_contact():	
	first_name = raw_input("First name: ").upper().strip()
	last_name = raw_input("Last name: ").upper().strip()
	mobile_num = raw_input("Mobile number: ").strip()
	work_phone = raw_input("Work phone: ").strip()
	email = raw_input("Email: ").upper().strip()
	twitter_handle = raw_input("Twitter: ").upper().strip()

	new_contact = contact.Contacts(first_name, last_name, mobile = mobile_num, work_number = work_phone, email = email, twitter_handle = twitter_handle)	

	if not contact_list:
		contact_list.append(new_contact)
	else:
		if find_person(first_name, last_name):
			print "This is a duplicate entry."
		else:
			contact_list.append(new_contact)
			
def find_person(first_name, last_name):
	for person in contact_list:
		if first_name == person.first_name and last_name == person.last_name:
			return person
	return None

def show_all_contacts():
	for person in contact_list:
		print person.first_name, person.last_name, person.mobile, person.work_number, person.email, person.twitter

def edit_contact():
	show_all_contacts()
	print "Please selecvt a contact to edit."
	first_name = raw_input("First name: ").upper().strip()
	last_name = raw_input("Last name: ").upper().strip()
	person = find_person(first_name, last_name)

	if person:
		person.first_name = raw_input("First name: ").upper().strip()
		person.last_name = raw_input("Last name: ").upper().strip()
		person.mobile_num = raw_input("Mobile number: ").strip()
		person.work_phone = raw_input("Work phone: ").strip()
		person.email = raw_input("Email: ").upper().strip()
		person.twitter_handle = raw_input("Twitter: ").upper().strip()

def delete_contact():
	print "Please select a contact to remove."
	first_name = raw_input("First name: ").upper().strip()
	last_name = raw_input("Last name: ").upper().strip()
	person = find_person(first_name, last_name)

	if person:
		contact_list.remove(person)		

def main():
	add_new_contact()
	show_all_contacts()
	add_new_contact()
	show_all_contacts()
	edit_contact()
	delete_contact()
	show_all_contacts()


if __name__ == '__main__':
	main()