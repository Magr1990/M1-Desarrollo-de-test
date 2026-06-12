# Portafolio de QA: Web Club de Corredores VeloRaptors 🏃‍♂️🦖

Este repositorio contiene el **Plan Preliminar de Pruebas** y la implementación base del backend para el **Hito T1 (MVP)** del ecosistema web del Club de Corredores VeloRaptors.

El proyecto fue desarrollado como parte del curso de **Desarrollo de Test / Aseguramiento de Calidad**, demostrando la aplicación práctica de metodologías ágiles, diseño de casos de prueba y automatización con Python.

## 🎯 Alcance del Proyecto (Hito T1)
El Producto Mínimo Viable (MVP) construido y testeado en esta fase incluye el núcleo transaccional del sistema:
- **Módulo de Corredores:** Registro seguro, validación de credenciales y login.
- **Módulo de Carreras:** Carga de eventos deportivos al sistema.
- **Pasarela de Pagos:** Inscripción a carreras con validación simulada de tarjetas de crédito.
- **Módulo de Sponsors:** Gestión (Alta/Baja) de banners publicitarios.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Testing:** `unittest` (Librería estándar de Python)
- **Control de Versiones:** Git & GitHub

## 📂 Estructura del Repositorio
- `codigo_sistema.py`: Contiene la lógica de negocio y la programación orientada a objetos que simula el backend de la plataforma web.
- `test_sistema.py`: Suite de pruebas automatizadas (Caja Blanca/Caja Negra) diseñadas por el rol de QA para validar el código, incluyendo caminos felices y de error (Edge Cases).

## 🚀 Cómo ejecutar las pruebas

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Magr1990/M1-Desarrollo-de-test.git
   ```
2. Navega a la carpeta del proyecto:
   ```bash
   cd "M1 Desarrollo de test"
   ```
3. Ejecuta la suite de pruebas desde la terminal:
   ```bash
   python test_sistema.py
   ```

### Salida esperada
Si el entorno está configurado correctamente, verás una salida indicando que todas las pruebas pasaron exitosamente (`OK`), lo que asegura la calidad y no regresión del código.

## 📋 Criterios de Calidad Aplicados
- **Prevención de regresión:** Se validan módulos independientemente para asegurar escalabilidad hacia las fases T2, T3 y T4.
- **Cobertura de errores:** Pruebas contra contraseñas cortas, correos inválidos, costos negativos y tarjetas de crédito rechazadas.

---
*Desarrollado para el Instituto Profesional IPP.*