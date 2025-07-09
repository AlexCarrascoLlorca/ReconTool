# ReconTool

Python tool for offensive reconnaissance: WHOIS, DNS resolution, port scanning, and banner grabbing.

---

## Usage

Run the main script with:

```bash
python main.py
```

Enter the target domain when prompted and wait for the results to be displayed.

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

Install them with:

```bash
pip install -r requirements.txt
```

## How to Run
1. Clone the repository
```bash
git clone https://github.com/AlexCarrascoLlorca/ReconTool.git
cd ReconTool
```

2. Install the required libraries:
```bash
pip install -r requirements.txt
```

3. Run the tool:
```bash
python main.py
```

4. Follow the menu prompts and enter a domain (e.g. example.com) to start scanning.

## Technologies

- Python 3.x  
- Libraries:  
  - `whois`  
  - `socket`  
  - `concurrent.futures`  

---

## Author

[Alex Carrasco] - [GitHub](https://github.com/AlexCarrascoLlorca)