"""empty message

Revision ID: 91b7f3d23403
Revises: 5a1729370788
Create Date: 2024-05-05 07:04:33.928113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91b7f3d23403'
down_revision: Union[str, None] = '5a1729370788'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_invite_registation_code'), 'invite_registation', ['code'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_invite_registation_code'), table_name='invite_registation')
    # ### end Alembic commands ###
