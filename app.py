from config import DevelopConfig

from services import create_app

if __name__ == '__main__':
    app = create_app(DevelopConfig)
    app.run()