import re
import os
import PyPDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import shutil

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

def mask_data(text):
    text = re.sub(r'\b[A-Z][a-z]*\s[A-Z][a-z]*\b', lambda x: f"User{get_random_bytes(2).hex()}", text)
    text = re.sub(r'\(\d{3}\)\s?\d{3}-\d{4}', lambda x: f"Phone{get_random_bytes(2).hex()}", text)
    text = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', lambda x: f"Email{get_random_bytes(2).hex()}@example.com", text)
    return text

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def write_file(output_path, data):
    with open(output_path, 'w') as file:
        file.write(data)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def remove_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"File '{file_path}' does not exist.")

def remove_input_folder(folder_path):
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' has been deleted.")

def process_pdf(input_pdf_path, output_path, key):
    text = pdf_to_text(input_pdf_path)
    input_file_path = 'input.txt'
    write_file(input_file_path, text)
    print(f"PDF content has been saved to {input_file_path}.")
    
    masked_text = mask_data(read_file(input_file_path))
    encrypted_data = encrypt_data(masked_text, key)
    
    write_file(output_path, encrypted_data)
    print(f"Masked and encrypted data has been saved to {output_path}")
    
    remove_file(input_file_path)
    remove_file(input_pdf_path)

if __name__ == "__main__":
    key = get_random_bytes(32)
    input_pdf_path = 'input/input.pdf'
    output_path = 'output/output.txt'

    if not os.path.exists('output'):
        os.makedirs('output')

    process_pdf(input_pdf_path, output_path, key)
