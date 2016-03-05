"""empty message

Revision ID: c4a05a4b98d8
Revises: None
Create Date: 2016-03-05 13:29:40.380000

"""

# revision identifiers, used by Alembic.
revision = 'c4a05a4b98d8'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('RoleName', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('RoleName')
    )
    op.create_table('user_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('UserName', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_table_UserName'), 'user_table', ['UserName'], unique=True)
    op.create_index(op.f('ix_user_table_email'), 'user_table', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_table_email'), table_name='user_table')
    op.drop_index(op.f('ix_user_table_UserName'), table_name='user_table')
    op.drop_table('user_table')
    op.drop_table('role_table')
    ### end Alembic commands ###
