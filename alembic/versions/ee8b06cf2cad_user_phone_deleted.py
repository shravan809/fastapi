"""user_phone deleted

Revision ID: ee8b06cf2cad
Revises: ca1b42890ed5
Create Date: 2024-04-23 17:30:04.099717

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee8b06cf2cad'
down_revision: Union[str, None] = 'ca1b42890ed5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
