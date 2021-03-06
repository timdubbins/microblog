"""followers

Revision ID: 670e557b469d
Revises: 6ee3c84611ba
Create Date: 2020-10-10 16:42:33.279257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '670e557b469d'
down_revision = '6ee3c84611ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follows')
    # ### end Alembic commands ###
