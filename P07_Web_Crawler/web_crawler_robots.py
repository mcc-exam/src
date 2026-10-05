import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

# User input
start_url = input("Enter starting URL: ")
max_pages = int(input("Enter number of pages: "))
delay = float(input("Enter crawling delay (seconds): "))

# Get website domain
domain = urlparse(start_url).netloc

# Read robots.txt
robots = RobotFileParser()
robots.set_url(urljoin(start_url, "/robots.txt"))

try:
    robots.read()
except Exception:
    print("Could not read robots.txt")

# Store URLs
queue = [start_url]
visited = set()

while queue and len(visited) < max_pages:
    url = queue.pop(0)

    if url in visited:
        continue

    # Check robots.txt
    if not robots.can_fetch("*", url):
        print("Blocked by robots.txt:", url)
        continue

    try:
        # Crawling delay
        time.sleep(delay)

        # Fetch page
        response = requests.get(
            url,
            headers={"User-Agent": "Educational-Web-Crawler"},
            timeout=10
        )

        if response.status_code != 200:
            print("Failed:", url, response.status_code)
            continue

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        visited.add(url)

        print("\nPage", len(visited))
        print("URL:", url)
        print(
            "Title:",
            soup.title.text.strip()
            if soup.title
            else "No Title"
        )

        # Extract links
        for link in soup.find_all("a", href=True):
            new_url = urljoin(url, link["href"])
            new_domain = urlparse(new_url).netloc

            # Crawl only the same website
            if (
                new_domain == domain
                and new_url not in visited
                and new_url not in queue
            ):
                queue.append(new_url)

    except requests.RequestException as e:
        print("Error:", e)

print("\nCrawling completed.")
print("Total pages crawled:", len(visited))
