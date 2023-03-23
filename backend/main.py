from api import create_app
from settings import DATABASE, DB_USER

app = create_app(database=DATABASE, db_user=DB_USER)
app.run(debug = True)
