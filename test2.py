from youtubesearchpython import Hashtag

hashtag = Hashtag('ncs', limit = 2)

print(hashtag.result()['type'])

input()