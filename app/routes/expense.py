from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.delete("/{expense_id}")
def dete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Delete the expense record
    """

    # Fetch the target expense
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    # Validate the expense
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    # Ownership check
    if expense.user_id != current_user.id:
        raise HTTPException(403, detail="You are not allowed to delete this expense")

    # Delete
    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}


@router.put("/{expense_id}")
def update_expense(
    expense_id: int,
    data: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Update an expense record for owner
    """

    # Fetch the target expese
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    # Validate the Resource
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    # Owner validation
    if expense.user_id != current_user.id:

        raise HTTPException(
            status_code=403, detail="You are not allowed to modify this expense"
        )

    expense.title = data.title
    expense.amount = data.amount
    expense.category = data.category

    db.commit()
    db.refresh(expense)

    return expense


@router.post("/")
def create_expense(
    data: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Function creates a new expense for the user
    """

    new_expense = Expense(
        title=data.title,
        amount=data.amount,
        category=data.category,
        user_id=current_user.id,
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


@router.get("/")
def get_expense(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    """
    Function provides expenses of only logged-in user
    """

    expenses = db.query(Expense).filter(Expense.user_id == current_user.id).all()

    return expenses
