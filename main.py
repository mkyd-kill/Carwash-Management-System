from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

# setting up the static dir
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# setting up the template dir
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login():
    pass

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    data = {
            "request": request,
            "title": "Dashboard"
    }
    return templates.TemplateResponse("pages/dashboard.html", data)

@app.get("/sales", response_class=HTMLResponse)
async def sales(request: Request):
    data = {
            "request": request,
            "title": "Sales"
    }
    return templates.TemplateResponse("pages/sales.html", data)

@app.get("/clients", response_class=HTMLResponse)
async def clients(request: Request):
    data = {
            "request": request,
            "title": "Clients"
    }
    return templates.TemplateResponse("pages/clients.html", data)

@app.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    data = {
            "request": request,
            "title": "Services"
    }
    return templates.TemplateResponse("pages/services.html", data)

@app.get("/transactions", response_class=HTMLResponse)
async def transactions(request: Request):
    data = {
            "request": request,
            "title": "Transactions"
    }
    return templates.TemplateResponse("pages/transactions.html", data)

@app.get("/reports", response_class=HTMLResponse)
async def reports(request: Request):
    data = {
            "request": request,
            "title": "Reports"
    }
    return templates.TemplateResponse("pages/reports.html", data)

@app.get("/staff", response_class=HTMLResponse)
async def staff(request: Request):
    data = {
            "request": request,
            "title": "Staff"
    }
    return templates.TemplateResponse("pages/staff.html", data)

@app.get("/branch", response_class=HTMLResponse)
async def branch(request: Request):
    data = {
            "request": request,
            "title": "Branch"
    }
    return templates.TemplateResponse("pages/branch.html", data)

@app.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    data = {
            "request": request,
            "title": "Settings"
    }
    return templates.TemplateResponse("pages/settings.html", data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
