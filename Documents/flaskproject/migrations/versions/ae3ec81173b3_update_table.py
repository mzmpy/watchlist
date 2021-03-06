"""update table

Revision ID: ae3ec81173b3
Revises: 2bfd20ccbbdf
Create Date: 2019-09-06 14:11:04.346840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae3ec81173b3'
down_revision = '2bfd20ccbbdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'file', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'file', type_='foreignkey')
    op.drop_column('file', 'user_id')
    # ### end Alembic commands ###
