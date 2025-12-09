from quart import Quart
from quart_.oleg import blueprint

app = Quart(__name__)

app.secret_key = "Very_secret_much_wow"
CONN_STRING = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"
app.register_blueprint(blueprint, url_prefix='/oleg')

from quart_ import routes
print(app.url_map)