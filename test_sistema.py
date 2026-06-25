# -*- coding: utf-8 -*-
import unittest
from codigo_sistema import SistemaVeloRaptors

class TestSistemaVeloRaptorsM2(unittest.TestCase):

    def setUp(self):
        """Inicializa el entorno de prueba simulando pre-poblado de tablas."""
        self.sistema = SistemaVeloRaptors()
        # Usuario base para pruebas de login, duplicados e inscripción
        self.sistema.registrar_corredor("miguel@veloraptors.cl", "pass1234", "Miguel Ángel", 35)
        self.sistema.registrar_corredor("mario.qa@veloraptors.cl", "Run2026_!", "Mario", 34)
        self.sistema.cargar_carrera_desde_sistema("C1", "Maratón Santiago", "42K", 25000)

    # --- TEST ADAPTADOS DE LA ACTIVIDAD PRÁCTICA 2 ---
    
    def test_registrar_corredor_exitoso_m2(self):
        """Caso 1: Registro limpio de corredor válido."""
        resultado = self.sistema.registrar_corredor("nuevo.corredor@test.com", "PassValida_123", "Nuevo", 30)
        self.assertEqual(resultado, "Registro exitoso")
        self.assertIn("nuevo.corredor@test.com", self.sistema.usuarios)

    def test_registrar_corredor_duplicado_m2(self):
        """Caso 2: Validación de no duplicidad de correo electrónico."""
        resultado = self.sistema.registrar_corredor("miguel@veloraptors.cl", "Password_Test", "Miguel", 29)
        self.assertEqual(resultado, "El corredor ya existe")

    def test_registrar_corredor_edad_limite_inferior(self):
        """Caso 3: Validación del límite inferior de edad (Inválido menor de 18)."""
        resultado = self.sistema.registrar_corredor("joven@correo.com", "pass123", "Atleta Joven", 14)
        self.assertEqual(resultado, "Edad fuera del rango permitido")

    def test_registrar_corredor_edad_limite_superior(self):
        """Clase de equivalencia inválida: Mayor o igual a 80 años."""
        resultado = self.sistema.registrar_corredor("anciano@correo.com", "pass123", "Atleta Senior", 80)
        self.assertEqual(resultado, "Edad fuera del rango permitido")

    def test_registrar_corredor_edad_borde_valido(self):
        """Prueba de valor límite: 18 años exactos (Borde válido)."""
        resultado = self.sistema.registrar_corredor("borde.valido@correo.com", "pass123", "Justo 18", 18)
        self.assertEqual(resultado, "Registro exitoso")

    def test_inscripcion_con_pago_exitosa_m2(self):
        """Caso 4: Flujo completo feliz de inscripción y cobro."""
        resultado = self.sistema.inscribir_en_carrera_con_pago(
            "mario.qa@veloraptors.cl", "C1", "1234567812345678"
        )
        self.assertEqual(resultado, "Inscripción exitosa")
        self.assertEqual(self.sistema.inscripciones[("mario.qa@veloraptors.cl", "C1")], "Pagado")

    def test_inscripcion_usuario_no_registrado_m2(self):
        """Caso 5: Control de seguridad de inyección en inscripciones."""
        resultado = self.sistema.inscribir_en_carrera_con_pago(
            "anonimo@correo.com", "C1", "1234567812345678"
        )
        self.assertEqual(resultado, "Usuario no registrado")

if __name__ == '__main__':
    unittest.main()