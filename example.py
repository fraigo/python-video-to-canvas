import sys
from video_convert import video_to_js

try:
    filein = sys.argv[1]
    fileout = "html/video.js"
    video_to_js(filein, 120, 150, 1, 15, fileout)
except:
    print("Usage: %s video_file" % sys.argv[0])
