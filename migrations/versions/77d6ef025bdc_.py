"""empty message

Revision ID: 77d6ef025bdc
Revises: 
Create Date: 2024-07-08 18:10:13.352885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77d6ef025bdc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_table('auth',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=500), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('menu',
    sa.Column('menu_id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=250), nullable=False),
    sa.Column('img_name', sa.Text(), nullable=False),
    sa.Column('mimetype', sa.Text(), nullable=False),
    sa.Column('menu_name', sa.String(length=100), nullable=False),
    sa.Column('price', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('menu_id'),
    sa.UniqueConstraint('img')
    )
    op.create_table('staff',
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('img', sa.String(length=250), nullable=False),
    sa.Column('img_name', sa.Text(), nullable=False),
    sa.Column('mimetype', sa.Text(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('salary', sa.String(length=50), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('staff_id'),
    sa.UniqueConstraint('img')
    )
    op.create_table('order',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('table_number', sa.String(length=100), nullable=False),
    sa.Column('menu_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['menu.menu_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('staff')
    op.drop_table('menu')
    op.drop_table('auth')
    op.drop_table('admin')
    # ### end Alembic commands ###
