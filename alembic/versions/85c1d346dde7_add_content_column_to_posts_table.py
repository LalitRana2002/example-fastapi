"""add content column to posts table

Revision ID: 85c1d346dde7
Revises: f7d8431d315b
Create Date: 2026-10-16 14:15:01.057415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85c1d346dde7'
down_revision: Union[str, Sequence[str], None] = 'f7d8431d315b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
