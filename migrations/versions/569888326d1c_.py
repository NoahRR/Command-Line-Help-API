"""empty message

Revision ID: 569888326d1c
Revises: 0ea4622b9ea5
Create Date: 2020-12-02 11:50:46.462650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '569888326d1c'
down_revision = '0ea4622b9ea5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hints', sa.Column('classification', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hints', 'classification')
    # ### end Alembic commands ###
