from pathlib import Path


DATA_PATH = Path(__file__).parent / 'data/api'
DATA_PATH.mkdir(parents=True, exist_ok=True)