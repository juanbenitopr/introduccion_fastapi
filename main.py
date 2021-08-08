from enum import Enum
from typing import Dict, Any

import uvicorn
from fastapi import FastAPI, Path, Query

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
def validate_name(age: int = Query(10, ge=10, le=100, title='Person Age', description='possible age of the person'),
                  name: NameTypes = Path(..., title='Person Name',
                                         description='name of the person you want to retrieve the info'),
                  ) -> Dict[str, Any]:
    response = {**PEOPLE[name], 'age_right': PEOPLE[name]['age'] == age}

    return response


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
