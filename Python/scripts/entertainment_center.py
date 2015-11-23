import fresh_tomatoes
import media

big_lebowski = media.Movie("The Big Lebowski", 
	"THE DUDE DOES DOPE SHIT",
	"http://cstpdx.com/sites/clinton/files/The-Big-Lebowski-movies-25347166-1400-1000.jpg",
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")

darjeeling = media.Movie("The Darjeeling Limited",
	"Some random movie set in india",
	"http://www.foxsearchlight.com/media/blog_post_images/darj.jpg",
	"https://www.youtube.com/watch?v=aO1bYukdvLI")

boyz = media.Movie("Boyz n the hood",
	"Hood lyfe shenanigans",
	"http://ia.media-imdb.com/images/M/MV5BMTYyNTY2MTQ5N15BMl5BanBnXkFtZTgwNDg3MjkyMTE@._V1_SX640_SY720_.jpg",
	"https://www.youtube.com/watch?v=J4sKiGkzKJo")

almost_famous = media.Movie("Almost Famous",
	"No idea what this is about",
	"http://ia.media-imdb.com/images/M/MV5BMTI0MDc0MzIyM15BMl5BanBnXkFtZTYwMzc4NzA5._V1_SX640_SY720_.jpg",
	"https://www.youtube.com/watch?v=qk0XnyrENrE")
							 
her = media.Movie("her",
	"Guy falls in love with computer",
	"https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
	"https://www.youtube.com/watch?v=WzV6mXIOVl4")
							 

lion_king = media.Movie("Lion King",
	"AAHHHHHSABANYAAAABABAGANEECHAWABAAAAAAAA",
	"https://www.movieposter.com/posters/archive/main/108/MPW-54063",
	"https://www.youtube.com/watch?v=4sj1MT05lAA")
							 

movies = [big_lebowski, darjeeling, boyz, almost_famous, her, lion_king]
#fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)