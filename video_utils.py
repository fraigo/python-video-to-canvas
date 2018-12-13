import cv2


def resize_frame(frame, view_width, view_height):
        height, width, _ = frame.shape
        reduction_factor = (float(view_height)) / height * 100
        reduced_width = int(width * reduction_factor / 100)
        reduced_height = int(height * reduction_factor / 100)
        dim = (reduced_width, reduced_height)
        resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_LINEAR)
        return resized_frame


def pixel_to_rgb(pixel):
    bgr = tuple(float(x) for x in pixel[:3])
    return tuple(reversed(bgr))


def get_video(filename):
    return cv2.VideoCapture(filename)


def get_video_props(cap):
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    length = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    return width, height, length, fps


def get_frame(cap, view_width=None, view_height=None):
    while cap.isOpened():
        _ret, frame = cap.read()
        if frame is None:
            break
        else:
            if view_height is None or view_width is None:
                yield frame
            else:
                yield resize_frame(frame, view_width, view_height)
