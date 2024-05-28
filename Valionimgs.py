from ultralytics import YOLO

# Load a pretrained YOLOv10n model
model = YOLO("/Users/anirudhchilukuri/Desktop/VIproj/best6.pt")

# Perform object detection on an image
results = model("/Users/anirudhchilukuri/Desktop/VIproj/Dataset/manhole/0x0.jpg.webp")

# Display the results
results[0].show()