# Import the necessary components from the transformers library
from transformers import pipeline, set_seed

def generate_text(prompt, max_len=150):
    """
    Generates text using a pre-trained GPT-2 model.

    Args:
        prompt (str): The initial text to start the generation from.
        max_len (int): The maximum length of the generated text.

    Returns:
        str: The generated text.
    """
    # Create a text generation pipeline using the GPT-2 model
    # This will download the model the first time it's run
    print("Loading model... (This might take a moment on the first run)")
    generator = pipeline('text-generation', model='gpt2')

    # Set a seed for reproducibility, so you get the same result for the same prompt
    set_seed(42)

    print(f"\nGenerating text based on your prompt: '{prompt}'")
    print("---")

    # Generate the text
    # The pipeline handles tokenization, model inference, and decoding
    results = generator(prompt, max_length=max_len, num_return_sequences=1)

    return results[0]['text']


if __name__ == '__main__':
    # --- Get User Input ---
    # You can change this initial_prompt to anything you want
    initial_prompt = input("Enter a sentence to start the story: ")


    # --- Generate and Print the Text ---
    if initial_prompt:
        generated_story = generate_text(initial_prompt)
        print(generated_story)
    else:
        print("No prompt was entered. Please run the script again and provide a starting sentence.")

