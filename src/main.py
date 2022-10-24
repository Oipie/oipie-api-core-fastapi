"""
App definition
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
async def health():
    """
    Returns 200 OK if service is alive
    """
    return {"status": "OK"}
    