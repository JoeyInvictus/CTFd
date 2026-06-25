"""Rename scenario_id to scenario in dynamic_ia_c_challenge

Revision ID: a1b2c3d4e5f6
Revises: 67ebab6de598
Create Date: 2026-06-24 00:00:00.000000

"""
from alembic import op


revision = "a1b2c3d4e5f6"
down_revision = "67ebab6de598"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("dynamic_ia_c_challenge", "scenario_id", new_column_name="scenario")


def downgrade():
    op.alter_column("dynamic_ia_c_challenge", "scenario", new_column_name="scenario_id")
