"""Add hashed_password to users

Revision ID: e2962186fa82
Revises: d62d824bf75e
Create Date: 2026-01-27 00:25:11.813887
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = 'e2962186fa82'
down_revision: Union[str, Sequence[str], None] = 'd62d824bf75e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('users', 'hashed_password')
