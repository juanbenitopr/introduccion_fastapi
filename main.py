import uvicorn
from fastapi import FastAPI

app = FastAPI()


# Your code here
@app.get('/{id}', status_code=201)
def hello_world(id: int, parameter: str = 'hola'):
    return {'content': 'hello world', 'id': id, 'param': parameter}


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
