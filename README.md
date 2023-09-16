# Image Recognition Project

This is a simple image recognition project that utilizes a pre-trained ResNet-50 model to classify images and display the predicted class. It's powered by [Flet](https://github.com/fletorg/flet) for the user interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- Enables users to select an image for classification.
- Displays both the selected image and the predicted class.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/saadjoe/image-recognition.git
   cd image-recognition
   ```

2. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Launch the application:

   ```bash
   python main.py
   ```

2. Choose an image for prediction.

## Project Structure

- `main.py`: The primary script responsible for running the application.
- `image_processing.py`: Manages image processing and prediction.
- `ui.py`: Handles user interface design and page configuration.
- `requirements.txt`: Lists the required dependencies for the project.
- `README.md`: The current file, serving as project documentation.
- `LICENSE`: The license file (MIT License) specifying terms and conditions for using the code.

## License

This project is licensed under the MIT License - please refer to the [LICENSE](https://github.com/saadjoe/image-recognition/LICENSE) file for details.