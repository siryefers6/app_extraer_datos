from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.models.datos_texto import DatosTexto
from sqlmodel import Session
from app.models.models import TextoProcesado
from app.database import get_session, init_db
from sqlalchemy.exc import IntegrityError
from contextlib import asynccontextmanager  # ✅ nuevo import

# 🔄 Reemplazo del startup con lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    # Aquí podrías cerrar conexiones si lo necesitas

# ⬇️ Pasa el lifespan al instanciar la app
app = FastAPI(lifespan=lifespan)

# Montar la carpeta /dist como carpeta estática
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def pagina_principal(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/guardar_resultado", response_class=HTMLResponse)
def guardar_resultado(request: Request, texto: str = Form(...), session: Session = Depends(get_session)):
    dt = DatosTexto(texto)

    if dt.cantidad_resultados == 0:
        mensaje = 'No hay información extraída, no se guardó nada.'
        return templates.TemplateResponse(
            "confirmacion.html",
            {"request": request, "mensaje": mensaje}
        )

    nuevo = TextoProcesado(
        texto_original=texto,
        rut=",".join(dt.rut),
        pedidos=",".join(dt.pedidos),
        guias=",".join(dt.guias),
        facturas=",".join(dt.facturas),
        ordenes=",".join(dt.ordenes),
        ccosto=",".join(dt.ccosto),
        vendedores=",".join(dt.vendedores),
        montos=",".join(dt.montos),
        glosas=",".join(dt.glosas),
        fpago=",".join(dt.fpago),
    )

    try:
        session.add(nuevo)
        session.commit()
        session.refresh(nuevo)
        mensaje = "✅ Resultado guardado correctamente"
    except IntegrityError:
        session.rollback()
        mensaje = "⚠️ Este texto ya ha sido guardado anteriormente"

    return templates.TemplateResponse(
        "confirmacion.html",
        {"request": request, "mensaje": mensaje}
    )


@app.post("/extraer_rut")
def extraer_rut(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.rut
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "RUT"},
    )


@app.post("/extraer_pedidos")
def extraer_pedidos(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.pedidos
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "PEDIDOS"},
    )


@app.post("/extraer_guias")
def extraer_guias(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.guias
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "GUIAS"},
    )


@app.post("/extraer_facturas")
def extraer_facturas(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.facturas
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "FACTURAS"},
    )


@app.post("/extraer_ordenes")
def extraer_ordenes(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.ordenes
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "ORDENES"},
    )


@app.post("/extraer_ccosto")
def extraer_ccosto(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.ccosto
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "C.COSTO"},
    )


@app.post("/extraer_vendedores")
def extraer_cod_vendedores(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.vendedores
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "VENDEDORES"},
    )


@app.post("/extraer_montos")
def extraer_montos(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.montos
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "MONTOS"},
    )


@app.post("/extraer_glosas")
def extraer_glosas(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.glosas
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "GLOSAS"},
    )


@app.post("/extraer_fpago")
def extraer_fpago(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    resultado = datos_texto.fpago
    return templates.TemplateResponse(
        "resultado.html",
        {"request": request, "resultado": resultado, "titulo_resultado": "F.PAGO"},
    )


@app.post("/extraer_all_resultados")
def extraer_fpago(request: Request, texto: str = Form(...)):
    datos_texto = DatosTexto(texto)
    return templates.TemplateResponse(
        "all_resultados.html",
        {"request": request, "datos_texto": datos_texto, "len_texto": len(texto)},
    )
