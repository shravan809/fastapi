"""Add user_id column to blog table

Revision ID: b9c7c68ae018
Revises: 
Create Date: 2024-04-22 16:52:27.716529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9c7c68ae018'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blog', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blog', type_='foreignkey')
    op.drop_column('blog', 'user_id')
    # ### end Alembic commands ###
