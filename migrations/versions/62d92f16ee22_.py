"""empty message

Revision ID: 62d92f16ee22
Revises: 
Create Date: 2021-11-09 23:01:23.880333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62d92f16ee22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'downvotes', ['id'])
    op.create_unique_constraint(None, 'upvotes', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'upvotes', type_='unique')
    op.drop_constraint(None, 'downvotes', type_='unique')
    # ### end Alembic commands ###
