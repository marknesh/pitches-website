"""empty message

Revision ID: eab9c08d5bdd
Revises: fbf5d31ee1d9
Create Date: 2020-02-14 09:19:40.877432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eab9c08d5bdd'
down_revision = 'fbf5d31ee1d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'pitched', ['pitch_id'], ['id'])
    op.drop_constraint('pitched_user_id_fkey', 'pitched', type_='foreignkey')
    op.drop_column('pitched', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitched', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('pitched_user_id_fkey', 'pitched', 'person', ['user_id'], ['id'])
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###
