# Python Web Scraping Tutorial (2025)

<a href="https://iproyal.com/blog/python-web-scraping-step-by-step-guide/">
  <img alt="Banner" src="https://cms.iproyal.com/uploads/Python_Web_Scraping_Step_By_Step_Guide_2022_847x300_f433168d2b.jpg" width="1694" height="600">
</a>

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

## Fetching HTML

Use `requests.get()` with a distinctive User-Agent:

```python
import requests

page = requests.get(
    "https://old.reddit.com/r/programming/",
    headers={"User-agent": "Learning Python web scraping (example)"}
)
html = page.content
```

---

## Parsing HTML

Parse with Beautiful Soup and select the title container (`<p class="title">` in the old UI):

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
p_tags = soup.find_all("p", "title")
titles = [p.find("a").get_text() for p in p_tags]
print(titles)
```

You can find CSS classes by inspecting the page in your browser (Right click → Inspect).

<figure>
  <img src="https://cms.iproyal.com/uploads/blog1_7552525d29.png" alt="Inspect element - open" />
</figure>

<figure>
  <img src="https://cms.iproyal.com/uploads/blog2_672b2e2cbe.png" alt="Inspect element - DOM view" />
</figure>

---

## Scraping Multiple Pages

Old Reddit exposes a **Next** button with a `<span class="next-button">`. Follow it and iterate with a pause to be polite:

```python
next_page = soup.find("span", "next-button").find("a")["href"]
```

The included script iterates N pages (default 20), collects titles, and sleeps between requests.

---

## Finding the Most Talked-About Language

After collecting titles, split them into words and count mentions of common programming languages (based on popular surveys). The sample list is in the script as `LANGUAGES` and can be customized.

Example output (values vary by time):
```text
{'javascript': 20, 'html': 6, 'css': 10, 'sql': 0, 'python': 26, 'typescript': 1, 'java': 10, 'c#': 5, 'c++': 10, 'php': 1, 'c': 10, 'powershell': 0, 'go': 5, 'rust': 7, 'kotlin': 3, 'dart': 0, 'ruby': 1}
```

---

## Using Proxies (Optional)

For heavier scraping, route requests through a proxy provider. Example with IPRoyal-style endpoint:

```python
PROXIES = {
    "http":  "http://youruser:yourpass@geo.iproyal.com:22323",
    "https": "http://youruser:yourpass@geo.iproyal.com:22323",
}
# requests.get(url, headers=HEADERS, proxies=PROXIES, timeout=30)
```

Rotating proxies and randomized delays make traffic look more natural and reduce blocks.

---

## Run

```bash
# scrape 10 pages with 3s delay and print language counts
python -m src.scraper --pages 10 --delay 3
```

Options:
- `--pages` number of pages to scrape (default 20)
- `--delay` seconds between requests (default 3)
- `--start-url` starting URL (default r/programming old UI)
- `--print-titles` print collected titles
- `--use-proxy` read proxies from env `HTTP_PROXY`/`HTTPS_PROXY` or hardcode in script

---

## Project Structure

```
.
├─ README.md
├─ requirements.txt
└─ src
   └─ scraper.py
```

---

## FAQ

**Can web pages detect scraping?**  
Yes—fast or repetitive traffic, uniform User-Agents, and missing assets are signals. Slow down, randomize headers/delays, and consider headless browsers or proxies.

**Is this legal?**  
Follow site terms and robots.txt. Avoid personal data collection and rate-limit your requests.

**Why old.reddit.com?**  
Its markup is simpler for beginners. The new UI often uses dynamic class names and client-side rendering.

---

## License

MIT. See `LICENSE`.

---

## Credits

Adapted and paraphrased for GitHub from source material by IPRoyal / Justas Vitaitis (2025).
