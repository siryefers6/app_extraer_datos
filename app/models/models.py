from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone

class TextoProcesado(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    texto_original: str = Field(unique=True)  # ⚠️ Campo único
    rut: Optional[str] = None
    pedidos: Optional[str] = None
    guias: Optional[str] = None
    facturas: Optional[str] = None
    ordenes: Optional[str] = None
    ccosto: Optional[str] = None
    vendedores: Optional[str] = None
    montos: Optional[str] = None
    glosas: Optional[str] = None
    fpago: Optional[str] = None
    procesado_en: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
