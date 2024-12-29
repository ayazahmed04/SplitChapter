from flask import Flask, render_template, request, send_file
import os
import pdfplumber

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

# Create the uploads directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def extract_chapters(pdf_path):
    chapters = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            # Simple heuristic to find chapters: Adjust this logic as needed
            if text and text.strip().startswith("Chapter"):
                chapters.append(text.strip())
    return chapters

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files.get("file")
        if uploaded_file and uploaded_file.filename.endswith(".pdf"):
            # Save file temporarily
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)

            # Extract chapters
            chapters = extract_chapters(filepath)

            # Clean up
            os.remove(filepath)
            return render_template("index.html", chapters=chapters)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
