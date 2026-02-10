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
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), sa.ForeignKey("users.id", ondelete= "CASCADE"), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table='posts_new', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts_new')
    pass
