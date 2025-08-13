from app.models.datos_texto import DatosTexto

def test_obtener_rut():
    """
    Prueba la correcta extracción de los rut de un texto.
    """
    # Arrange
    texto = '24405907-4 ruben 24,219,980-4 miriam 24.803.784-9 y $100.000 pesos'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.rut

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['24405907', '24219980', '24803784']

def test_obtener_rut_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.rut

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_pedidos():
    """
    Prueba la correcta extracción de los pedidos de un texto.
    """
    # Arrange
    texto = '32222145 pedido 1: 31111145 pedido 1: 33333145'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.pedidos

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['32222145', '31111145', '33333145']

def test_obtener_pedidos_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.pedidos

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_guias():
    """
    Prueba la correcta extracción de las guías de un texto.
    """
    # Arrange
    texto = '5438847 guia 2  5438706 guia3 5438461 5438461- $ 5.438.464'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.guias

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['5438847', '5438706', '5438461']

def test_obtener_guias_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.guias

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_facturas():
    """
    Prueba la correcta extracción de las facturas de un texto.
    """
    # Arrange
    texto = '13826067 13826068 13826068- 13826069 $13826069'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.facturas

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['13826067', '13826068', '13826069']

def test_obtener_facturas_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.facturas

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_ordenes_compras():
    """
    Prueba la correcta extracción de las ordenes de compra de un texto.
    """
    # Arrange
    texto = 'OO19 OO  asdfkj23411234  ooyefersonbermúdez'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.ordenes

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['19', 'ASDFKJ23411234', 'YEFERSONBERMUDEZ']

def test_obtener_ordenes_compras_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.ordenes

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_ccosto():
    """
    Prueba la correcta extracción de los centros de costo de un texto.
    """
    # Arrange
    texto = 'cc19 cc  0  CC8 cc 09209 $9'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.ccosto

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['19', '0', '8']

def test_obtener_ccosto_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.ccosto

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_cod_vendedores():
    """
    Prueba la correcta extracción de los códigos de vendedores de un texto.
    """
    # Arrange
    texto = 'vv19 VV  8  vv918 vv 09209 vv $989'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.vendedores

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['19', '8', '918']

def test_obtener_cod_vendedores_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.vendedores

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_montos():
    """
    Prueba la correcta extracción de los montos de un texto.
    """
    # Arrange
    texto = '$ 19 $  108.934  $918.000- $w1993'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.montos

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['19', '108934', '918000']

def test_obtener_montos_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.montos

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_glosas():
    """
    Prueba la correcta extracción de las glosas de un texto.
    """
    # Arrange
    texto = '* Rebate     Q1 2025* otra glosa *mermas Q4  2025 facturación* * publicidad Q2    2025*'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.glosas

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['REBATE Q1 2025', 'MERMAS Q4 2025 FACTURACION', 'PUBLICIDAD Q2 2025']

def test_obtener_glosas_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.glosas

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_formas_pago():
    """
    Prueba la correcta extracción de las formas de pago de un texto.
    """
    # Arrange
    texto = ' ff90 ff30 ff7 1'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.fpago

    # Assert
    assert isinstance(resultado, list)
    assert resultado == ['90', '30', '7']

def test_obtener_formas_pago_cadena_vacia():
    """
    Prueba que retorne lista vacía con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.fpago

    # Assert
    assert isinstance(resultado, list)
    assert resultado == []

def test_obtener_cantidad_resultados():
    """
    Prueba la correcta obtención de la cantidad de resultados de un texto.
    """
    # Arrange
    texto = ' ff90 ff30 ff7 1 vv9 oo123 *glosa*'
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.cantidad_resultados

    # Assert
    assert isinstance(resultado, int)
    assert resultado == 6

def test_obtener_cantidad_resultados_cadena_vacia():
    """
    Prueba que retorne 0 con un texto vacío.
    """
    # Arrange
    texto = ''
    datos_texto = DatosTexto(texto)

    # Act
    resultado = datos_texto.cantidad_resultados

    # Assert
    assert isinstance(resultado, int)
    assert resultado == 0

