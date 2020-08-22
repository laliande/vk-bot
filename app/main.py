from app import app
#app.register_blueprint(api, url_prefix='/api/v1.1')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
