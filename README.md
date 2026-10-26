# Proyecto BI Comercial — ETL, SQL y Power BI

**Portfolio de Business Intelligence con datos 100 % simulados. Este proyecto no utiliza ni representa datos, clientes o procesos internos de Increxa ni de sus clientes.**

## 1. Objetivo del proyecto

Desarrollar un flujo reproducible de análisis comercial que abarque desde la preparación y validación de datos de origen hasta la construcción de consultas SQL e indicadores para un dashboard en Power BI.

El objetivo es demostrar habilidades prácticas en procesos ETL, limpieza y calidad de datos, análisis con SQL, modelado de información y visualización de indicadores de negocio.

## 2. Preguntas de negocio

El análisis busca responder las siguientes preguntas:

- ¿Cómo evolucionan las ventas a lo largo del tiempo?
- ¿Qué regiones y canales concentran la mayor facturación?
- ¿Qué productos y categorías tienen mejor rendimiento comercial?
- ¿Cuál es el ticket promedio de las operaciones?
- ¿Qué problemas de calidad presentan los datos y cómo se trataron?
- ¿Cómo se distribuyen las ventas entre los distintos segmentos de clientes?

## 3. Dashboard de Power BI

El informe está organizado en tres páginas, cada una orientada a una dimensión del análisis comercial.

### Página 1 — Resumen Ejecutivo

Ofrece una visión general del desempeño comercial mediante indicadores clave:

- Facturación total.
- Cantidad de operaciones.
- Unidades vendidas.
- Ticket promedio.
- Evolución mensual de las ventas.
- Distribución de la facturación por región y canal.

**Objetivo:** facilitar una lectura rápida del rendimiento comercial e identificar tendencias y diferencias entre regiones y canales.

### Página 2 — Análisis de Productos

Permite comparar el rendimiento de productos y categorías mediante:

- Facturación por producto.
- Ventas por categoría.
- Unidades vendidas por producto.
- Indicadores de productos y unidades comercializadas.

**Objetivo:** identificar qué productos y categorías tienen mayor participación en las ventas y cuáles podrían requerir un análisis más detallado.

### Página 3 — Clientes y Canales

Explora la composición de la actividad comercial desde la perspectiva de los clientes y su distribución geográfica:

- Ventas por segmento de clientes.
- Cantidad de clientes por segmento.
- Distribución geográfica de las ventas por provincia.
- Filtros por período, región, segmento de clientes, provincia y canal.

**Objetivo:** comparar segmentos de clientes, explorar diferencias geográficas y analizar cómo varían las ventas según los filtros seleccionados.

## 4. Proceso ETL y calidad de datos

El proyecto incluye un proceso de extracción, transformación y carga (ETL) implementado en Python.

Las etapas contemplan:

1. **Extracción:** lectura de archivos fuente con datos comerciales simulados.
2. **Perfilado y validación:** identificación de registros duplicados, fechas inválidas, valores faltantes e inconsistencias.
3. **Transformación:** aplicación de reglas de limpieza y normalización para preparar los datos para el análisis.
4. **Controles de calidad:** revisión de los registros procesados y documentación de las incidencias detectadas.
5. **Carga:** exportación del dataset procesado para su uso en consultas SQL y Power BI.

Los problemas de calidad se introducen de manera intencional en los datos de origen para demostrar cómo pueden identificarse, tratarse y documentarse.

## 5. Herramientas utilizadas

- **Python:** automatización del proceso ETL.
- **Pandas y NumPy:** manipulación y transformación de datos.
- **SQL:** consultas, agregaciones y análisis comercial.
- **Power BI:** visualización e interacción con los indicadores.
- **DAX:** creación de medidas e indicadores calculados.
- **GitHub:** documentación y control de versiones del proyecto.

## 6. Estructura del repositorio

```text
power-bi-analisis-comercial/
├── data/
│   ├── raw/
│   └── processed/
├── python/
│   └── etl_pipeline.py
├── sql/
│   ├── schema.sql
│   └── analysis.sql
├── powerbi/
│   └── dashboard_guide.md
├── docs/
│   ├── data_dictionary.md
│   ├── walkthrough.md
│   └── data_quality_report.md
├── requirements.txt
└── README.md
```

La estructura refleja los componentes previstos del proyecto. Los archivos deben incorporarse al repositorio si efectivamente están disponibles.

## 7. Cómo ejecutar el ETL

### Requisitos

- Python 3.10 o superior.
- Pandas.
- NumPy.

### Instalación y ejecución

```bash
pip install -r requirements.txt
python python/etl_pipeline.py
```

El proceso genera el dataset procesado en la ubicación definida por el script. Las consultas SQL y la guía de Power BI permiten continuar con el análisis.

## 8. Resultados y aprendizajes

Este proyecto permite practicar un flujo de trabajo de Business Intelligence de principio a fin:

- Identificar y tratar problemas de calidad de datos.
- Automatizar transformaciones con Python.
- Construir consultas SQL para responder preguntas comerciales.
- Crear indicadores y visualizaciones en Power BI.
- Documentar reglas de transformación y criterios de análisis.

## 9. Alcance y limitaciones

Todos los datos son sintéticos y se utilizan exclusivamente con fines educativos y de portfolio. Los resultados no describen una empresa real.

El dashboard presenta indicadores descriptivos de ventas. No incluye análisis de rentabilidad si no se dispone de costos, ni permite atribuir causalidad a las diferencias observadas.

---

**Autor:** Daniel Enrique Lotito Velasquez  
**Área:** Business Intelligence · Data Analytics · ETL · SQL · Power BI
