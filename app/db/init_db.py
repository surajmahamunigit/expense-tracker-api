from app.db.database import Base, engine

# Import all the models so SQLAlchemy can register
from app.models.user import User
from app.models.expense import Expense


def init_db():
    Base.metadata.create_all(bind=engine)
