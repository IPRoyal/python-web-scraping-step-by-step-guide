"""
Python Web Scraping Tutorial
- Fetch titles from old.reddit.com/r/programming
- Follow "next" links for multiple pages
- Count programming language mentions in titles
"""

from __future__ import annotations
import argparse
import os
import time
from typing import Dict, List, Optional
import requests
from bs4 import BeautifulSoup

DEFAULT_START_URL = "https://old.reddit.com/r/programming/"
HEADERS = {"User-Agent": "Learning Python web scraping (example)"}

LANGUAGES = [
    "javascript","html","css","sql","python","typescript","java",
    "c#","c++","php","c","powershell","go","rust","kotlin","dart","ruby"
]

def fetch(url: str, proxies: Optional[Dict[str, str]] = None, timeout: int = 30) -> bytes:
    resp = requests.get(url, headers=HEADERS, proxies=proxies, timeout=timeout)
    resp.raise_for_status()
    return resp.content

def parse_titles(html: bytes) -> (List[str], Optional[str]):
    soup = BeautifulSoup(html, "html.parser")
    p_tags = soup.find_all("p", "title")
    titles = []
    for p in p_tags:
        a = p.find("a")
        if a and a.get_text():
            titles.append(a.get_text())
    # find next page
    next_href = None
    nxt = soup.find("span", "next-button")
    if nxt:
        a = nxt.find("a")
        if a and a.get("href"):
            next_href = a["href"]
    return titles, next_href

def scrape_pages(start_url: str, pages: int, delay: float, proxies: Optional[Dict[str, str]]) -> List[str]:
    collected: List[str] = []
    url = start_url
    for i in range(pages):
        html = fetch(url, proxies=proxies)
        titles, next_url = parse_titles(html)
        collected.extend(titles)
        if not next_url:
            break
        url = next_url
        time.sleep(delay)
    return collected

def count_languages(titles: List[str], languages: List[str]) -> Dict[str, int]:
    counts = {lang: 0 for lang in languages}
    for title in titles:
        words = [w.strip(".,:;!?()[]{}'\"").lower() for w in title.split()]
        for w in words:
            if w in counts:
                counts[w] += 1
    return counts

def load_proxies_from_env() -> Optional[Dict[str, str]]:
    http = os.environ.get("HTTP_PROXY")
    https = os.environ.get("HTTPS_PROXY")
    if http or https:
        return {"http": http or "", "https": https or http or ""}
    return None

def main():
    ap = argparse.ArgumentParser(description="Scrape r/programming titles and count language mentions.")
    ap.add_argument("--pages", type=int, default=20, help="Number of pages to scrape")
    ap.add_argument("--delay", type=float, default=3.0, help="Seconds to sleep between requests")
    ap.add_argument("--start-url", default=DEFAULT_START_URL, help="Starting URL")
    ap.add_argument("--print-titles", action="store_true", help="Print collected titles")
    ap.add_argument("--use-proxy", action="store_true", help="Read proxies from HTTP_PROXY/HTTPS_PROXY env")
    args = ap.parse_args()

    proxies = load_proxies_from_env() if args.use_proxy else None
    titles = scrape_pages(args.start_url, args.pages, args.delay, proxies)

    if args.print_titles:
        for t in titles:
            print(t)

    counts = count_languages(titles, LANGUAGES)
    print(counts)

if __name__ == "__main__":
    main()
