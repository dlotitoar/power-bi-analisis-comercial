# Diccionario de datos

| Campo | Definición |
|---|---|
| sale_id | Identificador de operación |
| sale_date | Fecha de venta |
| customer_id | Clave ficticia del cliente |
| product_id | Clave del producto |
| product_name / category | Nombre y categoría comercial |
| region / channel | Región y canal |
| quantity | Unidades vendidas |
| unit_price_ars | Precio unitario nominal en ARS |
| discount_rate | Descuento como proporción 0–1 |
| sales_amount_ars | Importe registrado de la operación |
| expected_sales_ars | cantidad × precio × (1 − descuento), referencia |
| amount_variance_ars | Diferencia entre importe registrado y esperado |
| sale_month | Mes YYYY-MM |

## Reglas de calidad
- `sale_id` único; conservar primera ocurrencia de duplicados.
- Fechas imposibles se convierten en nulas y se excluyen.
- Cantidad y precio > 0; descuento entre 0 y 1; importe >= 0.
- Región faltante → `Sin informar`; cliente faltante → `CLIENTE_SIN_ID`.
- Enriquecimiento por claves de producto y cliente, sin inventar valores.
- Se calcula diferencia de importe sin sobrescribir el importe original.

## Limitaciones
Dataset sintético sin estacionalidad validada; no ajustado por inflación. La regla de importe no contempla impuestos, flete u otros cargos.
