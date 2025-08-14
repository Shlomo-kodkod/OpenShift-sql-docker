from fastapi import FastAPI
import logging
from data_loader import DataLoader


app = FastAPI()
logger = logging.getLogger(__name__)

@app.get("/names")
def get_names():
    try:
        names = DataLoader.load_data()
        logger.info("Data received successfully")
        return names
    except Exception as e:
        logger.error("Error while receiving data")
        return {"Error": e}
        
