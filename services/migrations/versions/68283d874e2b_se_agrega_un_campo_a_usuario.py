"""Se agrega un campo a Usuario

Revision ID: 68283d874e2b
Revises: 
Create Date: 2021-08-26 22:33:08.853914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68283d874e2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('contrasena', sa.String(length=20), nullable=False, server_default='123'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'contrasena')
    # ### end Alembic commands ###