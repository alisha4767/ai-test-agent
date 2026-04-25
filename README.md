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

---

---

## 🚀 Features

- Natural language → structured test steps  
- Dynamic data extraction (URL, credentials)  
- Generic (no hardcoded website logic)  
- Real browser execution using Playwright  
- Assertion-based validation  
- Reasoning layer (prints extracted data)  

---

## ⚠️ Limitations

- Uses generic selectors (may fail on some websites)  
- No Chrome Extension integration (simulated via Playwright)  
- LLM not used (rule-based logic instead)  

---

