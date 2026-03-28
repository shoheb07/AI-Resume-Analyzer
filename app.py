import os
from flask import Flask, render_template, request
from utils.parser import extract_text
from utils.analyzer import match_keywords
from utils.scorer import calculate_score

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"]

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        resume_text = extract_text(file_path)

        matched, missing = match_keywords(resume_text, job_desc)
        score = calculate_score(matched, len(missing) + len(matched))

        result = {
            "score": score,
            "matched": list(matched)[:20],
            "missing": list(missing)[:20]
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
