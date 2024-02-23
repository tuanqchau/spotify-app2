#set up backend
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import glob
import json
import base64
from requests import post
import json

load_dotenv()
#client_id = os.getenv("CLIENT_ID")
#client_secret = os.getenv("CLIENT_SECRET")
client_id = "92a0d89fa23740b3b8f6280abf388a55"
client_secret = "cd5aee1c0d804a8a817947c7492fda7e"
print(client_id)
app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
    return {"message": "Testing endpoint"}


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "client_credentials",
    }

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"] 
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

token = get_token()
print(token)