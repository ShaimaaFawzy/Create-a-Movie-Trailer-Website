#import media class
import media
#import fresh_tomatoes class
import fresh_tomatoes

#Define the movies  
finding_nemo = media.Movie("Finding Nemo",
	"Finding Nemo is a 2003 American computer-animated adventure film produced by Pixar Animation Studios",
	"https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",  
	"https://www.youtube.com/watch?v=wZdpNglLbt8",
        "8.1")  
lion_king = media.Movie("The Lion King",
	"The Lion King is a 1994 American animated epic musical film produced by Walt Disney Feature Animation and released ",
	"https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  
	"https://www.youtube.com/watch?v=_ujGv5dhGfk",
        "8.5")  


inside_out  = media.Movie("Inside Out ",
	"Inside Out is a 2015 American 3D computer-animated comedy-drama film produced by Pixar Animation Studios",
	"https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",  
	"https://www.youtube.com/watch?v=seMwpP0yeu4",
        "8.2")  

# appending movies into a list 
movies = [finding_nemo, lion_king, inside_out]

# buinding the data from the movie class to fresh_tomatoes page
fresh_tomatoes.open_movies_page(movies)
