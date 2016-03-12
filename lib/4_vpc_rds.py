import time
import MySQLdb
import os
import commands
import dotenv
import json

dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.env"))
dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.env"))
mysqlconfig = json.loads(os.environ['mysqlconfig'])

connector = MySQLdb.connect(host=mysqlconfig['host'], db=mysqlconfig['db'], user=mysqlconfig['user'], passwd=mysqlconfig['password'], charset="utf8")
cursor = connector.cursor()
      
      
def _(cmd):
  return commands.getoutput(cmd) 

def hello(val):
  sql = "insert into lambda_test values(0, %s, NOW())"
  cursor.execute(sql, (val,))
  connector.commit()
 
  return val + str(time.time())
