"""

Revision ID: 4f9c650647ae
Revises: e2c18ef24967
Create Date: 2020-07-13 11:01:30.349594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f9c650647ae'
down_revision = 'e2c18ef24967'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['department.id'], ),
    sa.ForeignKeyConstraint(['status'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_department_id'), 'department', ['id'], unique=False)
    op.create_index(op.f('ix_department_parent_id'), 'department', ['parent_id'], unique=False)
    op.create_index(op.f('ix_department_status'), 'department', ['status'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_department_status'), table_name='department')
    op.drop_index(op.f('ix_department_parent_id'), table_name='department')
    op.drop_index(op.f('ix_department_id'), table_name='department')
    op.drop_table('department')
    # ### end Alembic commands ###
