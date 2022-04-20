import os
import dotenv

dotenv.load_dotenv(
    os.path.join(os.path.dirname(__file__), '.env')
)


class Settings(object):
    # Server
    HTTP_SERVER_HOST = os.environ.get("HTTP_SERVER_HOST")
    HTTP_SERVER_PORT = int(os.environ.get("HTTP_SERVER_PORT"))
    COUNT_WORKERS_UVICORN = int(os.environ.get("COUNT_WORKERS_UVICORN", 1))
