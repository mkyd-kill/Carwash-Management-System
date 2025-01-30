from backend import app
from backend.maintenance import maintenance
from backend.auth import auth
from backend.services import service
from backend.utils import utils

# registering route templates
app.include_router(maintenance)
app.include_router(auth)
app.include_router(service)
app.include_router(utils)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)