import os, requests, json, sys

#nobody can be told what the matrix is...
def intro():
	os.system("clear")
	print "Yolo, stranger!"
	print "Here's how this works:"
	print "You tell me what section of The New York Times you're interested in," 
	print "and I'll give you the most recent headlines from that section."
	while True:
		switch = raw_input("Sound good? y/n ")
		if switch.lower() == "n":
			print "Bummer."
			sys.exit()
		elif switch.lower() == "y":
			break
		else:
			print "Sorry, I didn't get that."
			continue
	menu()

#launch our section menu
def menu():
	os.system('clear')
	print "Here's the list of New York Times sections."
	print "Just enter the number of the section you'd like to see headlines from, and hit return."
	print "Home [1]"
	print "World [2]"
	print "National [3]"
	print "Politics [4]"
	print "NY Region [5]"
	print "Business [6]"
	print "Opinion [7]"
	print "Technology [8]"
	print "Science [9]"
	print "Health [10]"
	print "Sports [11]"
	print "Arts [12]"
	print "Fashion [13]"
	print "Dining [14]"
	print "Travel [15]"
	print "Magazine [16]"
	print "Real Estate [17]"
	print "Or, if you want to quit, press [0]."
	while True:
		section_num = raw_input(">> ")
		if int(section_num) == 0:
			print "Goodbye!"
			sys.exit();
		elif int(section_num) > 17:
			print "That's not a section. Try again."
			continue
		else:
			get_stories(int(section_num))

#talk to the New York Times Top Stories API
def get_stories(section):
	load_section = dict[section]
	app_name = "NYT_TOP_STORIES"
	api_key = os.environ.get(app_name + "_KEY")
	api_url = "http://api.nytimes.com/svc/topstories/v1/%s.json?api-key=%s" % (load_section, api_key)
	response = requests.get(api_url)
	json_obj = json.loads(response.content)
	os.system("clear")
	for item in json_obj['results']:
		print item['title']
	while True:
		print("\nTo go back to the sections list, press 1. To quit, press 0.")
		choice = raw_input(">> ")
		if choice == "1":
			menu()
		elif choice == "0":
			sys.exit()
		else:
			print "Sorry, I didn't get that."
			continue

#a dictionary with section values for the API
dict = {1:"home", 2:"world", 3:"national", 4:"politics", 5:"nyregion", 6:"business", 7:"opinion", 8:"technology", 9:"science", 10:"health", 11:"sports", 12:"arts", 13:"fashion", 14:"dining", 15:"travel", 16:"magazine", 17:"realestate"}

if __name__ == "__main__":
	intro()
