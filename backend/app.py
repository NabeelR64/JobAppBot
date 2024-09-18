from flask import Flask, request, jsonify
from resume_parser import parse_resume
from job_role_suggestor import suggest_job_roles

app = Flask(__name__)

# File upload endpoint
@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_type = file.filename.split('.')[-1]

    if file_type not in ['pdf', 'docx']:
        return jsonify({'error': 'Unsupported file format'}), 400

    # Parse resume
    resume_text = parse_resume(file, file_type)

    # Suggest job roles based on parsed resume using OpenAI
    suggested_roles = suggest_job_roles(resume_text)

    return jsonify({
        'resume_text': resume_text,
        'suggested_roles': suggested_roles
    })

if __name__ == '__main__':
    app.run(debug=True)
