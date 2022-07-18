# You need to install VideoLan 64-bit and this libs:
# - python-vlc
# - pafy
# - urllib
# - re
# - youtube-dl
# - tkinter
# Goto backend-youtube-dl.py and comment lines 53, and 54

# If you're running this script as a .pyw file, you will not be able to download videos.

import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
import urllib.request
import re
import pafy
import vlc
import base64

# ----- Project settings: -----

# Change dark_theme to True to enable dark mode
dark_theme = False

# Change text_font to change the text font
text_font = "Calibri"

bg_color = "white"
text_color = "black"
logo = "https://i.imgur.com/0l1swMT.png"

if dark_theme:
    bg_color = "#363636"
    text_color = "white"
    logo = "https://i.imgur.com/WwXq6eq.png"

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

    root.geometry("400x620")

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

    def getPath(tstr):
        tempNum = 0
        tempStr = ""
        while True:
            if not str(tstr)[tempNum] == "'":
                tempNum += 1
            else:
                tempNum += 1
                while True:
                    if not str(tstr)[tempNum] == "'":
                        tempStr = str(tempStr) + str(tstr)[tempNum]
                        tempNum += 1
                    else:
                        break
                break
        return(tempStr)
    
    def dlVideoOne():
        path = askdirectory()
        url = video_urls[0]
        video = pafy.new(video_ids[0])
        best = video.getbest()
        showinfo("File downloading", "The video is being downloaded. Check the console to see the progress.")
        filename = best.download(path)
        showinfo("File downloaded", f"The video was sucessfully downloaded to {path}")

    def dlVideoTwo():
        path = askdirectory()
        url = video_urls[0]
        video = pafy.new(video_ids[1])
        best = video.getbest()
        showinfo("File downloading", "The video is being downloaded. Check the console to see the progress.")
        filename = best.download(path)
        showinfo("File downloaded", f"The video was sucessfully downloaded to {path}")

    def dlVideoThree():
        path = askdirectory()
        url = video_urls[0]
        video = pafy.new(video_ids[2])
        best = video.getbest()
        showinfo("File downloading", "The video is being downloaded. Check the console to see the progress.")
        filename = best.download(path)
        showinfo("File downloaded", f"The video was sucessfully downloaded to {path}")
    
    L1.destroy()
    E1.destroy()
    B1.destroy()

    L2 = tk.Label(root, text=f"\nShowing results for '{nonmduser}'", font=(text_font, 12), bg=bg_color, fg=text_color)
    L2.pack()

    LV1 = tk.Label(root, text=f"\n {videos[0].title}\n Channel: {videos[0].author}\n {videos[0].viewcount} views", wraplength=400, font=(text_font, 12), justify=tk.LEFT, bg=bg_color, fg=text_color)
    LV1.pack(anchor=tk.W)
    BV1 = tk.Button(root, text="Watch", command=videoOne, font=(text_font, 12), width=29, bg=bg_color, fg=text_color)
    BV1.pack()
    BD1 = tk.Button(root, text="Download", command=dlVideoOne, font=(text_font, 12), width=29, bg=bg_color, fg=text_color)
    BD1.pack()

    LV2 = tk.Label(root, text=f"\n {videos[1].title}\n Channel: {videos[1].author}\n {videos[1].viewcount} views", wraplength=400, font=(text_font, 12), justify=tk.LEFT, bg=bg_color, fg=text_color)
    LV2.pack(anchor=tk.W)
    BV2 = tk.Button(root, text="Watch", command=videoTwo, font=(text_font, 12), width=29, bg=bg_color, fg=text_color)
    BV2.pack()
    BD2 = tk.Button(root, text="Download", command=dlVideoTwo, font=(text_font, 12), width=29, bg=bg_color, fg=text_color)
    BD2.pack()

    LV3 = tk.Label(root, text=f"\n {videos[2].title}\n Channel: {videos[2].author}\n {videos[2].viewcount} views", wraplength=400, font=(text_font, 12), justify=tk.LEFT, bg=bg_color, fg=text_color)
    LV3.pack(anchor=tk.W)
    BV3 = tk.Button(root, text="Watch", command=videoThree, font=(text_font, 12), width=29, bg=bg_color, fg=text_color)
    BV3.pack()
    BD3 = tk.Button(root, text="Download", command=dlVideoThree, font=(text_font, 12), width=29, bg=bg_color, fg=text_color)
    BD3.pack()

# Tkinter configs
root = tk.Tk()
root.title("OpenTube")
root.geometry("400x190")
root.resizable(0, 0)
root.config(bg=bg_color)

opentubetext = tk.PhotoImage(data=base64.encodebytes(urllib.request.urlopen(logo).read()))

C1 = tk.Canvas(root, width=300, height=90, bg=bg_color, highlightthickness=0)
C1.pack()
C1.create_image(20, 20, image=opentubetext, anchor='nw')

# Search Window
L1 = tk.Label(root, text="Search video", font=(text_font, 12), bg=bg_color, fg=text_color)
L1.pack()
E1 = tk.Entry(root, width=30, font=(text_font, 12), bg=bg_color, fg=text_color)
E1.pack()
B1 = tk.Button(root, text="Search", command=search, width=29, font=(text_font, 12), bg=bg_color, fg=text_color)
B1.pack()

root.mainloop()
