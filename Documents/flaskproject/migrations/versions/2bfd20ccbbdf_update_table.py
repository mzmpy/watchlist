"""update table

Revision ID: 2bfd20ccbbdf
Revises: 4a98bf00647f
Create Date: 2019-09-06 14:06:57.913400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bfd20ccbbdf'
down_revision = '4a98bf00647f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('is_free', sa.Boolean(), nullable=True))
    op.drop_index('ix_file_source_filename', table_name='file')
    op.create_index(op.f('ix_file_source_filename'), 'file', ['source_filename'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_file_source_filename'), table_name='file')
    op.create_index('ix_file_source_filename', 'file', ['source_filename'], unique=1)
    op.drop_column('file', 'is_free')
    # ### end Alembic commands ###
