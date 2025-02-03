# PDF Encryption Tool

A secure PDF encryption tool utilizing the AES-256 encryption algorithm.

## Features
```
- Convert PDF to text
- Mask sensitive data (names, phone numbers, email addresses)
- Encrypt files using AES-256
- Automatically delete source files after processing
- Ensure compliance with data protection regulations
```
## Requirements
```
- Python 3.x
- Dependencies from `requirements.txt`
```
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PatrykIA/encryption_tool.git
   cd encryption_tool
Install the required dependencies:
pip install -r requirements.txt

Usage
```
Place your PDF file in the input/ directory.
Run the encryption script:
python encrypt.py
Encrypted files will be saved in the output/ directory.
Security Features
```
AES-256 encryption standard
Secure key management
Automatic deletion of source files
Data masking for sensitive information

Project Structure
```
pdf-encryption-tool/
├── README.md
├── requirements.txt
├── encrypt.py
├── input/
└── output/
```

Security Notice

This tool implements industry-standard encryption methods. However, ensure compliance with local data protection regulations when handling sensitive information.

Author

Patryk Rogowski / PatrykIA

Disclaimer

This tool is provided "as is" without any warranties. Use it at your own risk.
