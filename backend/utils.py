from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates

utils = APIRouter()

@utils.get("/transactions", response_class=HTMLResponse)
async def transactions(request: Request):
    return templates.TemplateResponse("pages/transactions.html", {"request": request})

@utils.get("/reports", response_class=HTMLResponse)
async def reports(request: Request):
    return templates.TemplateResponse("pages/reports.html", {"request": request})