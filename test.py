import torch
from PIL import Image
import timm
import torchvision.transforms as transforms

# Create a text file named 'imagenet_classes.txt' with a single class "manhole"
with open('imagenet_classes.txt', 'w') as f:
    f.write('manhole\n')

# Load and preprocess the image
def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)  # Add batch dimension
    return input_batch

# Load the pretrained model
def load_pretrained_model(model_name):
    model = timm.create_model(model_name, pretrained=True, num_classes=1)
    model.eval()  # Set the model to evaluation mode
    return model

# Perform inference
def predict(model, input_tensor):
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.sigmoid(output).squeeze(0).item()
        predicted_class = 0 if probabilities >= 0.5 else 1  # Binary classification threshold
    return predicted_class, probabilities

# Load class labels
with open('imagenet_classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]

# Display the prediction
def display_prediction(predicted_class, probabilities):
    if predicted_class == 0:
        label = labels[0]
        confidence = probabilities
        print(f'Predicted class: {label}, Confidence: {confidence:.2f}')
    else:
        print('Predicted class: Not manhole')

# Paths
image_path = '/Users/anirudhchilukuri/Desktop/VIproj/R-2-_jpg.rf.74d32a3cc31762686a39933d9e1b40a7.jpg'
print(image_path)

# Preprocess image
input_tensor = preprocess_image(image_path)

# Load pretrained model
model_name = 'resnet50'
model = load_pretrained_model(model_name)

# Perform inference
predicted_class, probabilities = predict(model, input_tensor)

# Display prediction
display_prediction(predicted_class, probabilities)
