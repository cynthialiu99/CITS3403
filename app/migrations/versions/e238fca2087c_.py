"""empty message

Revision ID: e238fca2087c
Revises: 7872ed3710a2
Create Date: 2024-05-19 12:11:56.437452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e238fca2087c'
down_revision = '7872ed3710a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('committed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('committed')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.VARCHAR(length=500), nullable=False))

    # ### end Alembic commands ###
