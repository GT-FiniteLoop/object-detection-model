import cv2
import numpy as np
import tensorflow as tf

def detect(image_frame):
    # TODO(): Encode image based on ML framework
    # and implement object detection logic
    confidence = 100.0
    return confidence

def transform_frame(frame):
    numpy_frame = np.asarray(frame)
    numpy_frame = cv2.normalize(numpy_frame.astype('float'), None, -0.5, .5, cv2.NORM_MINMAX)
    numpy_final = np.expand_dims(numpy_frame, axis=0)
    return numpy_final

def live_feed():
    camera = cv2.VideoCapture(0)
    while(1):
        # Capture frame from camera
        ret, frame = camera.read()
        frame = cv2.resize(frame, (299, 299), interpolation=cv2.INTER_CUBIC)
        # Adhere to TS graph input structure
        numpy_final = transform_frame(frame)
        if (detect(numpy_final) > .85):
            # TODO(): Alert security personnel
        # Break from feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

def youtube_video_feed(link):
    # Optional

def google_image_search_feed():
    # TODO(): use chromedriver extension
    # https://github.com/hardikvasa/google-images-download#arguments

def local_video_feed(filename):

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--feed', default='live')
    with tf.Session() as sess:
        feed_

        if parser.parse_args().threshold
        # # Execute surveillance:
        # live_feed()
        # youtube_video_feed()
        # google_image_search_feed()
        # local_video_feed()
