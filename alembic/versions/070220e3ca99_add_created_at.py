"""Add created_at

Revision ID: 070220e3ca99
Revises: b9c7c68ae018
Create Date: 2024-04-22 16:57:49.667355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '070220e3ca99'
down_revision: Union[str, None] = 'b9c7c68ae018'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('created_at', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'created_at')
    # ### end Alembic commands ###