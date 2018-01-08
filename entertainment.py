import fresh_tomatoes
import media

toy_story=media.Movie("Toy Story",
                      "A STORY OF BOY AND TOYS",
                   "https://resizing.flixster.com/QRH1navu0bXS9M80XkcWuW3EuVo=/206x305/v1.bTsxMTIwNzIwNztqOzE3MzY0OzEyMDA7MjE5MDsyOTIw",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

bahubali = media.Movie("Bahubali"," Story of Rajmouli",
                       "https://s1-ssl.dmcdn.net/MfFk3/1280x720-Gcm.jpg",
                       "https://www.youtube.com/watch?v=qD-6d8Wo3do")
#print(bahubali.storyline)
#bahubali.show_trailer()

noor = media.Movie("Noor","Story of a reporter",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/Noor_Poster.jpg/220px-Noor_Poster.jpg",
                    "https://www.youtube.com/watch?v=DHuM6C6EyXE")


smurfs =media.Movie("Smurfs","An animation movie",
                    "http://vignette2.wikia.nocookie.net/smurfs/images/3/30/The-art-of-smurfs-the-lost-village-11792.png/revision/latest?cb=20161102184121",
                    "https://www.youtube.com/watch?v=9NO8wk4n1Cs")
movies = [toy_story,bahubali,noor,smurfs]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.valid_ratings)
