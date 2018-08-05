"""empty message

Revision ID: cccbd24f64bd
Revises: 81f0fb6d5582
Create Date: 2018-08-05 21:05:35.125085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cccbd24f64bd'
down_revision = '81f0fb6d5582'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('profile_setting_uniq', 'profile_setting', ['transport', 'setting', 'profile_id'])
    op.create_unique_constraint('scan_profile_uniq', 'scan_profile', ['name', 'owner_id'])
    op.create_unique_constraint('task_uniq', 'task', ['name', 'owner_id'])
    op.create_unique_constraint('task_setting_uniq', 'task_setting', ['hostname', 'profile_id', 'task_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('task_setting_uniq', 'task_setting', type_='unique')
    op.drop_constraint('task_uniq', 'task', type_='unique')
    op.drop_constraint('scan_profile_uniq', 'scan_profile', type_='unique')
    op.drop_constraint('profile_setting_uniq', 'profile_setting', type_='unique')
    # ### end Alembic commands ###