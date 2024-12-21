from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates

utils = APIRouter()

@utils.get("/transactions", response_class=HTMLResponse)
async def transactions(request: Request):
    data = {
            "request": request,
            "title": "Transactions"
    }
    return templates.TemplateResponse("pages/transactions.html", data)

@utils.get("/reports", response_class=HTMLResponse)
async def reports(request: Request):
    data = {
            "request": request,
            "title": "Reports"
    }
    return templates.TemplateResponse("pages/reports.html", data)