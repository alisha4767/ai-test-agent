import re

def extract_url(text):
    match = re.search(r'(https?://[^\s]+|[\w]+\.[\w]+)', text)
    if match:
        url = match.group(0)
        if not url.startswith("http"):
            url = "https://" + url
        return url
    return "https://example.com"


def extract_credentials(text):
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    password_match = re.search(r'password\s+(\S+)', text, re.IGNORECASE)

    email = email_match.group(0) if email_match else "test@example.com"
    password = password_match.group(1) if password_match else "password123"

    return email, password


def generate_steps(description):
    url = extract_url(description)
    email, password = extract_credentials(description)

    # ✅ Reasoning layer
    print("\n--- Agent Reasoning ---")
    print("URL:", url)
    print("Email:", email)
    print("Password:", password)
    print("----------------------\n")

    return [
        { "action": "open", "url": url },
        { "action": "type", "target": "input[type='email'], input[name='session_key']", "value": email },
        { "action": "type", "target": "input[type='password']", "value": password },
        { "action": "click", "target": "button[type='submit']" },
        { "action": "assertion", "target": "body", "contains": "invalid" }
    ]