import flet as ft
import requests
from torchvision.models import ResNet50_Weights, resnet50

from image_processing import predict_image


def main(page: ft.Page):
    # Configure the page
    page.title = "Image Recognition"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Load the ResNet-50 model
    model = resnet50(weights=ResNet50_Weights.DEFAULT)
    
    # Download class labels
    label_url = 'https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json'
    response = requests.get(label_url)
    class_names = response.json()
    
    def pick_image_result(e: ft.FilePickerResultEvent) -> None:
        if e.files:
            # Display the progress bar
            page.splash = ft.ProgressBar()
            pick_image_btn.disabled = True
            page.update()

            # Show the image
            img = ft.Image(
                src=e.files[0].path,
                fit=ft.ImageFit.CONTAIN,
                height=500,
            )
            main_col.controls.clear()
            main_col.controls.append(img)
            page.update()

            # Predict the image and display the result
            result = predict_image(image_path=e.files[0].path, model=model, class_names=class_names)
            main_col.controls.append(ft.Text(result, size=26))
            page.splash = None
            pick_image_btn.disabled = False
            page.update()

    # Add file picker option
    file_picker = ft.FilePicker(on_result=pick_image_result)
    page.overlay.append(file_picker)

    main_col = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[]
    )

    pick_image_btn = ft.ElevatedButton(
        text="Pick Image",
        on_click=lambda _: file_picker.pick_files(file_type=ft.FilePickerFileType.IMAGE),
    )

    # Add elements to the page
    page.add(
        ft.Container(
            pick_image_btn,
        ),
        main_col
    )
