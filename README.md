# PDF Password Protection Using Python
This project demonstrates how to add password protection to a PDF file programmatically using Python. It uses the `PyPDF2` library to read, encrypt, and save PDF files securely with a password.

---

## Features

- Open and read an existing PDF file
- Encrypt the PDF with a user-defined password
- Save the encrypted PDF as a new file
- Simple and efficient Python script

---

## Installation

Make sure you have Python installed (version 3.6 or above recommended).

Install the required library `PyPDF2` using pip:

```bash
pip install PyPDF2

Usage

Place the PDF file you want to encrypt in your project directory (or provide the full path).

Open the Python script and update the following variables if needed:

file_pdf = PdfReader('imp_pdf.pdf') — change 'imp_pdf.pdf' to your PDF filename.

password = "Aditya@1234" — change the password to your preferred one.

Run the script. It will generate a new PDF file named encryptedtickets.pdf that is password protected.

How It Works

The script reads the original PDF file using PdfReader.

It iterates through all pages and adds them to a new PdfWriter object.

Then it encrypts the new PDF with the provided password.

Finally, it writes the encrypted PDF to disk.

Output
After running the script, you will get a new file named encryptedtickets.pdf. This file requires the password to be opened, ensuring your PDF content is secure.

Author
Aditya Barhate
Email: adityabarhate18@gmail.com
GitHub: adiiiii19
