# You need to install VideoLan 64-bit and this libs:
# - python-vlc
# - pafy
# - urllib
# - re
# - youtube-dl
# Goto backend-youtube-dl.py and comment lines 53, and 54

import urllib.request
import re
import pafy
import vlc

user = input("Search: ")
user = user.replace("%", "%25")
user = user.replace("+", "%2B")
user = user.replace("=", "%3D")
user = user.replace("/", "%\2F")
user = user.replace("\\", "%5C")
user = user.replace("?", "%\3F")
user = user.replace("#", "%23")
user = user.replace("$", "%24")
user = user.replace("|", "%7C")
user = user.replace("@", "%40")
user = user.replace("&", "%26")
user = user.replace("{", "%7B")
user = user.replace("}", "%7D")
user = user.replace("[", "%5B")
user = user.replace("]", "%5D")
user = user.replace("'", "%27")
user = user.replace("`", "%60")
user = user.replace(",", "%2C")
user = user.replace(";", "%3B")
user = user.replace(":", "%3A")
user = user.replace(" ", "+")

html = urllib.request.urlopen(f"https://youtube.com/results?search_query={user}")
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
url = f"https://www.youtube.com/watch?v={video_ids[0]}"

video = pafy.new(url)

best = video.getbest()

print(video_ids)

ins = vlc.Instance()
player = ins.media_player_new()

code = urllib.request.urlopen(url).getcode()
if str(code).startswith('2') or str(code).startswith('3'):
    print('Stream is working')
else:
    print('Stream is dead')

Media = ins.media_new(best.url)
Media.get_mrl()
player.set_media(Media)
player.play()

good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]

pause_state = 1

while str(player.get_state()) in good_states:
    print(f"Stream is working. Current state = {player.get_state}")

player.stop()