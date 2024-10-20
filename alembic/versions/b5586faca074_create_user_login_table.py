"""create user_login table

Revision ID: b5586faca074
Revises: 
Create Date: 2024-10-20 12:20:08.670478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5586faca074'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.String(100), nullable=False, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('username', sa.String(100), nullable=False, unique=True),
        sa.Column('password', sa.String(200), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())
    )


def downgrade() -> None:
    op.drop_table('user')