from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfReader, PdfWriter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/protect', methods=['POST'])
def protect():
    file = request.files['pdfFile']
    password = request.form['password']

    if file and password:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Read and write PDF
        reader = PdfReader(filepath)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(password)

        protected_path = os.path.join(UPLOAD_FOLDER, 'protected_' + filename)
        with open(protected_path, 'wb') as f:
            writer.write(f)

        return send_file(protected_path, as_attachment=True)

    return "Missing file or password!"

if __name__ == '__main__':
    app.run(debug=True)
    
