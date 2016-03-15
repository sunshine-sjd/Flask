"""empty message

Revision ID: 8476653ef090
Revises: 189ba0923a6f
Create Date: 2016-03-14 21:37:58.658000

"""

# revision identifiers, used by Alembic.
revision = '8476653ef090'
down_revision = '189ba0923a6f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role_table', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('role_table', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_role_table_default'), 'role_table', ['default'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_role_table_default'), table_name='role_table')
    op.drop_column('role_table', 'permissions')
    op.drop_column('role_table', 'default')
    ### end Alembic commands ###