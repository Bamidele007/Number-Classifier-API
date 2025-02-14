```markdown
# Number Classification API

A robust REST API that analyzes numbers and provides mathematical insights about them, including properties like Armstrong numbers, primality, perfect numbers, and interesting mathematical facts.

## Key Features

- Comprehensive number analysis including:
  - Armstrong number detection (e.g., 371 = 3³ + 7³ + 1³)
  - Prime number verification
  - Perfect number identification
  - Digit sum calculation
  - Odd/Even classification
- Integration with Numbers API for mathematical fun facts
- RESTful API with JSON responses
- Error handling for invalid inputs
- CORS support for cross-origin requests
- AWS Elastic Beanstalk deployment
- Input validation and sanitization

## Technology Stack

- **Backend:**
  - Python 3.8+
  - Flask 2.0.1
  - Flask-CORS
  - Gunicorn
- **External Services:**
  - Numbers API for mathematical facts
- **Deployment:**
  - AWS Elastic Beanstalk
  - Nginx
- **Development Tools:**
  - Git
  - pip

## Project Structure

```
number-classifier/
├── application.py          # Main Flask application
├── utils/
│   ├── __init__.py
│   └── number_utils.py     # Number analysis utilities
├── .ebextensions/
│   └── 01_flask.config    # AWS EB configuration
├── requirements.txt       # Python dependencies
└── Procfile              # Process file for deployment
```

## API Specification

### Endpoint: `GET /api/classify-number?number=<integer>`

#### Success Response (200 OK):
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}
```

#### Error Response (400 Bad Request):
```json
{
    "number": "invalid_input",
    "error": true
}
```

## Installation & Local Setup

1. Clone the repository:
```bash
git clone https://github.com/Bamidele007/Number-Classification-API.git
cd Number-Classification-API
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python application.py
```

## Deployment

1. Install AWS EB CLI:
```bash
pip install awsebcli
```

2. Initialize EB application:
```bash
eb init -p python-3.8 number-classifier
```

3. Create environment and deploy:
```bash
eb create number-classifier-env
eb deploy
```

## Testing

Test the API endpoint:
```bash
curl "http://your-eb-url/api/classify-number?number=371"
```

## Implementation Details

- Handles positive and negative integers
- Converts decimal inputs to integers
- Validates input to prevent injection and errors
- Implements efficient algorithms for number property calculations
- Uses caching for frequent requests
- Provides detailed error messages for debugging

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Numbers API for mathematical facts
- AWS for hosting infrastructure
- Flask community for the excellent web framework
```