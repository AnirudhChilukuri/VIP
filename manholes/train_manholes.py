from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("/Users/anirudhchilukuri/Desktop/VIproj/yolo-Weights/yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="data.yaml", epochs=100)  # train the model
metrics = model.val()
print(metrics)  # evaluate model performance on the validation set
path = model.export(format="onnx")  # export the model to ONNX format