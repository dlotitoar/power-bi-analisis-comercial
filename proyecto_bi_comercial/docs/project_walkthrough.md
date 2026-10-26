# Recorrido del proyecto

## Contexto
Una empresa comercial necesita convertir archivos operativos en información confiable. Antes de analizar ventas, valida fechas, claves, cantidades e importes.

## Alcance
Caso de portfolio con datos simulados: ETL, controles de calidad, SQL y guía de dashboard. No representa una empresa real.

## Decisiones
1. Deduplicar por identificador de venta.
2. Validar fechas y tipos numéricos.
3. Excluir fechas imposibles y valores numéricos inválidos.
4. Etiquetar datos ausentes sin adivinar la información real.
5. Calcular un importe esperado y una variación para identificar casos a investigar.
6. Documentar conteos y decisiones en `quality_report.csv`.

## Indicadores
Ventas totales, operaciones, ticket promedio, unidades vendidas, evolución mensual, ventas por región, canal, categoría y producto.

## Mejoras futuras
- Pruebas automatizadas de calidad.
- Cargar datos en PostgreSQL y ejecutar consultas.
- Modelo estrella con tabla calendario.
- Automatizar refresh.
- Incorporar margen cuando haya costos confiables.
- Ajustar por inflación con una fuente y metodología documentadas.

## Guion para entrevista
“Desarrollé un caso de BI con datos comerciales simulados. Introduje errores controlados en los archivos fuente, armé un pipeline en Python para limpiar y validar los datos, documenté los controles y preparé consultas SQL para responder preguntas comerciales. La guía de Power BI define KPIs y visualizaciones para explorar ventas por período, región, canal y producto. Busqué demostrar tanto preparación de datos como orientación al negocio.”
