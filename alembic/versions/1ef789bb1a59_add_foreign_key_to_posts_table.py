"""add foreign-key to posts table

Revision ID: 1ef789bb1a59
Revises: 7ac81784ecd8
Create Date: 2026-01-23 14:38:59.710296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ef789bb1a59'
down_revision: Union[str, Sequence[str], None] = '7ac81784ecd8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
