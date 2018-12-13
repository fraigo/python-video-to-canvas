
function VideoPlayer(canvasId, video){

    var canvas = document.getElementById(canvasId);
    var ctx = canvas.getContext('2d');
    var lastFrame = []
    var lastVideo = 0

    canvas.setAttribute("width",video.width)
    canvas.setAttribute("height",video.height)


    this.playVideo=function(video,freq){
        fps=freq
        if (!fps){
            fps=video.freq
        }
        console.log("Playing at "+fps+"fps")
        for(var i=0; i<video.data.length-1; i++){
            lastFrame[i]=setTimeout(this.playFrame.bind(this),fps*i,i,video.data[i],video)
        }
        lastVideo=setTimeout(this.playVideo.bind(this),fps*video.data.length-2,video,freq)
    }

    this.writeText=function(ctx,text, px){
        ctx.font = '10px Arial';
        ctx.fillStyle='white';
        ctx.fillText(text, px+5, 10);
        ctx.fillText(text, px+7, 12);
        ctx.fillStyle='black';
        ctx.fillText(text, px+6, 11);
    }

    this.playFrame=function(i,frame,video){
        ctx.fillRect(0,0,video.width,video.height)
        var d = ctx.createImageData(video.frame_width, video.frame_height);
        var f=0; 
        for(var px=0;px<frame.length; px++){
            var value=parseInt(frame[px],10)
            d.data[f]=value*26; f++;
            if((px+1)%3==0){ 
                d.data[f]=255; 
                f++; 
            } 
        }
        var padx=(video.width-video.frame_width)/2
        ctx.putImageData(d, padx, 0);
        this.writeText(ctx,"Frame "+i,padx)
    }

    this.stopVideo=function(){ 
        this.pauseVideo();
        window.clearTimeout(lastVideo) 
        lastVideo=0
    }

    this.pauseVideo=function(){ 
        for(var f=0; f<lastFrame.length; f++){
            window.clearTimeout(lastFrame[f]) 
        }
        lastFrame=[]
    }

    this.startVideo=function(){
        if (lastFrame.length){
            return
        }
        this.playVideo(video) 
    }

}
