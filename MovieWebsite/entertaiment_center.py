import fresh_tomatoes
import media

# Instanitiate movie objects and put them into movie_list array
avatar = media.Movie(
    "Avatar",
    "2h 42m",
    "On the lush alien world of Pandora live the Na'vi...",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://youtu.be/cRdxXPV9GNQ")

inside_out = media.Movie(
    "Inside out",
    "1h 42m",
    "A girl named Riley is born in Minnesota...",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
    "https://youtu.be/yRUAzGQ3nSY")

mi5 = media.Movie(
    "Mission: Impossible",
    "2h 11m",
    "After intercepting nerve gas being sold to terrorists...",
    "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",
    "https://youtu.be/E66Cimpp9Vw")

movie_list = [avatar, inside_out, mi5]

# Generate the static html with fresh_Tomatoes.py
fresh_tomatoes.open_movies_page(movie_list)

