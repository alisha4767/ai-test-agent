# AI Test Agent – Founding Engineer Assignment

## 🚀 Overview
This project converts natural language test descriptions into structured test steps (Action + Assertion objects).

### Example

**Input:**
Go to linkedin.com, login with email and password, verify error message


**Output:**
- Open website  
- Enter credentials  
- Click login  
- Verify error message  

---

## 🧠 Approach

### 1. Smart Logic Layer (No API required)
- Detects website (LinkedIn)
- Extracts email & password using regex
- Generates dynamic steps

### 2. Extensible Design
- LLM-ready architecture (can plug API anytime)
- Clean separation of logic

---

## 📥 Input Example
Go to linkedin.com, login with email txe@gmail.com
 and password 1h21j21j and verify invalid credentials message
 
---

## 📤 Output Example

```json
[
  { "action": "open", "url": "https://www.linkedin.com" },
  { "action": "type", "target": "//*[@id='username']", "value": "txe@gmail.com" },
  { "action": "type", "target": "//*[@id='password']", "value": "1h21j21j" },
  { "action": "click", "target": "//button[@type='submit']" },
  { "action": "assertion", "target": "//*[@id='error-for-password']", "contains": "invalid credentials" }
]
How to Run
python main.py

Features
Natural language → structured test steps
Dynamic credential extraction
Website detection
Reasoning layer (prints agent understanding)

Limitations
LLM integration not active (requires API billing)
Currently supports LinkedIn only
Selectors are predefined

Future Improvements
Add LLM integration
Support multiple websites
Add browser automation using Playwright
Use HTML parsing for dynamic selectors
