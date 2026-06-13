# 🔐 Cipherer

Cipherer is a simple web application that encrypts and decrypts messages using a deterministic key-based substitution cipher.

Enter a key and a message, and Cipherer generates a unique secret alphabet based on that key. Using the same key allows the encrypted text to be decrypted back to its original form.

Huggingface Link: https://huggingface.co/spaces/kosmoscpp/cipherer

## Features

- 🔒 Encrypt messages with a custom key
- 🔓 Decrypt messages using the same key
- 🔑 Deterministic secret alphabet generation
- 🔄 Same key always produces the same cipher
- 📝 Preserves spaces, punctuation, numbers, and formatting
- 🔤 Supports uppercase and lowercase letters
- 🌐 Built with Gradio

## Example

Input

Key:

TOMATO

Message:

THE KING IS DEAD!

Output

(Random encrypted text)

Decrypting with the same key returns:

THE KING IS DEAD!

How It Works

Cipherer generates a shuffled alphabet from the provided key and uses it as a substitution table.

Example:

ABCDEFGHIJKLMNOPQRSTUVWXYZ
↓
QWERTYUIOPASDFGHJKLZXCVBNM

Each letter is replaced according to the generated secret alphabet. The same key always produces the same alphabet, allowing perfect decryption.

Installation

pip install -r requirements.txt
python app.py

Disclaimer

Cipherer is designed for learning, experimentation, and casual message encryption. It is not intended to provide modern cryptographic security for sensitive information.

License

MIT License
