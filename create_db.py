from app import app
from src.models import db

with open('schema.sql', 'r') as sql_file:
    sql = sql_file.read()

with app.app_context():
    db.engine.execute(sql)
