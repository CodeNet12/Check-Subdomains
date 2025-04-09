# URL & Subdomain Checker

A simple Python tool to validate URLs and check for sub-URLs (subpaths) using a wordlist. Useful for reconnaissance, bug bounty hunting, or general web exploration.

## Features

- URL validation using regular expressions (Regex).
- Sub-URL discovery using a `common.txt` wordlist.
- Error handling (e.g., timeouts, invalid responses).
- Supports both `http` and `https`.

## Requirements

- Python 3.x
- `requests` library
- `common.txt` file , source : `https://github.com/danielmiessler/SecLists`

Install requirements using:

```bash
git clone https://github.com/CodeNet12/Check-Subdomains.git
cd Check-Subdomains
pip install -r requirements.txt
python main.py
# Check-Subdomains
