"""Add map_image column to zones

Revision ID: e6c44097184f
Revises: 3e127c4a099b
Create Date: 2024-07-15 19:44:09.564806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6c44097184f'
down_revision = '3e127c4a099b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('zone', schema=None) as batch_op:
        batch_op.add_column(sa.Column('map_image', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('zone', schema=None) as batch_op:
        batch_op.drop_column('map_image')

    # ### end Alembic commands ###
