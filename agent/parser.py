import re

def extract_credentials(text):
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    password_match = re.search(r'password\s+(\S+)', text, re.IGNORECASE)
    

    
    email = email_match.group(0) if email_match else "test@example.com"
    password = password_match.group(1) if password_match else "password123"

    return email, password


def detect_website(text):
    text = text.lower()

    if "linkedin" in text:
        return "linkedin"
    return "unknown"


def generate_steps(description):
    site = detect_website(description)
    email, password = extract_credentials(description)
  
    print("Detected website:", site)
    print("Extracted email:", email)
    print("Extracted password:", password)

    if site == "linkedin":
        return [
            { "action": "open", "url": "https://www.linkedin.com" },
            { "action": "type", "target": "//*[@id='username']", "value": email },
            { "action": "type", "target": "//*[@id='password']", "value": password },
            { "action": "click", "target": "//button[@type='submit']" },
            { "action": "assertion", "target": "//*[@id='error-for-password']", "contains": "invalid credentials" }
        ]

    return [
        { "action": "open", "url": "https://example.com" }
    ]