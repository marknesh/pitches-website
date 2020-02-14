"""SSSS

Revision ID: b974c0a078ad
Revises: 2ba0a57f790e
Create Date: 2020-02-13 10:48:59.834175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b974c0a078ad'
down_revision = '2ba0a57f790e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('person_pitch_id_fkey', 'person', type_='foreignkey')
    op.drop_column('person', 'pitch_id')
    op.add_column('pitched', sa.Column('user_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitched', 'user_id')
    op.add_column('person', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('person_pitch_id_fkey', 'person', 'pitched', ['pitch_id'], ['id'])
    # ### end Alembic commands ###
