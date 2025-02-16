from flask import Flask, request, jsonify, make_response
from resume_parser import parse_resume
from job_role_suggestor import suggest_job_roles
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# File upload endpoint
@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    try:
        print("file received")
        print(request.files)
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
    # response.headers.add("Access-Control-Allow-Origin", "*")
        print(jsonify({
            'suggested_roles': suggested_roles
        }))
        # resp = make_response({'suggested roles': suggested_roles})
        # resp.headers["Access-Control-Allow-Origin"] = "*"
        resp = {
            'suggested_roles': suggested_roles
        }
        return jsonify(resp), 200
    except Exception as e:
        print(f"and error occured {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/test', methods=['GET'])
def test_route():
    print("Test route was called")
    return "Flask is running!"

if __name__ == '__main__':
    app.run(debug=True, port=1992)
