"""Initial migration

Revision ID: 20240812184546_6d16b920a3ec
Revises:
Create Date: 2024-08-12 18:45:46.599604

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "20240812184546_6d16b920a3ec"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("uid", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("display_name", sa.String(length=255), nullable=True),
        sa.Column("email_verified", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("last_login_at", sa.TIMESTAMP(), nullable=True),
        sa.Column(
            "provider_info", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("provider_username", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("uid"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
