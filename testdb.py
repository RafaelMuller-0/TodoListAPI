from database import engine
from sqlalchemy import text

with engine.connect() as conn:
    test = conn.execute(text("select 1")).scalar()
    print(test)