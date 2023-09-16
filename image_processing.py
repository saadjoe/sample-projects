import torch
from torchvision.models import resnet50, ResNet50_Weights
from torchvision import transforms
from PIL import Image
import requests

def predict_image(image_path: str) -> str:
    # Load the ResNet-50 model
    model = resnet50(weights=ResNet50_Weights.DEFAULT)

    # Load the image
    image = Image.open(image_path)

    # Preprocess the image
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = preprocess(image)

    # Prepare the model for inference
    model.eval()

    # Perform inference
    with torch.no_grad():
        image = image.unsqueeze(0)  # Add a batch dimension
        outputs = model(image)

    # Download class labels
    label_url = 'https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json'
    response = requests.get(label_url)
    class_names = response.json()

    # Convert the predicted class index to class name
    predicted_class = class_names[outputs.argmax().item()]

    return predicted_class
