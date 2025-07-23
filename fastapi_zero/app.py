from fastapi import FastAPI
from http import HTTPStatus
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/exercicio-html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def exercicio_aula_02():
    return """
    <html>
      <head>
        <title>Nosso olá mundo!</title>
      </head>
      <body>
        <h1>olá, mundo!</h1>
      </body>
    </html>"""


#def read_root():
    #return {'message': 'olá, mundo!'}
