# Taller2_info1148
\documentclass[12pt,a4paper]{article}
\usepackage[spanish]{babel}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{xcolor}
\usepackage{hyperref}

\geometry{margin=2.5cm}

\title{\textbf{Bitácora de Trabajo \ Tarea 2 - INFO1148}}
\author{Benjamin Sobarzo, Kevin Cortes, Jonathan Huinca}
\date{15 de noviembre de 2025}

\begin{document}

\maketitle

\begin{center}
\textbf{Período de Trabajo: 4 al 15 de noviembre de 2025} \
\textbf{Fecha de Entrega: 15 de noviembre de 2025}
\end{center}

\section*{Información del Proyecto}
\begin{itemize}
\item \textbf{Título:} Análisis Comparativo de Algoritmos de Ordenamiento
\item \textbf{Integrantes:} Benjamin Sobarzo, Kevin Cortes, Jonathan Huinca
\item \textbf{Asignatura:} INFO1148
\item \textbf{Semestre:} II-2025
\item \textbf{Repositorio:} \url{https://github.com/blosttt/Taller2.info1148}
\end{itemize}

\section*{Distribución Inicial de Tareas}
\begin{table}[h!]
\centering
\begin{tabular}{p{0.3\textwidth}p{0.6\textwidth}}
\toprule
\textbf{Integrante} & \textbf{Responsabilidades Principales} \
\midrule
Benjamin Sobarzo & Implementación de algoritmos y sistema de medición \
Kevin Cortes & Diseño experimental y análisis de resultados \
Jonathan Huinca & Documentación y preparación de informe \
\bottomrule
\end{tabular}
\end{table}

\section*{Cronología de Actividades}

\subsection*{4 de noviembre - Inicio del Proyecto (12:00 hrs)}
\begin{itemize}
\item Reunión inicial del equipo para planificación del trabajo
\item Distribución de tareas y responsabilidades
\item Definición de objetivos y alcance del proyecto
\item Establecimiento de cronograma con hitos específicos
\end{itemize}

\subsection*{5-6 de noviembre - Fase de Investigación y Diseño}
\begin{itemize}
\item Investigación teórica sobre complejidad algorítmica
\item Diseño del experimento con los siguientes parámetros:
\begin{itemize}
\item Tamaños de entrada: 100, 500, 1000, 2000, 3000
\item Tipos de datos: aleatorios, ordenados, inversos
\item Métricas: tiempo de ejecución en milisegundos
\end{itemize}
\item Planificación de la implementación en Python
\end{itemize}

\subsection*{7-9 de noviembre - Implementación de Algoritmos}
\begin{itemize}
\item Desarrollo de los tres algoritmos de ordenamiento:
\begin{itemize}
\item \texttt{quicksort.py} - Implementación con pivote central
\item \texttt{mergesort.py} - Algoritmo divide y vencerás estable
\item \texttt{bubblesort.py} - Versión optimizada con detección de intercambios
\end{itemize}
\item Pruebas unitarias de cada implementación
\item Verificación de corrección con diferentes conjuntos de datos
\end{itemize}

\subsection*{10-12 de noviembre - Sistema de Medición y Pruebas}
\begin{itemize}
\item Desarrollo del archivo \texttt{comparacion.py}
\item Implementación de la clase \texttt{AlgorithmBenchmark}
\item Sistema de medición de tiempos con \texttt{time.perf_counter()}
\item Módulo de generación automática de gráficos con matplotlib
\item Ejecución de pruebas preliminares y ajuste de parámetros
\end{itemize}

\subsection*{13-14 de noviembre - Ejecución de Experimentos}
\begin{itemize}
\item Ejecución sistemática de todos los casos de prueba
\item Recolección de datos para los tres algoritmos en todos los escenarios
\item Generación de tablas y gráficos comparativos
\item Análisis inicial de resultados obtenidos
\end{itemize}

\subsection*{15 de noviembre - Finalización y Entrega (12:00 hrs)}
\begin{itemize}
\item Análisis detallado de resultados experimentales
\item Comparación con predicciones teóricas de complejidad
\item Elaboración del informe técnico completo
\item Revisión final del código y documentación
\item Integración de todos los componentes del proyecto
\item \textbf{Entrega final del trabajo completo}
\end{itemize}

\section*{Hitos Principales Alcanzados}
\begin{table}[h!]
\centering
\begin{tabular}{p{0.2\textwidth}p{0.7\textwidth}c}
\toprule
\textbf{Fecha} & \textbf{Hito} & \textbf{Estado} \
\midrule
4 nov & Planificación completa del proyecto & ✅ \
7 nov & Implementación de los tres algoritmos & ✅ \
10 nov & Sistema de medición funcional & ✅ \
13 nov & Ejecución completa de experimentos & ✅ \
15 nov & Análisis, documentación y entrega final & ✅ \
\bottomrule
\end{tabular}
\end{table}

\section*{Recursos Utilizados}

\subsection*{Tecnológicos}
\begin{itemize}
\item \textbf{Lenguaje:} Python 3.x
\item \textbf{Bibliotecas:} matplotlib, numpy, statistics, time
\item \textbf{Entorno:} Multiplataforma (Windows/Linux/macOS)
\item \textbf{Repositorio:} GitHub
\end{itemize}

\subsection*{Metodológicos}
\begin{itemize}
\item \textbf{Enfoque:} Investigación aplicada con validación experimental
\item \textbf{Métricas:} Tiempo de ejecución con múltiples repeticiones
\item \textbf{Validación:} Contrastación teoría-práctica
\end{itemize}

\section*{Estructura del Proyecto Entregado}
\begin{verbatim}
Tarea2_Algoritmos/
├── quicksort.py
├── mergesort.py
├── bubblesort.py
├── comparacion.py
├── TA_2_INFO1148_Benjamin_Sobarzo.pdf
└── README.md
\end{verbatim}

\section*{Observaciones Finales}
El proyecto se desarrolló exitosamente dentro del plazo establecido, cumpliendo con todos los objetivos planteados. La distribución colaborativa de tareas permitió optimizar el tiempo y recursos. Los resultados experimentales obtenidos confirmaron las expectativas teóricas sobre el comportamiento de los algoritmos de ordenamiento, demostrando claramente las ventajas de los algoritmos $O(n \log n)$ sobre aproximaciones de complejidad cuadrática.

\begin{center}
\textbf{Tiempo total de desarrollo: 11 días} \
\textbf{Fecha de entrega: 15 de noviembre de 2025} \
\textbf{Estado: ENTREGADO ✅}
\end{center}

\begin{center}
\rule{0.8\textwidth}{0.5pt} \
\textit{Bitácora actualizada el 15 de noviembre de 2025 para reflejar la fecha real de entrega del proyecto.}
\end{center}

\end{document}
