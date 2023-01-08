"""Deletion uneeded columns from whois record

Revision ID: 45713fea8097
Revises: e04e8301d1a2
Create Date: 2020-12-07 12:36:04.818466

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# pylint: skip-file

# revision identifiers, used by Alembic.
revision = "45713fea8097"
down_revision = "e04e8301d1a2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("pyfunceble_whois_record", "state")
    op.drop_column("pyfunceble_whois_record", "record")
    op.drop_column("pyfunceble_whois_record", "server")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "pyfunceble_whois_record",
        sa.Column("server", mysql.TEXT(collation="utf8mb4_unicode_ci"), nullable=True),
    )
    op.add_column(
        "pyfunceble_whois_record",
        sa.Column("record", mysql.TEXT(collation="utf8mb4_unicode_ci"), nullable=True),
    )
    op.add_column(
        "pyfunceble_whois_record",
        sa.Column(
            "state",
            mysql.VARCHAR(collation="utf8mb4_unicode_ci", length=80),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###