"""empty message

Revision ID: 78a44fac209e
Revises: ba53b34f8f03
Create Date: 2019-05-06 16:56:26.639179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78a44fac209e'
down_revision = 'ba53b34f8f03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscriber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('subscription_info', sa.String(length=2000), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('device_id', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscriber_created'), 'subscriber', ['created'], unique=False)
    op.create_index(op.f('ix_subscriber_modified'), 'subscriber', ['modified'], unique=False)
    op.add_column('device', sa.Column('ir_led', sa.Integer(), nullable=True))
    op.add_column('device', sa.Column('update_period', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('device', 'update_period')
    op.drop_column('device', 'ir_led')
    op.drop_index(op.f('ix_subscriber_modified'), table_name='subscriber')
    op.drop_index(op.f('ix_subscriber_created'), table_name='subscriber')
    op.drop_table('subscriber')
    # ### end Alembic commands ###