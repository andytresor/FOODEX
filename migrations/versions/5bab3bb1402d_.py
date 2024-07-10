"""empty message

Revision ID: 5bab3bb1402d
Revises: b986159c1806
Create Date: 2024-07-10 09:13:24.969693

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5bab3bb1402d'
down_revision = 'b986159c1806'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('quantity')
        batch_op.drop_column('table_number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('table_number', mysql.VARCHAR(length=100), nullable=False))
        batch_op.add_column(sa.Column('quantity', mysql.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
