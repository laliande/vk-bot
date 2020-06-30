from app import app


@app.route('/')
def index():
    return 'ok'


if __name__ == "__main__":
    app.run()
