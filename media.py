#import the webbrowser library 
import webbrowser

#Class creation 
class Movie():
      """ this funtion define the paramters of the movie """"

     def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,film_rating):
         self.title = movie_title
         self.storyline = movie_storyline
         self.poster_image_url = poster_image
         self.trailer_youtube_url = trailer_youtube
         self.rating=film_rating


     def show_trailer(self):
        """show_trailer() is for open the trailer url in the web brower
        when the string run the web browser will be opened
        """
        webbrowser.open(self.trailer_youtube_url) 

