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
    op.add_column('posts_new',sa.Column('content',sa.Strint(),nullable=False))
    
    pass


def downgrade() -> None:
    op.drop_column('posts_new','content')
    pass
