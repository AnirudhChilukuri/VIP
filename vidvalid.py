import cv2
from ultralytics import YOLO

# Load the custom YOLOv8 model
model = YOLO('/Users/anirudhchilukuri/Desktop/VIproj/best3.pt')

# Define class names (replace with your actual class names)
class_names = ["manhole", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
              "traffic light", "bench", "bird", "cat",
              "dog", "cow", "backpack", "umbrella",
                "ball", "skateboard", "chair", "sofa", "pottedplant", "bed",
              "table", "toilet", "tv", "cell phone",
               "sink", "refrigerator", "book", "vase", "person"]

# Open the video file
video_path = '/Users/anirudhchilukuri/Desktop/VIproj/Tourists Love THIS London Weather? Grey & Rainy Central London Walk - 4K HDR 60FPS.mp4'
cap = cv2.VideoCapture(video_path)

# Get video details
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Prepare to save the output video
output_path = 'output_video3.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Define a function to draw bounding boxes
def draw_boxes(frame, boxes, scores, classes):
    for box, score, cls in zip(boxes, scores, classes):
        x1, y1, x2, y2 = map(int, box)
        label = f'{class_names[int(cls)]} {score:.2f}'  # Get class name from class_names list
        # Draw the bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Put the label above the bounding box
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame

# Process the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)
    
# Iterate over each result in the results list
    for result in results:
        # Extract bounding boxes, scores, and classes
        boxes = result.boxes.xyxy.cpu().numpy()  # x1, y1, x2, y2
        scores = result.boxes.conf.cpu().numpy()  # confidence scores
        classes = result.boxes.cls.cpu().numpy()  # class indices

        # Draw bounding boxes on the frame
        frame = draw_boxes(frame, boxes, scores, classes)


    # Write the frame to the output video
    out.write(frame)

    # Optionally display the frame (comment out if running on a headless server)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
