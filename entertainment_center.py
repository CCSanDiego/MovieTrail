import fresh_tomatoes
import media

life_of_pi = media.Movie(
    "Life of Pi",
    "A Canadian fantasy adventure novel by Yann Martel published in 2001",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcQLik2EaN6bm4GQBKTvI7uIlH4b5kQ29IhY1Tqh_nEoHkUsru82",
    "https://www.youtube.com/watch?v=3Mnw7mTV9fE")
#life_of_pi.show_trailer()

babbettes_feast = media.Movie(
    "Babettes Feast",
    "A strict religious community in a Danish village takes in a French refugee from the Franco-Prussian War as a servant to the late pastor's daughters",   # noqa
    "https://images-na.ssl-images-amazon.com/images/I/51A2BJ1WTML._SY445_.jpg",
    "https://www.youtube.com/watch?v=SvNifgj_dv4")
#babbette's_feast.show_trailer()

big_wednesday = media.Movie(
    "Big Wednesday",
    "Three young surfer dudes from 1962 to 1974, as they catch waves, fight, have sex and try – successfully on the whole – to avoid growing up",   # noqa
    "http://www.gstatic.com/tv/thumb/movieposters/1262/p1262_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=yM96M_vv8rM")
#big_wednesday.show_trailer()

the_endless_summer_2 = media.Movie(
    "The Endless Summer 2",
    "Documentary · Bruce Brown, king of surfing documentaries, returns after nearly thirty years to trace the steps of two young surfers to top surfing spots around the world",    # noqa
    "https://static1.squarespace.com/static/51a2c934e4b00f4428931116/52d5a349e4b0c4f1c24c632c/51b18b22e4b00987e7d75257/1449254588506/The+Endless+Summer+II+movie+poster+Bruce+Brown.JPG?format=500w",   # moqa
    "https://www.youtube.com/watch?v=4hh4Mc7mtJE")
#the_endless_summer.show_trailer()

hair = media.Movie(
    "Hair",
    "Claude Bukowski leaves the family ranch in Oklahoma for New York where he is rapidly embraced into the hippie group of youngsters",      # noqa
    "https://images-na.ssl-images-amazon.com/images/I/51BPLT26BPL._SY445_.jpg",
    "https://www.youtube.com/watch?v=tC0FRKPuZM4")
#hair.show_trailer()
#print(hair.storyline)

the_sting = media.Movie(
    "The Sting",
    "The Sting is a 1973 American caper film set in September 1936, involving a complicated plot by two professional grifters to con a mob boss (Robert Shaw)",     # noqa
    "http://t1.gstatic.com/images?q=tbn:ANd9GcT3Ad2xVqEKYf51DnXpbpBo_gMZuN_BWp6SkVXNsf7NKQOzPLB5",
    "https://www.youtube.com/watch?v=LN2hBOIXhBs")
#the_sting.show_trailer()

movies = [life_of_pi, babbettes_feast, big_wednesday, the_endless_summer_2, hair, the_sting]
fresh_tomatoes.open_movies_page(movies)


