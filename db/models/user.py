from typing import Optional, List, TYPE_CHECKING
# from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from ..base_model import Base
from sqlalchemy.orm import relationship
from .room import user_room_association
from .receipt import user_item_association, UserReceiptAssociation

if TYPE_CHECKING:
    from .room import Room  # Import Room only for type checking
    from .receipt import Item, Receipt, UserReceiptAssociation  # Import Item only for type checking

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(30), unique=True)
    email: Mapped[Optional[str]]
    username: Mapped[Optional[str]] = mapped_column(String(50), unique=True)
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="users", cascade="all, delete-orphan"
    # )

    # Establish the many-to-many relationship with Room
    rooms: Mapped[List["Room"]] = relationship(
        "Room",
        secondary=user_room_association,
        back_populates="users"
    )

     # Establish the many-to-many relationship with Item
    items: Mapped[List["Item"]] = relationship(
        "Item",
        secondary=user_item_association,
        back_populates="users"
    )

    receipts: Mapped[List["Receipt"]] = relationship(
        secondary="user_receipt", back_populates="users", viewonly=True
    )

    receipt_associations: Mapped[List["UserReceiptAssociation"]] = relationship(back_populates="user")
    

    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, phone-number={self.phone_number!r}, email={self.email!r} )"