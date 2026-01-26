from quart import Quart

app = Quart(__name__)

app.secret_key = "Very_secret_much_wow"
CONN_STRING = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"

from quart_ import routes
print(app.url_map)