#set up backend
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
import os
import glob
import json

app = FastAPI()

origins = [
    "*",
]