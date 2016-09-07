from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"

#open the apiUrl and assign data to variable
response = urlopen(apiUrl)

json_obj = load(response)

def sf_film():
	list_2002 = []

	for i in json_obj:

		if i["release_year"] == "2002" and i["title"] not in list_2002:
			print i["title"]
			list_2002.append(i["title"])

def main():
	sf_film()

if __name__ == '__main__':
	main()
