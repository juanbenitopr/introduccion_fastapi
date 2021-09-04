import uvicorn
from fastapi import FastAPI

from students.db import Base, engine
from students.entdpoints.routes import router as student_router

app = FastAPI()
app.include_router(router=student_router, prefix='/students')


@app.on_event('startup')
def create_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
