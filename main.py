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
    return templates.TemplateResponse(
        "pages/dashboard.html", 
        {
            "request": request,
            "title": "Dashboard"
        }
    )

@app.get("/sales", response_class=HTMLResponse)
async def sales(request: Request):
    return templates.TemplateResponse("pages/sales.html", {"request": request})

@app.get("/clients", response_class=HTMLResponse)
async def clients(request: Request):
    return templates.TemplateResponse("pages/clients.html", {"request": request})

@app.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    return templates.TemplateResponse("pages/services.html", {"request": request})

@app.get("/transactions", response_class=HTMLResponse)
async def transactions(request: Request):
    return templates.TemplateResponse("pages/transactions.html", {"request": request})

@app.get("/reports", response_class=HTMLResponse)
async def reports(request: Request):
    return templates.TemplateResponse("pages/reports.html", {"request": request})

@app.get("/staff", response_class=HTMLResponse)
async def staff(request: Request):
    return templates.TemplateResponse("pages/staff.html", {"request": request})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
