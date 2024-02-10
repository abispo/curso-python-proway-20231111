"""empty message

Revision ID: 5eb4d19dbe15
Revises: f8d6744df2c8
Create Date: 2024-02-10 18:04:46.937922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5eb4d19dbe15'
down_revision: Union[str, None] = 'f8d6744df2c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_clientes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=300), nullable=False),
    sa.Column('tipo_logradouro', sa.String(length=20), nullable=False),
    sa.Column('logradouro', sa.String(length=200), nullable=False),
    sa.Column('numero', sa.String(length=10), nullable=False),
    sa.Column('bairro', sa.String(length=100), nullable=False),
    sa.Column('cidade', sa.String(length=100), nullable=False),
    sa.Column('uf', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_clientes')
    # ### end Alembic commands ###
