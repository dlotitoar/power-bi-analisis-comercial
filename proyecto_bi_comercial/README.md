# Proyecto BI Comercial — Calidad de Datos, SQL y Power BI
**Portfolio con datos 100% simulados. No representa datos ni procesos internos de Increxa ni de sus clientes.**

## Objetivo
Construir un flujo reproducible desde archivos fuente con problemas de calidad hasta un dataset analítico y consultas SQL para un dashboard comercial.

## Preguntas de negocio
- ¿Cómo evolucionan las ventas por mes?
- ¿Qué regiones y canales aportan más ventas?
- ¿Qué categorías y productos lideran el rendimiento?
- ¿Cuál es el ticket promedio?
- ¿Qué problemas de calidad existen y cómo se trataron?

## Estructura
- `data/raw/`: ventas con errores intencionales, catálogo y clientes simulados.
- `python/etl_pipeline.py`: limpieza, controles y exportación.
- `data/processed/`: dataset limpio generado por el ETL.
- `sql/schema.sql`, `sql/analysis.sql`: modelo y consultas SQL.
- `powerbi/dashboard_guide.md`: pasos y medidas DAX.
- `docs/`: diccionario de datos, walkthrough y reporte de calidad.

## Ejecución
Requisitos: Python 3.10+, pandas y numpy.
```bash
pip install -r requirements.txt
python python/etl_pipeline.py
```
## Nota
No se incluye `.pbix`; el repositorio incluye datos, ETL, SQL y guía para reproducir el dashboard en Power BI Desktop. Identificá siempre el caso como simulado.
