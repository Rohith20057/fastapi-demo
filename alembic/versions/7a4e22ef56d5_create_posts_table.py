"""create posts table

Revision ID: 7a4e22ef56d5
Revises: 
Create Date: 2026-01-23 12:22:55.101315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a4e22ef56d5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts_new',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('content', sa.String(), nullable=False),
        sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('owner_id', sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    )
    pass


def downgrade() -> None:    #downgrade is used to rollback the changes in the table
    """Downgrade schema."""
    op.drop_table('posts_new')
    pass
