"""new unique constraint

Revision ID: 660dada4fd37
Revises: aee03d3213e2
Create Date: 2023-11-02 01:27:42.168691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '660dada4fd37'
down_revision = 'aee03d3213e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('company_code',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.create_unique_constraint('primary_comapany_username', ['username', 'company_code'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('primary_comapany_username', type_='unique')
        batch_op.alter_column('company_code',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###