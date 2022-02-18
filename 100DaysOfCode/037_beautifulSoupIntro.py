from bs4 import BeautifulSoup
import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("What date do you want to travel to? Type a date in the format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")


songs = soup.find_all(name="h3", class_=re.compile("c-title a-no-trucate"))

song_names = [song.getText().strip() for song in songs]

print(song_names)

# ###### SPOTIFY PORTION I DON'T UNDERSTAND ############################################################################
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
#
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
#
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# # print(playlist)
#
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# #####################################################################################################################

# # Top 100 Movies List ________________________________________________________________________________________
# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# movies_page = response.text
# soup = BeautifulSoup(movies_page, "html.parser")
#
# titles = soup.find_all(name="h3", class_="title")
#
# title_list = [title.getText() for title in titles][::-1]
#
# title_text = ""
# for title in title_list:
#     title_text += title + "\n"
#
# print(title_text)
#
# with open("topMovies.txt", mode="w") as file:
#     file.write(title_text)
#



# # Y Combinator Top News Article ________________________________________________________________________________________
#
# response = requests.get("https://news.ycombinator.com/")
# yc_page = response.text
# soup = BeautifulSoup(yc_page, "html.parser")
#
# titles = soup.find_all(class_="titlelink")
# scores = soup.find_all(class_="score")
#
# title_list = [title.getText() for title in titles]
# link_list = [title.get("href") for title in titles]
# score_list = [int(score.getText().split()[0]) for score in scores]
#
# top_score_index = score_list.index(max(score_list))
#
# print(score_list[top_score_index], title_list[top_score_index], link_list[top_score_index])



# # Beautiful Soup Intro
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
#
# for tag in all_anchor_tags:
#     # Get all text from anchor tags
#     print(tag.getText())
#     # Get all of the links in the anchor tags
#     print(tag.get("href"))
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)