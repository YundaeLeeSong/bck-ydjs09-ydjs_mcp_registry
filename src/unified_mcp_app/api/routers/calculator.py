"""Calculator API Routers.

This module defines the FastAPI endpoints for the calculator domain.
It maps HTTP requests to core business logic.

Design Pattern:
    Router - Decouples HTTP endpoint definitions from core logic.
"""

from fastapi import APIRouter, HTTPException
from unified_mcp_app.core import multiply, add_numbers, subtract, divide

# Initialize router with domain-specific prefix and tags for Swagger documentation
router = APIRouter(prefix="/calculator", tags=["calculator"])

@router.post("/multiply")
def multiply_endpoint(a: float, b: float):
    """HTTP POST endpoint for multiplication."""
    return {"result": multiply(a, b)}

@router.post("/add")
def add_endpoint(x: float, y: float):
    """HTTP POST endpoint for addition."""
    return {"result": add_numbers(x, y)}

@router.post("/subtract")
def subtract_endpoint(a: float, b: float):
    """HTTP POST endpoint for subtraction."""
    return {"result": subtract(a, b)}

@router.post("/divide")
def divide_endpoint(a: float, b: float):
    """HTTP POST endpoint for division with error handling."""
    try:
        return {"result": divide(a, b)}
    except ValueError as e:
        # Map domain exceptions to HTTP status codes
        raise HTTPException(status_code=400, detail=str(e))
