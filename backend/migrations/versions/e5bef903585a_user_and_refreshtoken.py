"""user and refreshtoken

Revision ID: e5bef903585a
Revises: d3c4e033a0eb
Create Date: 2026-08-29 08:02:14.413577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5bef903585a'
down_revision: Union[str, Sequence[str], None] = 'd3c4e033a0eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
