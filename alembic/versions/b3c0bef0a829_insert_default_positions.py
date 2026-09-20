"""insert default positions

Revision ID: b3c0bef0a829
Revises: f366eaa9e79b
Create Date: 2026-09-07 04:05:51.896253

"""
from typing import Sequence, Union
from uuid import uuid4

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3c0bef0a829'
down_revision: Union[str, Sequence[str], None] = 'f366eaa9e79b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(
    f"""
    INSERT INTO positions (id, title)
    VALUES
        ('{uuid4()}', 'Клиент'),
        ('{uuid4()}', 'Парикмахер'),
        ('{uuid4()}', 'Администратор')
    """
)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
        "DELETE FROM positions (title)" 
        "WHERE title in ('Клиент', 'Парикмахер', 'Администратор')"
    )
