from fastapi import FastAPI
import os
import uvicorn

app=FastAPI()

@app.get('/')
async def fun():
    return {'name':'shravan','age':27}

@app.get('/items/')
async def list_items():
    return {"car":"Benz",'model':2018}

@app.get('/test')
def list_model():
    return{"message":"File added"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)