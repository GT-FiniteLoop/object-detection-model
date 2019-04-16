import cv2
import numpy as np
import tensorflow as tf
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import argparse

from collections import defaultdict
from io import StringIO
from PIL import Image

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


sys.path.append("..")

from utils import label_map_util
from utils import visualization_utils as vis_util


MODEL_NAME = 'firearm_graph_v6.pb'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'label_map.pbtxt')

NUM_CLASSES = 1


detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


def detect(image_np):
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    # Each box represents a part of the image where a particular object was detected.
    boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    # Each score represent how level of confidence for each of the objects.
    # Score is shown on the result image, together with the class label.
    scores = detection_graph.get_tensor_by_name('detection_scores:0')
    classes = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')
    # Actual detection.
    (boxes, scores, classes, num_detections) = sess.run(
      [boxes, scores, classes, num_detections],
      feed_dict={image_tensor: image_np_expanded})
    # Visualization of the results of a detection.
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8)
    cv2.imshow('object detection', cv2.resize(image_np, (800,600)))

    # TODO(): Map 'scores' above to confidence
    confidence = 100.0
    return confidence

def transform_frame(frame):
    numpy_frame = np.asarray(frame)
    numpy_frame = cv2.normalize(numpy_frame.astype('float'), None, -0.5, .5, cv2.NORM_MINMAX)
    numpy_final = np.expand_dims(numpy_frame, axis=0)
    return numpy_final

def live_feed():
    while(1):
        # Capture frame from camera
        ret, frame = camera.read()
        # frame = cv2.resize(frame, (299, 299), interpolation=cv2.INTER_CUBIC)
        # Adhere to TF graph input structure
        # numpy_final = transform_frame(frame)
        numpy_final = frame
        if (detect(numpy_final) > .85):
            # TODO(): Alert security personnel
            # continue
            print("Gun detected!")
        # Break from feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

def youtube_video_feed(link):
    # Optional
    return None

def google_image_search_feed():
    # TODO(): use chromedriver extension
    # https://github.com/hardikvasa/google-images-download#arguments
    return None

def local_video_feed():
    while(camera.isOpened()):
        # Capture frame from camera
        ret, frame = camera.read()
        # frame = cv2.resize(frame, (299, 299), interpolation=cv2.INTER_CUBIC)
        # Adhere to TF graph input structure
        # numpy_final = transform_frame(frame)
        numpy_final = frame
        if (detect(numpy_final) > .85):
            # TODO(): Alert security personnel
            # continue
            print("Gun detected!")
        # Break from feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', default='live')
    parser.add_argument('--video')
    args = parser.parse_args()

    with detection_graph.as_default():
      with tf.Session(graph=detection_graph) as sess:
        # Execute surveillance:
        if args.mode == "live":
            camera = cv2.VideoCapture(0)
            if camera is None or not camera.isOpened():
                print("No available camera.")
                exit()
            try:
              live_feed()
            except KeyboardInterrupt:
              print("Execution ended by user.")
              exit()
        # youtube_video_feed()
        # google_image_search_feed()
        if args.mode == "local" and args.video:
            camera = cv2.VideoCapture(args.video)
            if camera is None or not camera.isOpened():
                print("Unabel to open provided file. Check filename")
                exit()
            try:
                local_video_feed()

            except KeyboardInterrupt:
              print("Execution ended by user.")
              exit()
        elif args.mode == "local":
            print("Local usage: python model.py --mode local --video <video file>")
