from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
# Restrict CORS to specific production origin
CORS(app, resources={r"/api/*": {"origins": ["https://gcp-tech-conf-bakadja-v1.netlify.app"]}})

# Dummy Data for Google Cloud Technologies Conference
schedule_data = {
    "date": "October 24, 2026",
    "location": "Google Cloud Space, San Francisco",
    "title": "Google Cloud Tech Immersion Day",
    "events": [
        {
            "id": 1,
            "title": "Keynote: The Future of GCP",
            "time": "09:00 AM - 10:00 AM",
            "category": "Keynote",
            "description": "An overview of what's coming next for Google Cloud Platform including AI and Serverless.",
            "speakers": [
                {"firstName": "Sundar", "lastName": "Pichai", "linkedin": "https://linkedin.com/in/sundarpichai"}
            ],
            "type": "talk"
        },
        {
            "id": 2,
            "title": "Serverless Architectures with Cloud Run",
            "time": "10:15 AM - 11:15 AM",
            "category": "Serverless",
            "description": "Deep dive into building scalable applications with Google Cloud Run and Eventarc.",
            "speakers": [
                {"firstName": "Kelsey", "lastName": "Hightower", "linkedin": "https://linkedin.com/in/kelseyhightower"},
                {"firstName": "Steren", "lastName": "Giannini", "linkedin": "https://linkedin.com/in/steren"}
            ],
            "type": "talk"
        },
        {
            "id": 3,
            "title": "Generative AI with Vertex AI",
            "time": "11:30 AM - 12:30 PM",
            "category": "AI / ML",
            "description": "How to leverage Gemini models and Vertex AI to build enterprise-grade intelligence.",
            "speakers": [
                {"firstName": "Jeff", "lastName": "Dean", "linkedin": "https://linkedin.com/in/jeffdean"}
            ],
            "type": "talk"
        },
        {
            "id": "lunch",
            "title": "Lunch Break & Networking",
            "time": "12:30 PM - 01:30 PM",
            "category": "Break",
            "description": "Enjoy a 60-minute catered lunch and network with Google Cloud experts.",
            "speakers": [],
            "type": "break"
        },
        {
            "id": 4,
            "title": "Kubernetes: Advanced GKE Configurations",
            "time": "01:30 PM - 02:30 PM",
            "category": "Infrastructure",
            "description": "Optimizing GKE clusters for performance, security, and cost efficiency.",
            "speakers": [
                {"firstName": "Tim", "lastName": "Hockin", "linkedin": "https://linkedin.com/in/thockin"}
            ],
            "type": "talk"
        },
        {
            "id": 5,
            "title": "Data Engineering with BigQuery and Dataflow",
            "time": "02:45 PM - 03:45 PM",
            "category": "Data",
            "description": "Building robust streaming and batch data pipelines on Google Cloud.",
            "speakers": [
                {"firstName": "Lak", "lastName": "Lakshmanan", "linkedin": "https://linkedin.com/in/lakshmanan"}
            ],
            "type": "talk"
        },
        {
            "id": 6,
            "title": "Securing Your Cloud Environment (BeyondCorp)",
            "time": "04:00 PM - 05:00 PM",
            "category": "Security",
            "description": "Implementing zero-trust security and BeyondCorp Enterprise on GCP.",
            "speakers": [
                {"firstName": "Heather", "lastName": "Adkins", "linkedin": "https://linkedin.com/in/heatheradkins"}
            ],
            "type": "talk"
        },
        {
            "id": 7,
            "title": "Modern App Dev with Firebase & Flutter",
            "time": "05:15 PM - 06:15 PM",
            "category": "Mobile & Web",
            "description": "Cross-platform development strategies using the latest Firebase extensions.",
            "speakers": [
                {"firstName": "Todd", "lastName": "Kerpelman", "linkedin": "https://linkedin.com/in/toddkerpelman"}
            ],
            "type": "talk"
        },
        {
            "id": 8,
            "title": "Closing Panel & Happy Hour",
            "time": "06:30 PM - 07:30 PM",
            "category": "Networking",
            "description": "A panel discussion with today's speakers followed by drinks and appetizers.",
            "speakers": [
                {"firstName": "Thomas", "lastName": "Kurian", "linkedin": "https://linkedin.com/in/thomaskurian"}
            ],
            "type": "talk"
        }
    ]
}

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    return jsonify(schedule_data)

if __name__ == '__main__':
    # Debug mode disabled for production
    app.run(debug=False, port=5000)
