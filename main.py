from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def fun():
    return {'name':'shravan','age':27}

@app.get('/items/')
async def list_items():
    return {"car":"Benz",'model':2018}
