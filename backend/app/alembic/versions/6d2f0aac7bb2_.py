"""

Revision ID: 6d2f0aac7bb2
Revises: bf7d0f5be7d2
Create Date: 2020-06-28 16:43:56.168682

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6d2f0aac7bb2'
down_revision = 'bf7d0f5be7d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_group_menu_id', table_name='group_menu')
    op.drop_table('group_menu')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group_menu',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('group_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('menu_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('group_key', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], name='group_menu_ibfk_1'),
    sa.ForeignKeyConstraint(['menu_id'], ['menu.id'], name='group_menu_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_group_menu_id', 'group_menu', ['id'], unique=False)
    # ### end Alembic commands ###
