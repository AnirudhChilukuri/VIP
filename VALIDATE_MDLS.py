import torch
from ultralytics import YOLOv10
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
import numpy as np

# Define the transformation to apply to each image
transform = transforms.Compose([
    transforms.Resize((640, 640)),  # Resize the image to the required input size of the YOLO model
    transforms.ToTensor(),           # Convert the image to a PyTorch tensor
])

# Load the test dataset
test_dataset = ImageFolder(root='/Users/anirudhchilukuri/Desktop/VIproj/Dataset', transform=transform)

# Create a DataLoader for the test dataset
batch_size = 32
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# Load the trained YOLO model
model = YOLOv10('/Users/anirudhchilukuri/Desktop/VIproj/best7.pt')

# Iterate through the test dataset and compute accuracy
correct = 0
total = 0

# Define a confidence threshold for making predictions
confidence_threshold = 0.5

for images, labels in test_loader:
    results = model(images)  # Run inference
    
    # Process each image in the batch
    for i, (image, label) in enumerate(zip(images, labels)):
        predictions = results[i].boxes  # Get the predictions for the current image
        
        if predictions is not None and len(predictions) > 0:
            # Check each prediction
            for pred in predictions:
                if pred.conf > confidence_threshold:  # Apply confidence threshold
                    predicted_label = int(pred.cls)  # Assuming the label is stored in `cls`
                    correct += (predicted_label == label.item())
            total += 1

accuracy = 100 * correct / total if total > 0 else 0
print("Accuracy:", accuracy)
