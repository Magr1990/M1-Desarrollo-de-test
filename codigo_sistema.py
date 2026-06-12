# -*- coding: utf-8 -*-
"""
Módulo del Sistema Web del Club de Corredores VeloRaptors.
Contiene la lógica de negocio correspondiente al hito T1.
"""

class Carrera:
    def __init__(self, id_carrera, nombre, distancia, costo):
        self.id_carrera = id_carrera
        self.nombre = nombre
        self.distancia = distancia  # Ejemplo: "10K", "21K"
        self.costo = costo

class Corredor:
    def __init__(self, email, password, nombre):
        self.email = email
        self.password = password
        self.nombre = nombre
        self.activo = True

class SistemaVeloRaptors:
    def __init__(self):
        self.usuarios = {}       # Llave: email, Valor: objeto Corredor
        self.carreras = {}       # Llave: id_carrera, Valor: objeto Carrera
        self.inscripciones = {}  # Llave: (email, id_carrera), Valor: Estado de Pago
        self.banners = []        # Lista de diccionarios de sponsors

    # --- MÓDULO DE CORREDORES ---
    def registrar_corredor(self, email, password, nombre):
        if not email or "@" not in email:
            return "Email inválido"
        if len(password) < 6:
            return "Contraseña demasiado corta"
        if email in self.usuarios:
            return "El corredor ya existe"
        
        nuevo_corredor = Corredor(email, password, nombre)
        self.usuarios[email] = nuevo_corredor
        return "Registro exitoso"

    def login_corredor(self, email, password):
        if email in self.usuarios:
            user = self.usuarios[email]
            if user.password == password:
                return True
        return False

    # --- MÓDULO DE CARRERAS ---
    def cargar_carrera_desde_sistema(self, id_carrera, nombre, distancia, costo):
        if costo < 0:
            return "Costo no puede ser negativo"
        nueva_carrera = Carrera(id_carrera, nombre, distancia, costo)
        self.carreras[id_carrera] = nueva_carrera
        return "Carrera cargada exitosamente"

    # --- MÓDULO DE INSCRIPCIÓN Y PAGOS ---
    def inscribir_en_carrera_con_pago(self, email, id_carrera, tarjeta_credito):
        # Validaciones de precondición
        if email not in self.usuarios:
            return "Usuario no registrado"
        if id_carrera not in self.carreras:
            return "Carrera no existente"
        if not tarjeta_credito or len(tarjeta_credito) != 16:
            return "Pago rechazado: Tarjeta inválida"
        
        # Simulación de transacción exitosa de pasarela
        self.inscripciones[(email, id_carrera)] = "Pagado"
        return "Inscripción exitosa"

    # --- MÓDULO DE SPONSORS / BANNERS ---
    def alta_banner(self, id_banner, sponsor_nombre):
        self.banners.append({"id": id_banner, "sponsor": sponsor_nombre})
        return "Banner agregado"

    def baja_banner(self, id_banner):
        for b in self.banners:
            if b["id"] == id_banner:
                self.banners.remove(b)
                return "Banner eliminado"
        return "Banner no encontrado"