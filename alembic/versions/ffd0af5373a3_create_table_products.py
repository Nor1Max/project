"""create table products

Revision ID: ffd0af5373a3
Revises: b3c0bef0a829
Create Date: 2026-09-09 01:12:25.687683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ffd0af5373a3'
down_revision: Union[str, Sequence[str], None] = 'b3c0bef0a829'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
