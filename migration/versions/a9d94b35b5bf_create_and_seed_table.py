"""create and seed table

Revision ID: a9d94b35b5bf
Revises: 
Create Date: 2023-02-22 20:54:03.632873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9d94b35b5bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("DROP TABLE IF EXISTS items")

    op.create_table(
        "items",
        sa.Column("id", sa.Integer, sa.Identity(start=1, increment=1), primary_key=True),
        sa.Column("item_name", sa.String(255), nullable=False)
    )

    op.execute("INSERT INTO items (item_name) VALUES ('test item')")
    op.execute("INSERT INTO items (item_name) VALUES ('test item 2')")
    pass


def downgrade() -> None:
    op.execute("DROP TABLE items")
    pass
