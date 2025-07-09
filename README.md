# ReconTool

Python tool for offensive reconnaissance: WHOIS, DNS resolution, port scanning, and banner grabbing.

---

## Features

- WHOIS domain lookup
- Domain to IP resolution
- Common ports scanning
- Banner grabbing from services on open ports

---

## Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`

---

## How to Run
1. Clone the repository
```bash
git clone https://github.com/AlexCarrascoLlorca/ReconTool.git
cd ReconTool
```

2. (Optional but recommended) Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required libraries:
```bash
pip install -r requirements.txt
```

4. (Optional) Exit the virtual environment
```bash
deactivate
```

5. Run the tool:
```bash
python main.py
```

---

## Technologies

- Python 3.x  
- Libraries:  
  - `whois`  
  - `socket`  
  - `concurrent.futures`  

---

## Legal Disclaimer

This tool is intended for educational and authorized testing purposes only.
Do not use it against systems you do not own or lack explicit permission to test.
Unauthorized use is illegal.

---

## Author

[Alex Carrasco] - [GitHub](https://github.com/AlexCarrascoLlorca)