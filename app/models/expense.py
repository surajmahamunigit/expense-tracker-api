from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base


class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    # Description of the expense
    title = Column(String, nullable=False, index=True)

    # Amount spent
    amount = Column(Float, nullable=False)

    # Category
    category = Column(String, nullable=False, index=True)

    # Link expense to the user
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
