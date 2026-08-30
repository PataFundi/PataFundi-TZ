"""user and refreshtoken

Revision ID: d3c4e033a0eb
Revises: f44cb2db6c18
Create Date: 2026-08-29 08:00:30.111031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3c4e033a0eb'
down_revision: Union[str, Sequence[str], None] = 'f44cb2db6c18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
