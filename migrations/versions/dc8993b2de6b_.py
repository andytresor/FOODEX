"""empty message

Revision ID: dc8993b2de6b
Revises: 76b3163b1600
Create Date: 2024-07-31 16:04:30.958500

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dc8993b2de6b'
down_revision = '76b3163b1600'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commands',
    sa.Column('command_id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('command_id')
    )
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('qty')
        batch_op.drop_column('total_price')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('total_price', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('qty', mysql.INTEGER(), autoincrement=False, nullable=False))

    op.drop_table('commands')
    # ### end Alembic commands ###