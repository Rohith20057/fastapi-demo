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


def upgrade() -> None:   #upgrade is used to make the chages in the table
    """Upgrade schema."""
    op.create_table('posts_new',sa.column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.column('title', sa.String(), nullable=False),
    sa.column('content', sa.String(), nullable=False),
    sa.column('published', sa.Boolean(), server_default='TRUE', nullable=False),
    sa.column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default= sa.text('now()')),
    sa.column('owner_id', sa.Integer(), sa.ForeignKey("users.id", ondelete= "CASCADE"), nullable = False)
    )
    pass


def downgrade() -> None:    #downgrade is used to rollback the changes in the table
    """Downgrade schema."""
    op.drop_table('posts_new')
    pass
