"""rename nick_google_meet

Revision ID: bae24565bdee
Revises: 8e9ece31e32f
Create Date: 2023-12-21 12:21:42.915253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bae24565bdee'
down_revision: Union[str, None] = '8e9ece31e32f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nick_google_meet', sa.String(), nullable=False))
    op.drop_column('users', 'nick_meet')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nick_meet', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'nick_google_meet')
    # ### end Alembic commands ###
