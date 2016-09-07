import MovieInfo_class

from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"

#open the apiUrl and assign data to variable
response = urlopen(apiUrl)

json_obj = load(response)

def get_all_movies():
	MovieInfo_list = []
	#movie_director = director
	# add_release = release_year
	# add_title = title


	for movie in json_obj:
		new_movie = MovieInfo_class.MovieInfo(movie['director'], movie['release_year'], movie['title'], movie.get('actor_1'), movie.get('actor_2'), movie.get('locations'))
		MovieInfo_list.append(new_movie)
	print MovieInfo_list
	
	
		
	# 	if movie["director"] == director and ["release_year"] == release_year and ["title"] == title and ["actor_1"] == actor_1 and ["actor_2"] == actor_2 and ["location"] == location:
	# 		print "im here"

	# print MovieInfo_list

	# for i in json_obj:

	# 	if i["release_year"] == "2002" and i["title"] not in list_2002:
	# 		print i["title"]
	# 		list_2002.append(i["title"])

def main():
	get_all_movies()

if __name__ == '__main__':
	main()