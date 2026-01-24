"""add users table

Revision ID: 7ac81784ecd8
Revises: 58e574560b25
Create Date: 2026-01-23 12:59:37.021540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ac81784ecd8'
down_revision: Union[str, Sequence[str], None] = '58e574560b25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.column('email', sa.String(), nullable=False, unique=True),
    sa.column('password', sa.String(), nullable=False),
    sa.column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default= sa.text('now()'))
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
