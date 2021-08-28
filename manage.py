from flask_migrate import Migrate

from config import DevelopConfig

from services import create_app
from services.models import db
    
if __name__ == "__main__":
    app = create_app(DevelopConfig)
    db.init_app(app)
    migrate = Migrate(directory="services/migrations")
    migrate.init(app, db)
    
