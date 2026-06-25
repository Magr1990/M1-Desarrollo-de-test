# Portafolio de QA: Ecosistema Web Club de Corredores VeloRaptors (Módulo 2)

Este repositorio contiene la evolución práctica de la estrategia de Aseguramiento de la Calidad (QA) y Pruebas Automatizadas para el bloque transaccional **T1 (MVP)** de la plataforma web de **VeloRaptors**, extendido para dar cumplimiento analítico a las directrices del **Módulo 2**.

El proyecto demuestra la aplicación de técnicas avanzadas de diseño de pruebas: clasificación de requerimientos, diseño exhaustivo de casos de prueba con formatos institucionales, partición de clases de equivalencia, análisis de valores límite (BVA) y planificación de pruebas de carga masiva en Python 3.x.

## 📈 Alcance de las Evaluaciones de este Hito (M2)
* **Historias de Usuario Cubiertas:**
  * **HU 1 (Carga masiva de carreras):** Clasificación analítica de requerimientos funcionales y no funcionales de rendimiento.
  * **HU 2 (Registro de Corredor):** Lógica perimetral para el control estricto de la regla de negocio de edad (mínimo 18 años y menor de 80 años) y unicidad de correo electrónico.
  * **HU 3 (Inscripción a Competencias):** Validación integral de flujos transaccionales cruzados con pasarela simulada de pago.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje Core:** Python 3.x
* **Framework de Testing:** `unittest` (Librería estándar nativa de Python)
* **Metodología:** Testing Ágil / Caja Negra y Caja Blanca Avanzada

## 📂 Estructura del Repositorio
* `codigo_sistema.py`: Backend lógico simulado bajo POO que implementa las restricciones de negocio actualizadas (control de edad, unicidad de cuentas y persistencia de tablas).
* `test_sistema.py`: Suite unificada de pruebas automatizadas que ejecutan escenarios de caminos felices, alternativos y de error (Edge Cases).

## 🚀 Cómo Ejecutar las Pruebas

1. Clona este repositorio en tu entorno local:
   ```bash
   git clone [https://github.com/Magr1990/M1-Desarrollo-de-test.git](https://github.com/Magr1990/M1-Desarrollo-de-test.git)