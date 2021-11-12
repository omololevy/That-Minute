"""empty message

Revision ID: c09adbc05033
Revises: 0cff78683986
Create Date: 2021-11-12 17:51:36.781234

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c09adbc05033'
down_revision = '0cff78683986'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('upvotes')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    op.drop_table('downvotes')
    op.drop_table('comments')
    op.drop_table('pitches')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('pitches_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('pitch', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='pitches_user_id_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='pitches_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('comments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='comments_pitch_id_fkey', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='comments_user_id_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='comments_pkey'),
    sa.UniqueConstraint('comment', name='comments_comment_key')
    )
    op.create_table('downvotes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('downvote_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='downvotes_pitch_id_fkey', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='downvotes_user_id_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='downvotes_pkey'),
    sa.UniqueConstraint('id', name='downvotes_id_key')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('bio', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    op.create_table('upvotes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('upvote_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='upvotes_pitch_id_fkey', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='upvotes_user_id_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='upvotes_pkey')
    )
    # ### end Alembic commands ###
