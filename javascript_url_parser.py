import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import argparse

def extract_js_files(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script', src=True)
        
        js_files = []
        for script in scripts:
            src = script['src']
            full_url = urllib.parse.urljoin(url, src)
            js_files.append(full_url)
        
        return js_files
    except requests.RequestException as e:
        print(f"Error occurred while fetching the URL: {e}")
        return []

def extract_urls_from_js(js_url):
    try:
        response = requests.get(js_url)
        response.raise_for_status()
        
        js_content = response.text
        url_pattern = re.compile(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        )
        urls = re.findall(url_pattern, js_content)
        return urls
    except requests.RequestException as e:
        print(f"Error occurred fetching the JavaScript file: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description='Script to Parse websites for javascript files and extract urls from them.')
    parser.add_argument('url', type=str, help='Add URL of the website to parse.')
    args = parser.parse_args()
    website = args.url
 
    js_files = extract_js_files(website)
    
    if js_files:
        print("JavaScript files found on the website:")
        for js_file in js_files:
            print(f"\nExtracting URLs found in {js_file}:")
            urls = extract_urls_from_js(js_file)
            if urls:
                for url in urls:
                    print(url)
            else:
                print("No URLs found in this JavaScript file.")
    else:
        print("No JavaScript files found.")

if __name__ == "__main__":
    main()
