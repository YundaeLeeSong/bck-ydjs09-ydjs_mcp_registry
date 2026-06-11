"""RSS Feed API Routers.

This module defines the FastAPI endpoints for the RSS feed domain.
"""

from fastapi import APIRouter
from mcp_core.feed import fcc_news_search, fcc_youtube_search, fcc_secret_message

# Initialize router with domain-specific prefix and tags
router = APIRouter(prefix="/feed", tags=["feed"])

@router.get("/fcc_news_search")
def news_search_endpoint(query: str, max_results: int = 3):
    """HTTP GET endpoint for news search."""
    return {"results": fcc_news_search(query, max_results)}

@router.get("/fcc_youtube_search")
def youtube_search_endpoint(query: str, max_results: int = 3):
    """HTTP GET endpoint for YouTube search."""
    return {"results": fcc_youtube_search(query, max_results)}

@router.get("/fcc_secret_message")
def secret_message_endpoint():
    """HTTP GET endpoint for the secret message."""
    return {"message": fcc_secret_message()}
