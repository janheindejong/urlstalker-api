"""Create resources and snapshots tables

Revision ID: 37c7847fa871
Revises: 
Create Date: 2022-02-08 19:37:38.691184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37c7847fa871'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'resources',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('path', sa.String, nullable=False),
    )

    op.create_table(
        'snapshots',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('datetime', sa.DateTime, nullable=False),
        sa.Column('status_code', sa.Integer, nullable=False),
        sa.Column('response', sa.String, nullable=False),
        sa.Column('resource_id', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('resources')
    op.drop_table('snapshots')
