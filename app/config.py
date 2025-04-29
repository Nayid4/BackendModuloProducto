class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///products.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


### Archivo: app/main.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)