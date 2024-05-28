from ultralytics import YOLOv10

model = YOLOv10()
model.train(data='',epochs=5,imgsz=640)