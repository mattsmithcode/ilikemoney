"""add_is_settlement_property

Revision ID: 1cc615397a92
Revises: 927ed575acbd
Create Date: 2024-02-21 09:16:25.552906

"""

# revision identifiers, used by Alembic.
revision = '1cc615397a92'
down_revision = '927ed575acbd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bill', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_settlement', sa.Boolean(), nullable=True))

    with op.batch_alter_table('bill_version', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_settlement', sa.Boolean(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bill_version', schema=None) as batch_op:
        batch_op.drop_column('is_settlement')

    with op.batch_alter_table('bill', schema=None) as batch_op:
        batch_op.drop_column('is_settlement')

    # ### end Alembic commands ###
