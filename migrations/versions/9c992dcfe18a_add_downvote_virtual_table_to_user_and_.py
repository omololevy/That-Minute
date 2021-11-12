"""add downvote virtual table to user and pitch tables

Revision ID: 9c992dcfe18a
Revises: 607e5eb79b5e
Create Date: 2021-04-26 21:06:41.441701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c992dcfe18a'
down_revision = '607e5eb79b5e'
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
