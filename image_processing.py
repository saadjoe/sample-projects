from typing import Any

from PIL import Image
from torch import Tensor, no_grad
from torchvision import transforms
from torchvision.models.resnet import ResNet


def predict_image(image_path: str, model: ResNet, class_names: list) -> str:
    # Load the image
    image_obj: Image.Image = Image.open(image_path)

    # Preprocess the image
    preprocess: Any = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image_pre: Tensor = preprocess(image_obj)

    # Prepare the model for inference
    model.eval()

    # Perform inference
    with no_grad():
        image: Tensor = image_pre.unsqueeze(0)  # Add a batch dimension
        outputs: Tensor = model(image)

    # Find the index of the maximum value along the appropriate dimension
    max_index: Tensor = outputs.argmax(dim=1)

    # Convert the predicted class index to class name
    predicted_class: str = class_names[int(max_index.item())]

    return predicted_class
