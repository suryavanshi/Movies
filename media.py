import webbrowser

class Movie():
    """Movie Class-Provides a way to store Movie related information"""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title #these are instance vars accessible by object
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
