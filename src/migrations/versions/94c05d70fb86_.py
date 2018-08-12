"""empty message

Revision ID: 94c05d70fb86
Revises: a7fb8f08a32c
Create Date: 2018-08-12 15:39:08.401129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94c05d70fb86'
down_revision = 'a7fb8f08a32c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task_result', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('task_fk', 'task_result', 'user', ['owner_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('task_fk', 'task_result', type_='foreignkey')
    op.drop_column('task_result', 'owner_id')
    # ### end Alembic commands ###
