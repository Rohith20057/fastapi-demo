"""add content column to post table

Revision ID: 58e574560b25
Revises: 7a4e22ef56d5
Create Date: 2026-01-23 12:44:21.052022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58e574560b25'
down_revision: Union[str, Sequence[str], None] = '7a4e22ef56d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
