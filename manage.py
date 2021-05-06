from flask import Flask
from appReWate.views import appReWater_bp
from appPhoto.views import appPhoto_bp
import settings


app = Flask(__name__)
app.config.from_object("settings.DevelopmentConfig")

app.register_blueprint(appReWater_bp, url_prefix='/water')
app.register_blueprint(appPhoto_bp, url_prefix='/photo')


@app.route('/')
def hello_world():
    print(app.config.get("DB_SERVER"))
    print(app.config.get("DEBUG"))
    return 'Hello World!'


if __name__ == '__main__':
    print("----")
    app.run()