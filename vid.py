import cv2 as cv
import numpy as np
from mtcnn import MTCNN

def detect_face_in_first_frame(video_path):
    cap = cv.VideoCapture(video_path)
    detector = MTCNN()

    # Read the first frame
    ret, frame = cap.read()
    if not ret:
        raise ValueError("Cannot read video file")

    # Convert the frame to RGB and detect faces
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    faces = detector.detect_faces(frame_rgb)

    cap.release()

    if len(faces) == 0:
        raise ValueError("No faces detected in the first frame")

    # Get the bounding box of the first detected face
    face_data = faces[0]
    if 'box' not in face_data:
        raise ValueError("Face detection returned invalid data")

    x1, y1, width, height = face_data['box']
    x2, y2 = x1 + width, y1 + height

    return (x1, y1, x2, y2)

def expand_bbox(bbox, padding, frame_shape):
    """
    Expands the bounding box by adding padding.
    """
    x1, y1, x2, y2 = bbox
    h, w, _= frame_shape

    # Expand the bounding box with padding
    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(w, x2 + padding)
    y2 = min(h, y2 + padding)

    return (x1, y1, x2, y2)

def crop_video_to_face(input_video_path, output_video_path, bbox, padding):
    cap = cv.VideoCapture(input_video_path)
    fps = int(cap.get(cv.CAP_PROP_FPS))
    
    # Get frame size from the expanded bbox
    frame = cap.read()[1]
    if frame is None:
        raise ValueError("Cannot read frame from video")

    expanded_bbox = expand_bbox(bbox, padding, frame.shape)
    frame_width = expanded_bbox[2] - expanded_bbox[0]
    frame_height = expanded_bbox[3] - expanded_bbox[1]

    # Define codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Expand the bounding box for the current frame
        expanded_bbox = expand_bbox(bbox, padding, frame.shape)

        # Crop the frame to the expanded bounding box
        x1, y1, x2, y2 = expanded_bbox
        cropped_frame = frame[y1:y2, x1:x2]

        if cropped_frame.size == 0:
            print("Cropped frame is empty.")
            continue

        out.write(cropped_frame)

    cap.release()
    out.release()
    cv.destroyAllWindows()

# Define paths
input_video_path = 'C:/Users/ebrahem/Data Science/Lip-Sync/Resources/Video/13_K.mp4'
output_video_path = 'C:/Users/ebrahem/Data Science/Lip-Sync/Resources/Video/cropped_face_video_1.mp4'
padding = 30  # Adjust padding as needed

# Detect face position in the first frame
bbox = detect_face_in_first_frame(input_video_path)

# Crop video based on detected face position with padding
crop_video_to_face(input_video_path, output_video_path, bbox, padding)
