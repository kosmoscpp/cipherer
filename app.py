import string
import random
import gradio as ui

def generate_secret_alphabet(key: str) -> str:
    """Generates a deterministic shuffled alphabet based on the provided key."""
    standard_alphabet = list(string.ascii_uppercase)
    # Using random.Random with a seed ensures determinism across runs
    seeded_random = random.Random(key)
    seeded_random.shuffle(standard_alphabet)
    return "".join(standard_alphabet)

def validate_inputs(key: str, text: str):
    """Validates that key and text are not empty or just whitespace."""
    if not key.strip():
        raise ui.Error("Key cannot be empty! Please enter a valid key.")
    if not text.strip():
        raise ui.Error("Text cannot be empty! Please enter some text.")

def encrypt_text(key: str, plain_text: str):
    validate_inputs(key, plain_text)
    
    secret_alphabet = generate_secret_alphabet(key)
    standard_alphabet = string.ascii_uppercase
    
    # Create mapping dictionaries for fast lookup
    upper_map = {src: dst for src, dst in zip(standard_alphabet, secret_alphabet)}
    lower_map = {src.lower(): dst.lower() for src, dst in zip(standard_alphabet, secret_alphabet)}
    
    encrypted_chars = []
    for char in plain_text:
        if char.isupper():
            encrypted_chars.append(upper_map.get(char, char))
        elif char.islower():
            encrypted_chars.append(lower_map.get(char, char))
        else:
            encrypted_chars.append(char)
            
    # Format alphabet display for the user
    alphabet_display = f"Standard: {standard_alphabet}\nSecret:   {secret_alphabet}"
    return "".join(encrypted_chars), alphabet_display

def decrypt_text(key: str, cipher_text: str):
    validate_inputs(key, cipher_text)
    
    secret_alphabet = generate_secret_alphabet(key)
    standard_alphabet = string.ascii_uppercase
    
    # Reverse mapping for decryption
    upper_map = {src: dst for src, dst in zip(secret_alphabet, standard_alphabet)}
    lower_map = {src.lower(): dst.lower() for src, dst in zip(secret_alphabet, standard_alphabet)}
    
    decrypted_chars = []
    for char in cipher_text:
        if char.isupper():
            decrypted_chars.append(upper_map.get(char, char))
        elif char.islower():
            decrypted_chars.append(lower_map.get(char, char))
        else:
            decrypted_chars.append(char)
            
    alphabet_display = f"Standard: {standard_alphabet}\nSecret:   {secret_alphabet}"
    return "".join(decrypted_chars), alphabet_display

# Build the Gradio Interface
with ui.Blocks(title="Cipherer") as demo:
    ui.Markdown("# 🔐 Cipherer")
    ui.Markdown(
        "Encrypt and decrypt text using a deterministic, key-based substitution cipher. "
        "The same key will always generate the exact same secret alphabet mapping."
    )
    
    with ui.Tabs():
        # --- ENCRYPT TAB ---
        with ui.TabItem("⚙️ Encrypt"):
            with ui.Row():
                with ui.Column():
                    encrypt_key = ui.Textbox(
                        label="Secret Key", 
                        placeholder="e.g., TOMATO", 
                        max_lines=1
                    )
                    plain_input = ui.Textbox(
                        label="Plain Text", 
                        placeholder="Enter text to encrypt here...", 
                        lines=5
                    )
                    encrypt_btn = ui.Button("Encrypt Text", variant="primary")
                
                with ui.Column():
                    encrypt_output = ui.Textbox(
                        label="Encrypted Output", 
                        interactive=False, 
                        lines=5
                    )
                    encrypt_mapping = ui.Textbox(
                        label="Generated Alphabet Mapping", 
                        interactive=False, 
                        lines=2
                    )
            
            encrypt_btn.click(
                fn=encrypt_text,
                inputs=[encrypt_key, plain_input],
                outputs=[encrypt_output, encrypt_mapping]
            )
            
        # --- DECRYPT TAB ---
        with ui.TabItem("🔓 Decrypt"):
            with ui.Row():
                with ui.Column():
                    decrypt_key = ui.Textbox(
                        label="Secret Key", 
                        placeholder="e.g., TOMATO", 
                        max_lines=1
                    )
                    cipher_input = ui.Textbox(
                        label="Cipher Text", 
                        placeholder="Enter text to decrypt here...", 
                        lines=5
                    )
                    decrypt_btn = ui.Button("Decrypt Text", variant="primary")
                
                with ui.Column():
                    decrypt_output = ui.Textbox(
                        label="Decrypted Output", 
                        interactive=False, 
                        lines=5
                    )
                    decrypt_mapping = ui.Textbox(
                        label="Generated Alphabet Mapping", 
                        interactive=False, 
                        lines=2
                    )
            
            decrypt_btn.click(
                fn=decrypt_text,
                inputs=[decrypt_key, cipher_input],
                outputs=[decrypt_output, decrypt_mapping]
            )
            
    # --- FOOTER CREDITS ---
    ui.HTML(
        """
        <div style="text-align: center; margin-top: 25px;">
            <a href="https://www.instagram.com/kosmos.cpp" target="_blank" style="text-decoration: none; color: #E1306C; font-weight: bold; font-size: 15px;">
                Follow Me ig@kosmos.cpp
            </a>
        </div>
        """
    )

if __name__ == "__main__":
    demo.launch(theme=ui.themes.Soft())
