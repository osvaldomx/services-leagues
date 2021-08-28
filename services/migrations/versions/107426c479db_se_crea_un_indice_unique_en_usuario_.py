"""Se crea un indice UNIQUE en Usuario.email

Revision ID: 107426c479db
Revises: 68283d874e2b
Create Date: 2021-08-26 23:36:32.702366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107426c479db'
down_revision = '68283d874e2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('usuario', 'email',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.create_unique_constraint(None, 'usuario', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'usuario', type_='unique')
    op.alter_column('usuario', 'email',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###
