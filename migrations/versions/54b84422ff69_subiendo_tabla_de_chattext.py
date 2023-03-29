"""subiendo tabla de chattext

Revision ID: 54b84422ff69
Revises: eb12ca5059e7
Create Date: 2023-03-29 14:22:11.330301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54b84422ff69'
down_revision = 'eb12ca5059e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chatusers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('text', sa.String(length=120), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chatusers')
    # ### end Alembic commands ###