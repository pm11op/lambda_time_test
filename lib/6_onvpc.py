import time
import os
import commands
import dotenv
import json

dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.env"))
dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.env"))
      
def _(cmd):
  return commands.getoutput(cmd) 

def hello(val):
  return val + str(time.time())
