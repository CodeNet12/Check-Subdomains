import requests
import re
import time

pattern = r"https?://[\w\.-]+\.[a-z]{2,6}(?:/[\w\-]*)*"
pattern_noparam = r"https?://[\w\.-]+\.[a-z]{2,6}"

url = input("Enter the URL: ")

def check_url(url):
    if re.match(pattern, url) or re.match(pattern_noparam, url):
        print("Checking the query of your URL...")
        time.sleep(2)
        print("__________________")
        time.sleep(2)
        print("Query: {done} True")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Status: OK")
            else:
                print("Error: Status Code", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Request Failed:", e)
    else:
        print("Invalid URL format.")

def check_subdomains():
    try:
        with open("common.txt", "r") as file:
            for line in file:
                newurl = url.strip("/") + "/" + line.strip()
                try:
                    response = requests.get(newurl)
                    if response.status_code == 200:
                        print(f"URL found: {newurl}")
                    else:
                        print(f"Not found: {newurl}")
                except requests.exceptions.RequestException as e:
                    print("Request Failed:", e)
    except FileNotFoundError:
        print("common.txt file not found.")

# Call functions
check_url(url)
check_subdomains()
