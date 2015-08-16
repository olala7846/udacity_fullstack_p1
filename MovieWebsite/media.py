import webbrowser


class Movie():
    """This is the class containing informations about a mobie"""

    def __init__(self, movie_title, duration, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.duration = duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


