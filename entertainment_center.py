import media #as the name of file is media
import fresh_tomatoes

#creating instance of class Media from file media.py
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on Alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

schoolrock = media.Movie("School of Rock",
                         "About rock music",
                         "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                         "https://www.youtube.com/watch?v=3PsUJFEBC74")

hungergames = media.Movie("Hunger Games",
                          "Fighting of district",
                          "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=PbA63a7H0bo")
                          
movies = [toy_story,avatar,schoolrock,hungergames]
fresh_tomatoes.open_movies_page(movies)
print media.Movie.VALID_RATINGS
print media.Movie.__doc__
#print(toy_story.storyline)
#toy_story.show_trailer()
