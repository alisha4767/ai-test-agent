# AI Test Agent – Founding Engineer Assignment

## 🚀 Overview
This project converts natural language test descriptions into structured test steps and executes them in a real browser.

The agent:
1. Parses user input
2. Generates test steps (Action + Assertion objects)
3. Executes them in a browser using Playwright
4. Validates success/failure based on assertions

---

## 🧠 Architecture

### 🔹 1. Input Processing
- Extracts URL, email, and password using regex
- No hardcoding of specific websites

### 🔹 2. Test Step Generation
- Converts natural language into structured steps:
  - `open`
  - `type`
  - `click`
  - `assertion`

### 🔹 3. Execution Layer
- Uses Playwright to control a real browser
- Performs actions sequentially
- Stops execution on failure

### 🔹 4. Validation
- Assertions verify expected outcomes
- If any step fails → test fails

---

## 📥 Input Example
Go to linkedin.com login with email test@gmail.com
 and password 123456 and verify invalid credentials

 
---

## 📤 Output (Generated Steps)

```json
[
  { "action": "open", "url": "https://linkedin.com" },
  { "action": "type", "target": "input[type='email']", "value": "test@gmail.com" },
  { "action": "type", "target": "input[type='password']", "value": "123456" },
  { "action": "click", "target": "button[type='submit']" },
  { "action": "assertion", "target": "body", "contains": "invalid" }
]

Execution Flow
Run the script
Enter test description
Agent generates steps
Browser opens automatically
Actions are executed
Result is displayed:
✅ Test Passed
or
❌ Test Failed

How to Run
python main.py

Features
Natural language → structured test steps
Dynamic data extraction (URL, credentials)
Generic (no hardcoded website logic)
Real browser execution using Playwright
Assertion-based validation
Reasoning layer (prints extracted data)

Limitations
Uses generic selectors (may fail on some websites)
No Chrome Extension integration (simulated via Playwright)
LLM not used (rule-based logic instead)

Future Improvements
Integrate LLM for smarter step generation
Add Chrome Extension for screenshot + HTML capture
Improve selector detection using DOM parsing
Support more complex test scenarios
Add retry and self-healing logic

Architecture Alignment with Assignment
Backend logic implemented in Python
Browser actions executed via Playwright
Failure handling implemented
Designed to integrate with:
Chrome Extension (future)
LLM backend (future)

Note

Playwright browser binaries could not be installed due to system security restrictions (Device Guard).

Used existing Chrome browser via:

channel="chrome"