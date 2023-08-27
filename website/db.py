import psycopg2
import os 
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(database=os.environ.get('DATABASE'),
                        host=os.environ.get('HOST'),
                        user=os.environ.get('USER'),
                        password=os.environ.get('PASSWORD'),
                        port=os.environ.get('PORT'), sslmode='require')

cursor = conn.cursor()