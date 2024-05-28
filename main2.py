from ultralytics import YOLO
import cv2
import math

# Load model
model = YOLO("/Users/anirudhchilukuri/Desktop/VIproj/best4.pt")

# Object classes
classNames = [ "manhole", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
              "traffic light", "bench", "bird", "cat",
              "dog", "cow", "backpack", "umbrella",
              "ball", "skateboard", "chair", "sofa", "pottedplant", "bed",
              "table", "toilet", "tv", "cell phone",
              "sink", "refrigerator", "book", "vase","person"
              ]

def process_image(image_path):
    # Load image
    img = cv2.imread(image_path)

    # Check if the image was successfully read and has valid dimensions
    if img is None or img.size == 0:
        print("Failed to load image or image is empty")
        return

    results = model(img, stream=True)
    counts = {class_name: 0 for class_name in classNames}

    l = {class_name: 0 for class_name in classNames}

    # Coordinates
    for r in results:
        boxes = r.boxes
        keys_to_remove = []

        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to int values

            # Put box in image
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # Class name
            cls = int(box.cls[0])
            if 0 <= cls < len(classNames):  # Check if cls is within the range of classNames
                print("Class name -->", classNames[cls])
                class_name = classNames[cls]
                counts[class_name] += 1

                for class_name, count in counts.items():
                    l[class_name] = count

                for key, val in l.items():
                    if val == 0:
                        keys_to_remove.append(key)
                for key in keys_to_remove:
                    if key in l:
                        del l[key]
                print("Here -->", l)

                # Object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
            else:
                print("Class index out of range:", cls)

    # Check if the image has valid dimensions before displaying
    if img.shape[0] > 0 and img.shape[1] > 0:
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage
image_path = "/Users/anirudhchilukuri/Desktop/VIproj/Dataset/manhole/images.jpeg"  # Replace with your image path
process_image(image_path)
