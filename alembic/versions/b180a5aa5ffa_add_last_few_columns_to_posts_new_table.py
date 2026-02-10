"""add last few columns to posts_new table

Revision ID: b180a5aa5ffa
Revises: 1ef789bb1a59
Create Date: 2026-01-23 14:46:18.995339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b180a5aa5ffa'
down_revision: Union[str, Sequence[str], None] = '1ef789bb1a59'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts_new', sa.Column(
        'published', sa.Boolean(), server_default='TRUE', nullable=False))
    op.add_column('posts_new', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default= sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts_new', 'published')
    op.drop_column('posts_new', 'created_at')
    pass
