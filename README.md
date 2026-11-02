# AI Security Policy Generator for a Small Organisation

A beginner-friendly Flask web application that creates a customised information security policy using organisation details and selected security practices.

## Features
- Collects basic organisation information.
- Customises policy sections for access control, email safety, devices, remote work, backups, training, and incident response.
- Displays the generated policy in the browser.
- Downloads the policy as a `.txt` file.
- Responsive HTML and CSS interface.

## Technology stack
- Python
- Flask
- HTML5
- CSS3

## Project structure
```text
ai-security-policy-generator/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run locally

1. Install Python 3.10 or newer.
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-security-policy-generator.git
   cd ai-security-policy-generator
   ```
3. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   ```
   Windows:
   ```bash
   .venv\\Scripts\\activate
   ```
   macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the application:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.

## How it works
The current version uses a rule-based policy generator. It adapts prewritten security guidance to the answers entered by the user. It does not call an external AI model or require an API key. An LLM integration can be added in a future version.

## Important disclaimer
This project creates an educational starter template. It is not a guarantee of security, legal compliance, or certification. An organisation should review the generated policy with management and a qualified security professional and adapt it to its risks and applicable laws.

## Future improvements
- Add PDF export.
- Add user login and saved policies.
- Add policy templates for different industries.
- Integrate a language model through a securely stored API key.
- Add admin approval and policy version history.
