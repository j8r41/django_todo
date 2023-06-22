"""

Revision ID: dc4605a2c431
Revises: 
Create Date: 2023-06-22 10:15:36.756134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dc4605a2c431"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "accounts",
        sa.Column("user_id", sa.Integer, primary_key=True),
        sa.Column("telegram_auth_key", sa.VARCHAR(20)),
    )


def downgrade() -> None:
    op.drop_table("accounts")
