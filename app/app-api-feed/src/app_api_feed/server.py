"""Main entry point for the FastAPI Feed Service.

This module orchestrates the startup of the HTTP API application.
"""

import uvicorn
from fastapi import FastAPI
from app_api_feed.routers import router as feed_router

# Create the standard FastAPI application
app = FastAPI(
    title="Feed Service API",
    description="HTTP API Service for Feed operations.",
    version="1.0.0"
)

# Include the domain-specific router
app.include_router(feed_router)

def main():
    """Starts the application service."""
    print("Starting the HTTP API Service...")
    print("API documentation is available at: http://localhost:8000/docs")
    
    # Uvicorn entry point points to the 'app' instance
    uvicorn.run("app_api_feed.server:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    main()
