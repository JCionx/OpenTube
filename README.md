<h1>OpenTube - A Lightweight YouTube Client</h1>
<h2>How to install OpenTube:</h2>
<h3>- Install VLC 64-Bit</h3>
<a href="https://get.videolan.org/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe">Download VLC 64-Bit for Windows</a>
<br>
<a href="https://get.videolan.org/vlc/3.0.17.3/macosx/vlc-3.0.17.3-intel64.dmg">Download VLC 64-Bit for MacOS with Intel Processors</a>
<br>
<a href="https://get.videolan.org/vlc/3.0.17.3/macosx/vlc-3.0.17.3-arm64.dmg">Download VLC 64-Bit for MacOS with Apple Processors</a>
<br>
<h3>- Install Python</h3>
<a href="https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe">Download Python 64-Bit for Windows</a>
<br>
<a href="https://www.python.org/ftp/python/3.10.5/python-3.10.5-macos11.pkg">Download Python 64-Bit for MacOS</a>
<br>
<h3>- Install the python libraries (run the commands in teminal)</h3>
<p>- Instal python-vlc</p>
```
pip3 install python-vlc
```
<br>
<p>- Install pafy</p>
```
pip3 install pafy
```
<br>
<p>- Install youtube-dl</p>
```
pip3 install youtube-dl
```
<br>
<p>- Install urllib</p>
```
pip3 install urllib
```
<br>
<h3>- Download the OpenTube latest release and fix the error</h3>
<p>- Execute the python file.</p>
<p>- Open the path that appears in the error. That path should end in "backend_youtube_dl.py".</p>
<p>- Edit that file, and comment the lines 53, and 54 by adding an "#" in the beggining of them.</p>
<p>- Save the file.</p>
<br>
<h3>Thats it! Run the python file, search any video, and wait for it to play!</h3>
<p>This project is just in beta, so don´t expect anyting awesome.</p>
