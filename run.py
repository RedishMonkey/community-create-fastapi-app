import uvicorn

from src.core import settings


if __name__ == "__main__":
    uvicorn.run(
        "main:app",              # module_name:app_instance
        host=settings.host,      # the host IP to bind
        port=settings.port,      # port
        reload=settings.reload   # auto-reload on code changes (dev only)
    )