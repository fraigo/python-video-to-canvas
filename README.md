# Python Video to HTML Canvas Demo

This script can create a Javascript object with video information from a video file.

The javascript object can be played in **HTML Canvas** as a sequence of frames with pixel data.


## Python packages

* `opencv-python`: OpenCV, Open Source Computer Vision Library. BSD license and hence it’s free for both academic and commercial use.

## Usage

### Python code example

```python
import sys
from video_convert import video_to_js

filein = "example/multi.mov"
fileout = "html/video.js"
video_to_js(filein, 200, 200, 1, 15, fileout)
```

### Video example (included)

This example will generate the file `html/video.js`:

`python example.py example/multi.mov`



### Javascript Video usage


Use this code snippet to embed your video in Canvas

```html
<canvas id=canvas></canvas>    
<script src="video.js" ></script>
<script src="player.js" ></script>
<script >
document.body.onload=function(){ 
    var player = new VideoPlayer("canvas", video)
    player.startVideo()
}
</script>
```

Where `video.js` is the video file generated by the script, and `player.js` is the Video player component to play the video vile format.


## Online Demo

Check the example in https://fraigo.github.io/python-video-to-canvas/html/index.html


