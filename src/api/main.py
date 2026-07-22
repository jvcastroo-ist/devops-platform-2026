from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/athlete/load")
def athlete_load():
    raise HTTPException(status_code=501, detail="not implemented yet")

@app.get("/sea/latest")
def sea_latest():
    raise HTTPException(status_code=501, detail="not implemented yet")

@app.get("/metrics")
def metrics():
    raise HTTPException(status_code=501, detail="not implemented yet")
