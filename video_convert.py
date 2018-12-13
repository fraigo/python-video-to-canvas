import sys
from video_utils import get_video, get_video_props, get_frame, pixel_to_rgb


def video_to_js(infile, cwidth, cheight, frame_start, frame_end, outfile=None):
    opacity = 255
    comp = 26
    cap = get_video(infile)
    if outfile is None:
        writer = sys.stdout
    else:
        writer = open(outfile, "w")
        print("Writing to %s ..." % outfile)
    width, height, length, real_fps = get_video_props(cap)
    real_freq = int(1000/real_fps)

    writer.write("video ={\n")
    writer.write('"width":%s,\n' % cwidth)
    writer.write('"height":%s,\n' % cheight)
    writer.write('"fps":%s,\n' % real_fps)
    writer.write('"freq":%s,\n' % real_freq)
    writer.write('"data":[\n')
    fn = 0
    i = 0
    fwidth = 0
    fheight = 0
    for rframe in get_frame(cap, cwidth, cheight):
        fn += 1
        if fn < frame_start:
            continue
        if fn > frame_end:
            break
        fheight, fwidth, _ = rframe.shape
        pad = max(int(cwidth) - fwidth, 0)
        writer.write('"')
        for j in range(fheight-1):
            for i in range(fwidth):
                pixel = rframe[j][i]
                r, g, b = pixel_to_rgb(pixel)
                writer.write("%s" % int(r/comp))
                writer.write("%s" % int(g/comp))
                writer.write("%s" % int(b/comp))
        writer.write('",\n')
        writer.flush()
    writer.write('""\n')
    writer.write(" ],\n")
    writer.write('"frame_width":%s,\n' % fwidth)
    writer.write('"frame_height":%s\n' % fheight)
    writer.write("}\n")
    writer.flush()
