# Subdomain Finder using nslookup

This Python script discovers subdomains of a target domain using `nslookup`, saves the results to a JSON file, and parses the JSON logs for analysis.

---

## Features
- Discovers subdomains using `nslookup`.
- Reads potential subdomain names from a wordlist file.
- Saves the results to a JSON file with resolution status.
- Parses and displays the JSON logs.

---

## Prerequisites

### Requirements
- Python 3.x
- `nslookup` installed and available in your system's PATH.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/subdomain-finder.git
   cd subdomain-finder
   ```
2. Ensure you have a wordlist file ready (e.g., `wordlist.txt`) with potential subdomain names, one per line.

---

## Usage

### Command-Line Arguments
- `-target`: The target domain to search for subdomains (e.g., `example.com`).
- `-wordlist`: Path to the wordlist file containing potential subdomain names.
- `-output`: Path to save the JSON file with results.

### Example Command
```bash
python sub.py -target example.com -wordlist wordlist.txt -output results.json
```

### Sample Wordlist File
```txt
www
mail
ftp
api
dev
```

---

## Output

### JSON File Structure
The results are saved in a JSON file with the following structure:
```json
[
    {"subdomain": "www.example.com", "status": "resolved"},
    {"subdomain": "mail.example.com", "status": "resolved"},
    {"subdomain": "dev.example.com", "status": "unresolved"}
]
```

### Terminal Output
```bash
Searching for subdomains of example.com using nslookup...

Found: www.example.com
Found: mail.example.com

Results saved to results.json

Parsed JSON Logs:
Subdomain: www.example.com, Status: resolved
Subdomain: mail.example.com, Status: resolved
Subdomain: dev.example.com, Status: unresolved
```
