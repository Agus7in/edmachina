"""Agregar IDs autoincrementales

Revision ID: b06beb837bb1
Revises: 0997eedde53d
Create Date: 2024-08-31 20:00:03.921348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b06beb837bb1'
down_revision: Union[str, None] = '0997eedde53d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('carreras', 'nombre_carrera',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('inscripciones', 'lead_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('inscripciones', 'materia_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('inscripciones', 'carrera_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('inscripciones', 'anio_inscripcion',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('inscripciones', 'nro_veces_cursada',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('inscripciones', 'tiempo_cursado',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('leads', 'nombre_completo',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('leads', 'direccion',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('leads', 'telefono',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('leads', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('materias', 'nombre_materia',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('materias', 'nombre_materia',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('leads', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('leads', 'telefono',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('leads', 'direccion',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('leads', 'nombre_completo',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('inscripciones', 'tiempo_cursado',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('inscripciones', 'nro_veces_cursada',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('inscripciones', 'anio_inscripcion',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('inscripciones', 'carrera_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('inscripciones', 'materia_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('inscripciones', 'lead_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('carreras', 'nombre_carrera',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
