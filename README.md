# Python Web Scraping Tutorial (2025)

<a href="https://iproyal.com/proxies/"><img width="2180" height="550" alt="GitHub Banner" src="https://github.com/user-attachments/assets/c857fdbc-882d-4089-af87-cfa93408311d"></img></a>

## Overview

This repository turns a long-form tutorial into a concise, GitHub-ready guide. You will scrape the first pages of the r/programming subreddit using **Requests** and **Beautiful Soup**, then analyze which programming languages appear most often in post titles. The tutorial targets the simpler old Reddit UI at `old.reddit.com`.

> Note: Always follow a website’s Terms of Service and robots.txt. Use respectful crawl rates and unique User-Agent strings.

---

## What Is Web Scraping?

Web scraping is the practice of programmatically fetching HTML and extracting information. Many tasks only need two ingredients:
- an **HTTP client** to download HTML,
- an **HTML parser** to locate the elements you care about.

Headless browsers (or full automation via Playwright/Selenium) are used when pages require JavaScript to render content.

---

## Why Python?

Python’s ecosystem makes scraping approachable:
- **requests** – minimal, reliable HTTP client  
- **beautifulsoup4** – HTML parsing and traversal  
- Advanced options: **scrapy**, **playwright**

Python is also easy to prototype, even for non-specialists.

---

## Setup

Install Python 3.9+ and the dependencies:

```bash
pip install -r requirements.txt
# or
pip install requests beautifulsoup4
```

Create a file named `src/scraper.py` (already included here).

---

## Full Script

```python
import requests
from bs4 import BeautifulSoup
import time

# Optional: Proxy support
PROXIES = {
    "http":  "http://youruser:yourpass@geo.iproyal.com:22323",
    "https": "http://youruser:yourpass@geo.iproyal.com:22323",
}

# Storage for titles
post_titles = []
next_page = "https://old.reddit.com/r/programming/"

# Scrape 20 pages politely
for current_page in range(0, 20):
    page = requests.get(next_page,
                        headers={'User-agent': 'Sorry, learning Python!'})
    html = page.content

    soup = BeautifulSoup(html, "html.parser")
    p_tags = soup.find_all("p", "title")
    titles = [p.find("a").get_text() for p in p_tags]

    post_titles += titles
    next_page = soup.find("span", "next-button").find("a")['href']
    time.sleep(3)

# Count language mentions
language_counter = {
    "javascript": 0, "html": 0, "css": 0, "sql": 0, "python": 0, "typescript": 0,
    "java": 0, "c#": 0, "c++": 0, "php": 0, "c": 0, "powershell": 0,
    "go": 0, "rust": 0, "kotlin": 0, "dart": 0, "ruby": 0
}

words = []
for title in post_titles:
    words += [word.lower() for word in title.split()]

for word in words:
    for key in language_counter:
        if word == key:
            language_counter[key] += 1

print(language_counter)
```

---

## Example Output

```text
{'javascript': 20, 'html': 6, 'css': 10, 'sql': 0, 'python': 26, 'typescript': 1, 'java': 10, 'c#': 5, 'c++': 10, 'php': 1, 'c': 10, 'powershell': 0, 'go': 5, 'rust': 7, 'kotlin': 3, 'dart': 0, 'ruby': 1}
```

---

## Final Thoughts

In this tutorial, you learned the basics of **Python web scraping** using `requests` and `BeautifulSoup`.  
You scraped post titles from `r/programming`, analyzed the data, and even saw how to use proxies for larger jobs.

For advanced scraping, explore:
- **Scrapy** – a full-featured scraping framework  
- **Playwright** – a browser automation library for JavaScript-heavy sites  

---

### 🐍 Happy Scraping!
