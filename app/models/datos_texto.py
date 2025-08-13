import re

class DatosTexto:
    def __init__(self, texto: str):
        self.texto = texto
        self.texto_formateado = re.sub(r'[.,]', '', texto).upper().strip()
        self.texto_sin_dobles_espacios = re.sub('\s+', ' ', texto).upper().strip()
        self.texto_sin_glosas = re.sub(r'\*([^*]+?)\*', '', self.texto).upper().strip()
        self.texto_formateado_sin_glosas = re.sub(r'\*([^*]+?)\*', '', self.texto_formateado).upper().strip()
        self.rut = self.get_rut()
        self.pedidos = self.get_pedidos()
        self.guias = self.get_guias()
        self.facturas = self.get_facturas()
        self.ordenes = self.get_ordenes_compras()
        self.ccosto = self.get_ccosto()
        self.vendedores = self.get_cod_vendedores()
        self.montos = self.get_montos()
        self.glosas = self.get_glosas()
        self.fpago = self.get_fpago()
        self.resultados = []

    def get_rut(self) -> list:
        texto = self.texto_formateado_sin_glosas
        patron = r'(?<!\$)\s*\b(\d{7,8})-'
        return re.findall(patron, texto)

    def get_pedidos(self) -> list:
        texto = self.texto_sin_glosas
        patron = r'(?<!\$)\s*\b(3\d{7})\b(?!-)'
        return re.findall(patron, texto)

    def get_guias(self) -> list:
        texto = self.texto_sin_glosas
        patron = r'(?<!\$)\s*\b(5\d{6})\b(?!-)'
        return re.findall(patron, texto)

    def get_facturas(self) -> list:
        texto = self.texto_sin_glosas
        patron = r'(?<!\$)\s*\b(1[234]\d{6})\b(?!-)'
        return re.findall(patron, texto)

    def get_ordenes_compras(self) -> list:
        texto = self.texto_sin_dobles_espacios
        texto_sin_acentos = texto.translate(str.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU'))
        patron = r'OO\s*([^\s]{1,20})\b'
        return re.findall(patron, texto_sin_acentos)

    def get_ccosto(self) -> list:
        texto = self.texto_sin_dobles_espacios
        patron = r'CC\s*(\d{1,4})\b(?!-)'
        return re.findall(patron, texto)

    def get_cod_vendedores(self) -> list:
        texto = self.texto_sin_dobles_espacios
        patron = r'VV\s*(\d{1,3})\b(?!-)'
        return re.findall(patron, texto)

    def get_montos(self) -> list:
        texto = self.texto_formateado_sin_glosas
        patron = r'\$\s*(\d{1,10})\b'
        return re.findall(patron, texto)

    def get_glosas(self) -> list:
        texto = self.texto_sin_dobles_espacios
        texto_sin_acentos = texto.translate(str.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU'))
        patron = r'\*([^*]+?)\*'
        glosas: str = re.findall(patron, texto_sin_acentos)
        return [glosa.strip() for glosa in glosas]

    def get_fpago(self) -> list:
        texto = self.texto_formateado_sin_glosas
        patron = r'FF\s*(\d{1,2})\b'
        return re.findall(patron, texto)



