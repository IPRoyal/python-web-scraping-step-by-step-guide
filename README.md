# Python Web Scraping Tutorial (2025)

<a href="https://iproyal.com/proxies/">
  <img width="2180" height="550" alt="GitHub Banner"
       src="https://github.com/user-attachments/assets/c857fdbc-882d-4089-af87-cfa93408311d"></img>
</a>

## Overview

This repository turns a full-length article into a practical, GitHub-ready guide.  
You’ll scrape the **r/programming** subreddit using **Requests** and **BeautifulSoup**, collect post titles, and analyze which **programming languages** appear most often.

The tutorial targets **old Reddit** (`https://old.reddit.com`) — an easier static HTML interface that doesn’t require JavaScript.

> ⚠️ Always check a website’s robots.txt and Terms of Service before scraping.  
> Respect rate limits, add delays, and use a unique User-Agent.

---

## What Is Web Scraping?

Web scraping means using code to:
1. **Fetch** the HTML of a webpage, and  
2. **Extract** useful data from it.

Most sites can be scraped with:
- `requests` – downloads the HTML  
- `beautifulsoup4` – parses and navigates HTML  

For pages that render data dynamically via JavaScript, you’ll need **Playwright** or **Selenium**.

**Common use cases:**
- Market & price tracking  
- Research & analytics  
- Trend or keyword monitoring  

---

## Why Python?

Python’s ecosystem is the go-to choice for scraping in 2025 because it’s simple, powerful, and well-supported.  
Popular libraries include:

| Library | Purpose |
|----------|----------|
| `requests` | Fetch HTML from websites |
| `beautifulsoup4` | Parse and navigate HTML trees |
| `scrapy` | Advanced framework for large projects |
| `playwright` | Headless browser automation |

---

## Setup

You’ll need **Python 3.9+**.

```bash
pip install requests beautifulsoup4
# or
pip install -r requirements.txt
```

Create a file `src/scraper.py` and follow the examples below.

---

## Step 1: Fetch HTML

```python
import requests

page = requests.get(
    "https://old.reddit.com/r/programming/",
    headers={'User-agent': 'Learning Python Web Scraping'}
)
html = page.content
```

---

## Step 2: Parse the Page

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
p_tags = soup.find_all("p", "title")
titles = [p.find("a").get_text() for p in p_tags]

print(titles)
```

At this point, you’ll see the post titles from the first page of `r/programming`.

---

## Step 3: Scrape Multiple Pages

Old Reddit includes a “Next” button with `<span class="next-button">`.  
We can loop through multiple pages safely:

```python
import requests
from bs4 import BeautifulSoup
import time

post_titles = []
next_page = "https://old.reddit.com/r/programming/"

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

print(post_titles)
```

---

## Step 4: Analyze the Data

Let’s count mentions of popular programming languages:

```python
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

**Example output:**
```text
{'javascript': 20, 'html': 6, 'css': 10, 'sql': 0, 'python': 26, 'typescript': 1,
 'java': 10, 'c#': 5, 'c++': 10, 'php': 1, 'c': 10, 'powershell': 0,
 'go': 5, 'rust': 7, 'kotlin': 3, 'dart': 0, 'ruby': 1}
```

---

## Step 5: Optional — Use Proxies

To avoid rate limits or bans, route requests through a **proxy provider** such as [IPRoyal](https://iproyal.com/proxies/).

```python
PROXIES = {
    "http":  "http://youruser:yourpass@geo.iproyal.com:22323",
    "https": "http://youruser:yourpass@geo.iproyal.com:22323",
}

page = requests.get(next_page,
                    headers={'User-agent': 'Just learning Python, sorry!'},
                    proxies=PROXIES)
```

Proxies allow rotation between IPs, making traffic look more natural and reducing blocks.

---

## Summary

You now know how to:
1. Fetch and parse HTML with Requests and BeautifulSoup  
2. Scrape multiple pages safely  
3. Count language mentions from Reddit titles  
4. Optionally add proxy support for stability  

For larger or dynamic projects, explore **Scrapy** or **Playwright**.

---

### 🐍 Happy Scraping!
