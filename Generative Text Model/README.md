# Text Generator

This project is a simple text generation tool using the Hugging Face Transformers library and a pre-trained GPT-2 model. It allows you to generate creative text based on a prompt you provide.

## Features
- Generates text using GPT-2
- Simple command-line interface
- Reproducible results with a fixed random seed

## Requirements
- Python 3.6 or higher
- [transformers](https://pypi.org/project/transformers/)

## Installation
1. Clone this repository or download the `text_generator.py` file.
2. Install the required Python package:
   ```bash
   pip install transformers
   ```

## Usage
Run the script from the command line:

```bash
python text_generator.py
```

You will be prompted to enter a sentence to start the story. The script will then generate and display a continuation of your prompt using GPT-2.

## Example
```
Enter a sentence to start the story: Once upon a time in a distant galaxy,
Loading model... (This might take a moment on the first run)

Generating text based on your prompt: 'Once upon a time in a distant galaxy,'
---
Once upon a time in a distant galaxy, ...
```

## Notes
- The first time you run the script, the GPT-2 model will be downloaded automatically.
- If you do not enter a prompt, the script will exit with a message.

## License
This project is for educational purposes and uses the open-source GPT-2 model from Hugging Face. 