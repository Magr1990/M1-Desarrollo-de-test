# -*- coding: utf-8 -*-
import unittest
from codigo_sistema import SistemaVeloRaptors

class TestSistemaVeloRaptorsT1(unittest.TestCase):

    def setUp(self):
        """Inicializa el entorno de prueba antes de cada test."""
        self.sistema = SistemaVeloRaptors()
        # Pre-poblar datos requeridos comunes
        self.sistema.registrar_corredor("miguel@veloraptors.cl", "pass1234", "Miguel Ángel")
        self.sistema.cargar_carrera_desde_sistema("C1", "Maratón Santiago", "42K", 25000)

    # --- TEST DE REGISTRO Y SEGURIDAD ---
    def test_registrar_corredor_exitoso(self):
        resultado = self.sistema.registrar_corredor("juan@correo.com", "secure99", "Juan Pérez")
        self.assertEqual(resultado, "Registro exitoso")
        self.assertIn("juan@correo.com", self.sistema.usuarios)

    def test_registrar_corredor_password_corto(self):
        resultado = self.sistema.registrar_corredor("test@correo.com", "123", "Prueba")
        self.assertEqual(resultado, "Contraseña demasiado corta")

    def test_registrar_corredor_existente(self):
        resultado = self.sistema.registrar_corredor("miguel@veloraptors.cl", "nuevapass", "Miguel Otro")
        self.assertEqual(resultado, "El corredor ya existe")

    def test_registrar_corredor_email_invalido(self):
        resultado = self.sistema.registrar_corredor("correo_sin_arroba.com", "pass1234", "Sin Arroba")
        self.assertEqual(resultado, "Email inválido")

    def test_login_exitoso(self):
        resultado = self.sistema.login_corredor("miguel@veloraptors.cl", "pass1234")
        self.assertTrue(resultado)

    def test_login_fallido_password_incorrecto(self):
        resultado = self.sistema.login_corredor("miguel@veloraptors.cl", "erronea")
        self.assertFalse(resultado)

    def test_login_fallido_usuario_inexistente(self):
        resultado = self.sistema.login_corredor("fantasma@veloraptors.cl", "pass1234")
        self.assertFalse(resultado)

    # --- TEST DE MODULO CARRERAS ---
    def test_cargar_carrera_costo_negativo(self):
        resultado = self.sistema.cargar_carrera_desde_sistema("C2", "Carrera Gratis Error", "10K", -500)
        self.assertEqual(resultado, "Costo no puede ser negativo")

    # --- TEST DE PASARELA DE PAGOS E INSCRIPCIONES ---
    def test_inscripcion_con_pago_exitosa(self):
        resultado = self.sistema.inscribir_en_carrera_con_pago(
            "miguel@veloraptors.cl", "C1", "1234567812345678"
        )
        self.assertEqual(resultado, "Inscripción exitosa")
        self.assertEqual(self.sistema.inscripciones[("miguel@veloraptors.cl", "C1")], "Pagado")

    def test_inscripcion_pago_fallido_tarjeta_invalida(self):
        resultado = self.sistema.inscribir_en_carrera_con_pago(
            "miguel@veloraptors.cl", "C1", "123"  # Menos de 16 dígitos
        )
        self.assertEqual(resultado, "Pago rechazado: Tarjeta inválida")

    # --- TEST DE REGRESIÓN DE BANNERS (CRUD) ---
    def test_gestion_banners_alta_y_baja(self):
        self.sistema.alta_banner(101, "Sponsor Nike")
        self.assertEqual(len(self.sistema.banners), 1)
        
        self.sistema.baja_banner(101)
        self.assertEqual(len(self.sistema.banners), 0)

    def test_baja_banner_no_encontrado(self):
        resultado = self.sistema.baja_banner(999)
        self.assertEqual(resultado, "Banner no encontrado")

if __name__ == '__main__':
    unittest.main()