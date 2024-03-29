"""new column companyname

Revision ID: aee03d3213e2
Revises: 
Create Date: 2023-11-02 00:47:59.372462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aee03d3213e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    op.drop_table('requests')
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_name', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.drop_column('company_name')

    op.create_table('requests',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sender', sa.INTEGER(), nullable=False),
    sa.Column('receiver', sa.INTEGER(), nullable=False),
    sa.Column('request_tag', sa.TEXT(), nullable=True),
    sa.Column('info', sa.TEXT(), nullable=True),
    sa.Column('approval', sa.BOOLEAN(), nullable=True),
    sa.Column('comments', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sender', sa.INTEGER(), nullable=False),
    sa.Column('receiver', sa.INTEGER(), nullable=False),
    sa.Column('msg_type', sa.TEXT(), nullable=True),
    sa.Column('msg', sa.TEXT(), nullable=True),
    sa.Column('read', sa.BOOLEAN(), nullable=True),
    sa.Column('send_time', sa.DATETIME(), nullable=True),
    sa.Column('read_time', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
