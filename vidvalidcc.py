import cv2
from ultralytics import YOLOv10
import supervision as sv
import numpy as np

video_path = '/Users/anirudhchilukuri/Desktop/VIproj/Tourists Love THIS London Weather? Grey & Rainy Central London Walk - 4K HDR 60FPS.mp4'
cap = cv2.VideoCapture(video_path)

# Get video details
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Prepare to save the output video
output_path = 'output_v10_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

def initialize_camera(video_path):
    cap = cv2.VideoCapture(video_path)
    return cap

def load_yolov8_model(model_path="/Users/anirudhchilukuri/Desktop/VIproj/best7.pt"):
    model = YOLOv10(model_path)
    return model

def process_frame(frame, model, box_annotator):
    result = model(frame, agnostic_nms=True)[0]
    detections = sv.Detections.from_ultralytics(result)
    print("----", detections, "----")
    
    # Create labels for the detections
    labels = [
        f"{model.model.names[class_id]} {confidence:.2f}"
        for confidence, class_id in zip(detections.confidence, detections.class_id)
    ]

    # Annotate the frame with bounding boxes
    annotated_frame = box_annotator.annotate(
        scene=frame,
        detections=detections
    )

    # Draw the labels separately
    for i, box in enumerate(detections.xyxy):
        x1, y1, x2, y2 = map(int, box)
        label = labels[i]
        # Draw text background
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(annotated_frame, (x1, y1 - 20), (x1 + w, y1), (0, 255, 0), -1)
        # Draw text
        cv2.putText(annotated_frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    return annotated_frame

def main():
    cap = initialize_camera(video_path)
    model = load_yolov8_model()
    box_annotator = sv.BoundingBoxAnnotator(
        thickness=2
    )

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        annotated_frame = process_frame(frame, model, box_annotator)

        # Write the frame to the output video
        out.write(annotated_frame)

        cv2.imshow("yolov8", annotated_frame)

        if cv2.waitKey(20) == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
