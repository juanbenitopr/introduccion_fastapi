from enum import Enum

import uvicorn
from fastapi import FastAPI, Path

app = FastAPI()


class NameTypes(str, Enum):
    JUAN = 'JUAN'
    ANTONIO = 'ANTONIO'


PEOPLE = {
    NameTypes.JUAN: {
        'age': 23,
        'name': NameTypes.JUAN.value
    },
    NameTypes.ANTONIO: {
        'age': 23,
        'name': NameTypes.ANTONIO.value
    }
}


@app.get('/{name}', status_code=201)
def validate_name(name: NameTypes = Path(..., description='name of the person you want to retrieve the info')):
    return PEOPLE[name]


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
