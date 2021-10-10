# %%
import threading  # threading for creating threads
# imports from library to interface with the api of the  tmdb
from tmdbv3api import Movie, TMDb
tmdb = TMDb()
# this is my own api key
tmdb.api_key = 'obfuscated'
# declares language to search movies in
tmdb.language = 'en'
# this makes it so the response from the api is printed
tmdb.debug = False
# object of the Movie call from tmdb
movie = Movie()
MVIDS = []
# function to find a movie by a given title
def get_movie(arg):
    search = movie.search(arg)  # object from movie to search in tmdb
    # IF CASE there is no response, its not great, I should've managed exceptions and not worked around  them.
    if len(search) == 0:
        print("NO MATCHING TITLE FOUND. TRY AGAIN")
        get_movie(input("Enter the movie title to search: "))
    movie_id = search[1]['id']  # gets movie id in tmdb
    overview = search[1]['overview']  # synopsis
    print('\n####', search[1]['original_title'], "####")  # show title
    print(overview)  # show synopsis
    MVIDS.append(movie_id)
    return movie_id
def get_cast(id):
    castlen = len(movie.credits(id)['cast'])
    if castlen < 5:  # makes sure if there are not enough credited people to show.
        cast = movie.credits(id)['cast']
    else:
        cast = movie.credits(id)['cast'][:5]
    print('TOP 5 CREDITED:')
    # print those credited
    for actor in cast:
        print(actor['name'], 'as', actor['character'])
    print('. . . .')
class agent:
    # this is the one that calls every function and starts the threads`
    def __init__(self):
        self.title = input("Enter the movie title to search: ")
        self.ask(self.title)
    def ask(self, title):
        # this asks the function but calling them as threads.
        self.movie1 = threading.Thread(
            target=get_movie, args=(str(self.title),))
        self.movie1.start()
        self.movie1.join()
        self.cast1 = threading.Thread(target=get_cast, args=(MVIDS[0],))
        self.cast1.start()
        self.cast1.join()
if __name__ == "__main__":
    asker = agent()
    answers = ['y', 'yes', 'ye', 'ys']
    # this keeps asking if you want to keep searching for movies
    while input('Want to search another movie [Yes/N]?').lower() in answers:
        print()
        asker = agent()
