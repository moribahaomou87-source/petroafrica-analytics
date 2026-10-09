from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
DATA_DIR = APP_DIR.parent / "data"
DB_PATH = DATA_DIR / "petroafrica.db"
