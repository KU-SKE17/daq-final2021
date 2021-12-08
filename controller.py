import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

db = mysql.connect(host=DB_HOST,
                   user=DB_USER,
                   passwd=DB_PASSWD,
                   db=DB_NAME)


def get_products():
    cs = db.cursor()
    cs.execute("SELECT id ,name FROM product")
    result = [models.ProductShort(product_id, name) for product_id, name in cs.fetchall()]
    cs.close()
    return result

## Your code here