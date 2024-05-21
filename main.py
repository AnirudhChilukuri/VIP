from ultralytics import YOLO
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

# model
model = YOLO("yolo-Weights/yolov8n.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
              "traffic light", "bench", "bird", "cat",
              "dog", "cow", "backpack", "umbrella",
                "ball", "skateboard", "chair", "sofa", "pottedplant", "bed",
              "table", "toilet", "tv", "cell phone",
               "sink", "refrigerator", "book", "vase"
              ]
l = {class_name: 0 for class_name in classNames}

while True:
    success, img = cap.read()
    
    # Check if the image was successfully read and has valid dimensions
    if not success or img.size == 0:
        continue
    
    results = model(img, stream=True)
    counts = {class_name: 0 for class_name in classNames}



    # coordinates
    for r in results:
        boxes = r.boxes
        keys_to_remove = []
        labels_dict = {}
        count = 0
        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->", confidence)

            # class name
            cls = int(box.cls[0])
            if 0 <= cls < len(classNames):  # Check if cls is within the range of classNames
                print("Class name -->", classNames[cls])
                class_name = classNames[cls]
                counts[class_name] += 1

                for class_name, count in counts.items():
                    l[class_name] = count

                # for class_name, count in l.items():
                #     print(f"{class_name}:{count}", "---------")
                for key, val in l.items():
                    if val == 0:
                        keys_to_remove.append(key)
                for key in keys_to_remove:
                    if key in l:
                        del l[key]
                print("here -->",l)
                    #lvalue = l.values()
                    # for j in lvalue:
                    #     if j <= 0:
                    #         l.pop(str(class_name))
                    # for i in range(0, len(l.values())):
                    #     lii = list(l.items())
                    #     Lii = lii
                    #     li.append(l.values())
                    #     #print(type(li))
                    # print(Lii)
                    # for j in Lii:
                    #     print(j[1])
                    #     if j[1] == 0:
                    #         Lii.remove(j)   
                    
                # object details
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
        cv2.imshow('Webcam', img)
    
    if cv2.waitKey(1) == ord('q'):
        break
