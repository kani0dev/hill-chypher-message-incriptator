from fastapi import FastAPI

app = FastAPI()

@app.get('/incript')
def incript_message(message: srt ):
   return message 
