from fastapi import FastAPI 
from fastapi.responses import JSONResponse
import logging
from service.data_loader import DataLoader


app = FastAPI()
logger = logging.getLogger(__name__)

@app.get("/names")
def get_names():
    """
    Endpoint to retrieve names from the database.
    Returns the names data or an error message if the retrieval fails.
    """
    try:
        names = DataLoader.load_data()
        logger.info("Data received successfully")
        return JSONResponse(content=names)
    except Exception as e:
        logger.error("Error while receiving data")
        return JSONResponse(content={"Error": e})
    

        
