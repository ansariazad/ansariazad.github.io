"""
Web Scraper — Portfolio Demo
Scrapes top headlines from a news site. Shows Python scraping skill.
Run: pip install requests beautifulsoup4 && python scraper.py
"""
import json
import datetime


def generate_sample_data():
    """Generate sample scraped data to demonstrate output format."""
    headlines = [
        {"title": "AI Revolution: GPT-5 Changes Everything", "source": "TechCrunch", "time": "2 hours ago"},
        {"title": "Python Surpasses JavaScript in Developer Survey", "source": "Stack Overflow", "time": "4 hours ago"},
        {"title": "Remote Work Now Permanent at 60% of Tech Companies", "source": "Forbes", "time": "6 hours ago"},
        {"title": "India's Tech Sector Grows 15% in 2026", "source": "Economic Times", "time": "8 hours ago"},
        {"title": "FastAPI Becomes #1 Python Web Framework", "source": "GitHub Blog", "time": "12 hours ago"},
    ]
    return headlines


def scrape_with_requests():
    """Scrape using requests + BeautifulSoup (if available)."""
    try:
        import requests
        from bs4 import BeautifulSoup

        url = "https://news.ycombinator.com"
        print(f"Scraping {url}...")

        response = requests.get(url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select(".titleline > a")[:10]

        results = []
        for i, item in enumerate(items, 1):
            results.append({
                "rank": i,
                "title": item.get_text(),
                "url": item.get("href", ""),
            })

        return results

    except ImportError:
        print("requests/beautifulsoup4 not installed. Using sample data.\n")
        return None
    except Exception as e:
        print(f"Error scraping: {e}. Using sample data.\n")
        return None


def save_results(data, filename="scraped_data.json"):
    """Save results to JSON."""
    output = {
        "scraped_at": str(datetime.datetime.now()),
        "total_items": len(data),
        "data": data,
    }
    with open(filename, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved {len(data)} items to {filename}")


def display_results(data):
    """Pretty print results."""
    print("\n" + "=" * 60)
    print("  SCRAPED HEADLINES")
    print("=" * 60)
    for item in data:
        rank = item.get("rank", "-")
        title = item.get("title", "")
        source = item.get("source", item.get("url", "")[:40])
        print(f"\n  [{rank}] {title}")
        print(f"      └─ {source}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("🕷️  Web Scraper Demo")
    print("─" * 40)

    # Try real scraping first
    results = scrape_with_requests()

    if not results:
        # Fall back to sample data
        results = [{"rank": i + 1, **h} for i, h in enumerate(generate_sample_data())]

    display_results(results)
    save_results(results)
    print("\nDone!")
