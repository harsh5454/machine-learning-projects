import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def load_image(image_path, max_dim=512):
    """Loads an image and limits its maximum dimension to 512 pixels."""
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img

def display_image(image, title=''):
    """Displays an image."""
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

def save_image(image, filename="stylized_image.jpg"):
    """Saves the generated image to a file."""
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)

    # Convert to a format that can be saved by OpenCV
    image = cv2.cvtColor(np.array(image) * 255, cv2.COLOR_RGB2BGR)
    cv2.imwrite(filename, image)
    print(f"Image saved to {filename}")


if __name__ == '__main__':
    # --- Configuration ---
    CONTENT_IMAGE_DIR = 'content_images'
    STYLE_IMAGE_DIR = 'style_images'
    OUTPUT_DIR = 'output_images'

    # Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created output directory: {OUTPUT_DIR}")

    # Check if directories exist
    if not os.path.exists(CONTENT_IMAGE_DIR):
        print(f"Error: Directory '{CONTENT_IMAGE_DIR}' does not exist.")
        exit()
    
    if not os.path.exists(STYLE_IMAGE_DIR):
        print(f"Error: Directory '{STYLE_IMAGE_DIR}' does not exist.")
        exit()

    # Get the first image from each directory
    try:
        content_image_name = os.listdir(CONTENT_IMAGE_DIR)[0]
        style_image_name = os.listdir(STYLE_IMAGE_DIR)[0]
    except IndexError:
        print("Error: Please make sure you have placed an image in both the 'content_images' and 'style_images' folders.")
        exit()

    content_path = os.path.join(CONTENT_IMAGE_DIR, content_image_name)
    style_path = os.path.join(STYLE_IMAGE_DIR, style_image_name)
    output_path = os.path.join(OUTPUT_DIR, f"stylized_{os.path.splitext(content_image_name)[0]}_{os.path.splitext(style_image_name)[0]}.jpg")

    # Check if image files exist
    if not os.path.exists(content_path):
        print(f"Error: Content image not found at {content_path}")
        exit()
    
    if not os.path.exists(style_path):
        print(f"Error: Style image not found at {style_path}")
        exit()

    # --- Load Images ---
    print("Loading images...")
    try:
        content_image = load_image(content_path)
        style_image = load_image(style_path)
        print("Images loaded successfully!")
    except Exception as e:
        print(f"Error loading images: {e}")
        exit()

    # --- Load Pre-trained Model from TensorFlow Hub ---
    print("Loading Neural Style Transfer model...")
    try:
        hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        print("This might be due to network issues or an outdated model URL.")
        exit()

    # --- Apply Style Transfer ---
    print("Applying style... This may take a moment.")
    try:
        stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
        print("Style transfer completed successfully!")
    except Exception as e:
        print(f"Error during style transfer: {e}")
        exit()

    # --- Display and Save Results ---
    print("Style transfer complete!")

    # Display the images
    try:
        plt.figure(figsize=(15, 5))

        plt.subplot(1, 3, 1)
        display_image(content_image, 'Content Image')

        plt.subplot(1, 3, 2)
        display_image(style_image, 'Style Image')

        plt.subplot(1, 3, 3)
        display_image(stylized_image, 'Stylized Image')

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error displaying images: {e}")

    # Save the final image
    try:
        save_image(stylized_image, output_path)
    except Exception as e:
        print(f"Error saving image: {e}")