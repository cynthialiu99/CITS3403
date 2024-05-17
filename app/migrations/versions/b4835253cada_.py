"""empty message

Revision ID: b4835253cada
Revises: 2d5ab562cdbb
Create Date: 2024-05-17 19:53:27.447695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4835253cada'
down_revision = '2d5ab562cdbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('response', schema=None) as batch_op:
        batch_op.drop_column('response_no')
        batch_op.drop_column('responder_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('response', schema=None) as batch_op:
        batch_op.add_column(sa.Column('responder_id', sa.VARCHAR(length=8), nullable=False))
        batch_op.add_column(sa.Column('response_no', sa.INTEGER(), nullable=False))

    # ### end Alembic commands ###
