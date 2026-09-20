"""delete table positions

Revision ID: 42d46dce3372
Revises: 3cc2c090f115
Create Date: 2026-09-10 01:46:43.695716

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42d46dce3372'
down_revision: Union[str, Sequence[str], None] = '3cc2c090f115'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        'users',
        sa.Column(
            'is_admin',
            sa.Boolean(),
            nullable=False,
            server_default=sa.false()
        )
    )

    op.add_column(
        'users',
        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default=sa.text('now()'),
            nullable=False
        )
    )

    op.drop_constraint(
        op.f('users_position_id_fkey'),
        'users',
        type_='foreignkey'
    )

    op.drop_column('users', 'position_id')

    op.drop_table('positions')


def downgrade() -> None:
    """Downgrade schema."""

    op.create_table(
        'positions',
        sa.Column('title', sa.VARCHAR(), nullable=False),
        sa.Column('id', sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('positions_pkey')),
        sa.UniqueConstraint(
            'title',
            name=op.f('positions_title_key')
        )
    )

    op.add_column(
        'users',
        sa.Column(
            'position_id',
            sa.UUID(),
            nullable=True
        )
    )

    op.create_foreign_key(
        op.f('users_position_id_fkey'),
        'users',
        'positions',
        ['position_id'],
        ['id']
    )

    op.drop_column('users', 'created_at')
    op.drop_column('users', 'is_admin')
