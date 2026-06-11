"""RSS Feed processing logic.

This module handles the retrieval and parsing of RSS feeds from FreeCodeCamp.
It encapsulates external network interactions and data filtering.
"""

import feedparser

def fcc_news_search(query: str, max_results: int = 3) -> list:
    """Searches the FreeCodeCamp news RSS feed for a specific query.

    Args:
        query: The search term to look for in titles and descriptions.
        max_results: The maximum number of results to return. Defaults to 3.

    Returns:
        A list of dictionaries containing title and url for matching articles.
    """
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
    results = []
    query_lower = query.lower()
    
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        # Perform case-insensitive search
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({"title": title, "url": entry.get("link", "")})
        if len(results) >= max_results:
            break
            
    return results or [{"message": "No results found"}]

def fcc_youtube_search(query: str, max_results: int = 3) -> list:
    """Searches the FreeCodeCamp YouTube RSS feed for a specific query.

    Args:
        query: The search term to look for in video titles.
        max_results: The maximum number of results to return. Defaults to 3.

    Returns:
        A list of dictionaries containing title and url for matching videos.
    """
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ")
    results = []
    query_lower = query.lower()
    
    for entry in feed.entries:
        title = entry.get("title", "")
        if query_lower in title.lower():
            results.append({"title": title, "url": entry.get("link", "")})
        if len(results) >= max_results:
            break
            
    return results or [{"message": "No videos found"}]

def fcc_secret_message() -> str:
    """Returns a static secret message.

    Returns:
        A string containing a secret coding message.
    """
    return "Keep exploring! and happy coding! (MCP Server)"
