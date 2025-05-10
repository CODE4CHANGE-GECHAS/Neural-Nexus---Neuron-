from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'localhost'
PORT = '8900'
ENV = 'dev'

GEMINI_API_KEY = os.getenv("AIzaSyDEVm91FZurMeFW9z6pkJ_k8aRjIXFIfGc")