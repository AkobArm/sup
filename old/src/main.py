import uvicorn

from old.src.app.config.project_config import settings as main_settings

from old.src.app import get_application

app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host=main_settings.host, port=main_settings.port, reload=main_settings.debug)
