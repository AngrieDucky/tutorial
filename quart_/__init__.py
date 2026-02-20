from quart import Quart

app = Quart(__name__)

app.secret_key = "Very_secret_much_wow"
# http://oleg.ru -> dns resolver -> 0.0.0.0 -> goal
# 0.0.0.0 -> goal
CONN_STRING = "postgresql+psycopg2://postgres:1234@127.0.0.1:5432/postgres"

from quart_ import routes
print(app.url_map)