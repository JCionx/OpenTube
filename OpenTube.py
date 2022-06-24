# You need to install VideoLan 64-bit and this libs:
# - python-vlc
# - pafy
# - urllib
# - re
# - youtube-dl
# - tkinter
# Goto backend-youtube-dl.py and comment lines 53, and 54

import tkinter as tk
import urllib.request
import re
import pafy
import vlc
import base64

def runVideo(url):
    video = pafy.new(url)

    best = video.getbest()

    ins = vlc.Instance()
    player = ins.media_player_new()

    code = urllib.request.urlopen(url).getcode()
    if str(code).startswith('2') or str(code).startswith('3'):
        print('Stream is working fine.')
    else:
        print('Stream is NOT working. Please try again.')

    Media = ins.media_new(best.url)
    Media.get_mrl()
    player.set_media(Media)
    player.play()

    good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]

    while str(player.get_state()) in good_states:
        nothing = 0
    
    player.stop()

def search():

    root.geometry("400x520")

    nonmduser = str(E1.get())
    user = nonmduser
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
    video_urls = [f"https://www.youtube.com/watch?v={video_ids[0]}", f"https://www.youtube.com/watch?v={video_ids[1]}", f"https://www.youtube.com/watch?v={video_ids[2]}"]
    videos = [pafy.new(video_urls[0]), pafy.new(video_urls[1]), pafy.new(video_urls[2])]
    
    def videoOne():
        url = video_urls[0]
        runVideo(url)
    
    def videoTwo():
        url = video_urls[1]
        runVideo(url)

    def videoThree():
        url = video_urls[2]
        runVideo(url)
    
    L1.destroy()
    E1.destroy()
    B1.destroy()

    L2 = tk.Label(root, text=f"\nShowing results for '{nonmduser}'", font="Calibri")
    L2.pack()

    LV1 = tk.Label(root, text=f"\n {videos[0].title}\n Channel: {videos[0].author}\n {videos[0].viewcount} views", wraplength=400, font="Calibri", justify=tk.LEFT)
    LV1.pack(anchor=tk.W)
    BV1 = tk.Button(root, text="Watch", command=videoOne, font="Calibri", width=29)
    BV1.pack()

    LV2 = tk.Label(root, text=f"\n {videos[1].title}\n Channel: {videos[1].author}\n {videos[1].viewcount} views", wraplength=400, font="Calibri", justify=tk.LEFT)
    LV2.pack(anchor=tk.W)
    BV2 = tk.Button(root, text="Watch", command=videoTwo, font="Calibri", width=29)
    BV2.pack()

    LV3 = tk.Label(root, text=f"\n {videos[2].title}\n Channel: {videos[2].author}\n {videos[2].viewcount} views", wraplength=400, font="Calibri", justify=tk.LEFT)
    LV3.pack(anchor=tk.W)
    BV3 = tk.Button(root, text="Watch", command=videoThree, font="Calibri", width=29, )
    BV3.pack()

# Tkinter configs
root = tk.Tk()
root.title("OpenTube")
root.geometry("400x190")
root.resizable(0, 0)

opentubetext = tk.PhotoImage(data=base64.encodebytes(urllib.request.urlopen("https://i.imgur.com/0l1swMT.png").read()))

C1 = tk.Canvas(root, width=300, height=90)
C1.pack()
C1.create_image(20, 20, image=opentubetext, anchor='nw')

# Search Window
L1 = tk.Label(root, text="Search video", font="Calibri")
L1.pack()
E1 = tk.Entry(root, width=30, font="Calibri")
E1.pack()
B1 = tk.Button(root, text="Search", command=search, width=29, font="Calibri")
B1.pack()

root.mainloop()
