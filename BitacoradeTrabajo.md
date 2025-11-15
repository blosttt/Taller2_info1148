# Bitácora de Trabajo – Tarea 2 - INFO1148

**Período de Trabajo:** 4 al 15 de noviembre de 2025  
**Fecha de Entrega:** 15 de noviembre de 2025  

---

## Información del Proyecto

- **Título:** Análisis Comparativo de Algoritmos de Ordenamiento  
- **Integrantes:** Benjamin Sobarzo, Kevin Cortes, Jonathan Huinca  
- **Asignatura:** INFO1148  
- **Semestre:** II-2025  
- **Repositorio:** [https://github.com/blosttt/Taller2.info1148](https://github.com/blosttt/Taller2.info1148)  

---

## Distribución Inicial de Tareas

| Integrante        | Responsabilidades Principales                     |
|-------------------|---------------------------------------------------|
| Benjamin Sobarzo  | Implementación de algoritmos y sistema de medición |
| Kevin Cortes      | Diseño experimental y análisis de resultados      |
| Jonathan Huinca   | Documentación y preparación de informe            |

---

## Cronología de Actividades

### 4 de noviembre – Inicio del Proyecto (12:00 hrs)

- Reunión inicial del equipo para planificación del trabajo  
- Distribución de tareas y responsabilidades  
- Definición de objetivos y alcance del proyecto  
- Establecimiento de cronograma con hitos específicos  

### 5-6 de noviembre – Fase de Investigación y Diseño

- Investigación teórica sobre complejidad algorítmica  
- Diseño del experimento con los siguientes parámetros:  
  - **Tamaños de entrada:** 100, 500, 1000, 2000, 3000  
  - **Tipos de datos:** aleatorios, ordenados, inversos  
  - **Métricas:** tiempo de ejecución en milisegundos  
- Planificación de la implementación en Python  

### 7-9 de noviembre – Implementación de Algoritmos

- Desarrollo de los tres algoritmos de ordenamiento:  
  - `quicksort.py` – Implementación con pivote central  
  - `mergesort.py` – Algoritmo divide y vencerás estable  
  - `bubblesort.py` – Versión optimizada con detección de intercambios  
- Pruebas unitarias de cada implementación  
- Verificación de corrección con diferentes conjuntos de datos  

### 10-12 de noviembre – Sistema de Medición y Pruebas

- Desarrollo del archivo `comparacion.py`  
- Implementación de la clase `AlgorithmBenchmark`  
- Sistema de medición de tiempos con `time.perf_counter()`  
- Módulo de generación automática de gráficos con **matplotlib**  
- Ejecución de pruebas preliminares y ajuste de parámetros  

### 13-14 de noviembre – Ejecución de Experimentos

- Ejecución sistemática de todos los casos de prueba  
- Recolección de datos para los tres algoritmos en todos los escenarios  
- Generación de tablas y gráficos comparativos  
- Análisis inicial de resultados obtenidos  

### 15 de noviembre – Finalización y Entrega (12:00 hrs)

- Análisis detallado de resultados experimentales  
- Comparación con predicciones teóricas de complejidad  
- Elaboración del informe técnico completo  
- Revisión final del código y documentación  
- Integración de todos los componentes del proyecto  
- **Entrega final del trabajo completo**  

---

## Hitos Principales Alcanzados

| Fecha   | Hito                                          | Estado |
|---------|-----------------------------------------------|--------|
| 4 nov   | Planificación completa del proyecto           | ✅     |
| 7 nov   | Implementación de los tres algoritmos         | ✅     |
| 10 nov  | Sistema de medición funcional                 | ✅     |
| 13 nov  | Ejecución completa de experimentos            | ✅     |
| 15 nov  | Análisis, documentación y entrega final       | ✅     |

---

## Recursos Utilizados

### Tecnológicos

- **Lenguaje:** Python 3.x  
- **Bibliotecas:** matplotlib, numpy, statistics, time  
- **Entorno:** Multiplataforma (Windows/Linux/macOS)  
- **Repositorio:** GitHub  

### Metodológicos

- **Enfoque:** Investigación aplicada con validación experimental  
- **Métricas:** Tiempo de ejecución con múltiples repeticiones  
- **Validación:** Contrastación teoría-práctica  

---

## Estructura del Proyecto Entregado
Tarea2_Algoritmos/
├── quicksort.py
├── mergesort.py
├── bubblesort.py
├── comparacion.py
├── TA_2_INFO1148_Benjamin_Sobarzo.pdf
└── BitacoraTrabjo.md

---

## Observaciones Finales

El proyecto se desarrolló exitosamente dentro del plazo establecido, cumpliendo con todos los objetivos planteados. La distribución colaborativa de tareas permitió optimizar el tiempo y recursos. Los resultados experimentales obtenidos confirmaron las expectativas teóricas sobre el comportamiento de los algoritmos de ordenamiento, demostrando claramente las ventajas de los algoritmos \(O(n \log n)\) sobre aproximaciones de complejidad cuadrática.

> **Tiempo total de desarrollo:** 11 días  
> **Fecha de entrega:** 15 de noviembre de 2025  
> **Estado:** ENTREGADO ✅

---
