# flask_app.py
import os
import json
from io import BytesIO
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from helper import configure_genai, get_gemini_response, extract_pdf_text, prepare_prompt

app = Flask(__name__, static_folder="static", template_folder="templates")

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("Please set GOOGLE_API_KEY in .env")

configure_genai(API_KEY)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        jd = request.form.get("jd", "").strip()
        uploaded_file = request.files.get("resume")

        if not jd:
            return jsonify({"success": False, "error": "Job description required."}), 400
        if uploaded_file is None or uploaded_file.filename == "":
            return jsonify({"success": False, "error": "Upload a PDF resume."}), 400

        file_stream = BytesIO(uploaded_file.read())
        resume_text = extract_pdf_text(file_stream)

        input_prompt = prepare_prompt(resume_text, jd)
        response_text = get_gemini_response(input_prompt)

        try:
            result_json = json.loads(response_text)
        except:
            import re
            match = re.search(r"{.*}", response_text, re.DOTALL)
            if match:
                result_json = json.loads(match.group())
            else:
                raise ValueError("AI response not JSON.")

        return jsonify({"success": True, "result": result_json})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501, debug=True)
