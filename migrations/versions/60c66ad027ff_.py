"""empty message

Revision ID: 60c66ad027ff
Revises: 69d9496326d0
Create Date: 2022-02-21 13:59:12.930998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60c66ad027ff'
down_revision = '69d9496326d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_date', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('answer_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_comment_answer_id_answer'), 'answer', ['answer_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_comment_answer_id_answer'), type_='foreignkey')
        batch_op.drop_column('answer_id')
        batch_op.drop_column('create_date')

    # ### end Alembic commands ###