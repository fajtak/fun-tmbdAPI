import requests

def test():
	req = requests.get("https://api.themoviedb.org/3/movie/76341?api_key=fb3d514ef28708534a2c617322cacaf1&language=en")
	print(req.text)

def SearchMovie(query):
	req = requests.get("https://api.themoviedb.org/3/search/movie?api_key=fb3d514ef28708534a2c617322cacaf1&query=" + query)
	results = req.json()
	for item in results["results"]:
		print(item["original_title"],item["release_date"].split("-")[0],item["vote_average"],item["popularity"])
	# print(req.text)

def SearchTV(query):
	req = requests.get("https://api.themoviedb.org/3/search/tv?api_key=fb3d514ef28708534a2c617322cacaf1&query=" + query)
	results = req.json()
	# print(results)
	for item in results["results"]:
		print(item["original_name"],item["first_air_date"].split("-")[0],item["vote_average"],item["popularity"],item["origin_country"])

def SearchMulti(query):
	req = requests.get("https://api.themoviedb.org/3/search/multi?api_key=fb3d514ef28708534a2c617322cacaf1&query=" + query)
	results = req.json()
	# print(results)
	for item in results["results"]:
		print(item)

def GetTrending(query):
	req = requests.get("https://api.themoviedb.org/3/trending/all/week?api_key=fb3d514ef28708534a2c617322cacaf1")
	results = req.json()
	# print(results)
	for item in results["results"]:
		# print(item)
		if query != "" and query not in genresInverse:
			print("Not a valid genre!")
			break
		if query != "" and genresInverse.get(query,"") not in item["genre_ids"]:
			continue
		if (item["media_type"] == "movie"):
			print(item["title"],item["release_date"].split("-")[0],item["vote_average"],item["popularity"],item["media_type"])
			# for genre in item["genre_ids"]:
			# 	print(genres[genre])
		else:
			print(item["name"],item["first_air_date"].split("-")[0],item["vote_average"],item["popularity"],item["media_type"])

def GetGenres():
	req = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=fb3d514ef28708534a2c617322cacaf1")
	# print(req.text)
	genres_list = req.json()["genres"]
	for genre in genres_list:
		genres[genre["id"]] = genre["name"].lower()
		genresInverse[genre["name"].lower()] = genre["id"]
	print(genres)

def GetWatchProvidersRegion():
	req = requests.get("https://api.themoviedb.org/3/watch/providers/regions?api_key=fb3d514ef28708534a2c617322cacaf1")
	print(req.text)

def GetWatchProvidersMovie():
	req = requests.get("https://api.themoviedb.org/3/watch/providers/movie?api_key=fb3d514ef28708534a2c617322cacaf1&watch_region=CZ")
	print(req.text)

def GetWatchProvidersTV():
	req = requests.get("https://api.themoviedb.org/3/watch/providers/tv?api_key=fb3d514ef28708534a2c617322cacaf1&wath_region=CZ")
	print(req.text)

def DiscoverMovie():
	req = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=fb3d514ef28708534a2c617322cacaf1&sort_by=popularity.desc")
	results = req.json()
	print(results)

def GetRecommendations(query):
	req = requests.get("https://api.themoviedb.org/3/search/movie?api_key=fb3d514ef28708534a2c617322cacaf1&query=" + query)
	results = req.json()["results"]
	movie_id = results[0]["id"]
	req = requests.get("https://api.themoviedb.org/3/movie/" + str(movie_id) +"/recommendations?api_key=fb3d514ef28708534a2c617322cacaf1")
	results = req.json()["results"]
	# print(results)
	for item in results:
		print(item["original_title"],item["release_date"].split("-")[0],item["vote_average"],item["popularity"])

genres = {}
genresInverse = {}

if __name__ == "__main__":
	# SearchMovie(input("Search for: "))
	# SearchTV(input("Search for: "))
	# SearchMulti(input("Search for: "))
	GetGenres()
	# GetWatchProvidersRegion()
	# GetWatchProvidersMovie()
	# GetWatchProvidersTV()
	# GetTrending(input("Search for: ").lower())
	# DiscoverMovie()
	GetRecommendations(input("Search for: "))
	input()


# Add discover movies
# Add Movie Recommendations