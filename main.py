from backend import app
from backend.site_maintenance import maintenance
from backend.root_auth import auth
from backend.site_services import service
from backend.site_utils import utils

# registering route templates
app.include_router(maintenance)
app.include_router(auth)
app.include_router(service)
app.include_router(utils)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)