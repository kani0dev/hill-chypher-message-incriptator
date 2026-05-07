from fastapi import FastAPI
from .service.hill_ciphey  import cypherService;
from pydantic import BaseModel

class request(BaseModel):
      msg: str

app = FastAPI()


@app.post('/incript')
def incript_message(message: request):
   response = cypherService.encoder(message.msg)      
   return response

@app.post('/decript')
def decript_message(message: request):
   response = cypherService.decoder(message.msg)
   return response