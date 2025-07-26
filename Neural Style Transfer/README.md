# Neural Style Transfer

This project applies neural style transfer to blend the artistic style of one image with the content of another using TensorFlow and a pre-trained model from TensorFlow Hub.

## Features
- Uses TensorFlow and TensorFlow Hub's pre-trained arbitrary image stylization model
- Simple interface: just place your content and style images in the respective folders
- Automatically saves the stylized output image
- Robust error handling and informative messages

## Project Structure
```
Task3/
├── content_images/        # Place your content images here
│   └── content_image.jpg
├── style_images/          # Place your style images here
│   └── style_image.jpg
├── output_images/         # Stylized images will be saved here
├── neural_style_transfer.py
├── requirements.txt
└── README.md
```

## Setup
1. **Clone or download this repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your images:**
   - Place a content image in the `content_images` folder
   - Place a style image in the `style_images` folder

## Usage
Run the script:
```bash
python neural_style_transfer.py
```

- The script will automatically use the first image it finds in each folder.
- The stylized image will be saved in the `output_images` directory with a descriptive filename.

## Notes
- The script uses the [Magenta Arbitrary Image Stylization model](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2) from TensorFlow Hub.
- Make sure you have a stable internet connection the first time you run the script (to download the model).
- If you want to use different images, just replace the files in the `content_images` and `style_images` folders.

## Troubleshooting
- If you encounter errors about missing directories or files, ensure the folder structure matches the one above and that you have at least one image in each of the `content_images` and `style_images` folders.
- For any other issues, check the error messages printed by the script for guidance.

## License
This project is for educational and research purposes. 