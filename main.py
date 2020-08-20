from app import app
from routes import api
app.register_blueprint(api, url_prefix='/api/v1.0')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
