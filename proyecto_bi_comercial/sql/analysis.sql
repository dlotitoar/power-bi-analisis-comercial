-- 1. KPIs generales
SELECT COUNT(*) AS operations, SUM(sales_amount_ars) AS total_sales_ars,
       AVG(sales_amount_ars) AS average_order_value_ars, SUM(quantity) AS units_sold
FROM fact_sales;

-- 2. Evolución mensual (PostgreSQL)
SELECT DATE_TRUNC('month', sale_date)::date AS month, SUM(sales_amount_ars) AS sales_ars,
       COUNT(*) AS operations
FROM fact_sales GROUP BY 1 ORDER BY 1;

-- 3. Región y canal
SELECT region, channel, SUM(sales_amount_ars) AS sales_ars, COUNT(*) AS operations
FROM fact_sales GROUP BY region, channel ORDER BY sales_ars DESC;

-- 4. Categorías y productos
SELECT p.category, p.product_name, SUM(f.sales_amount_ars) AS sales_ars, SUM(f.quantity) AS units
FROM fact_sales f JOIN dim_product p ON p.product_id=f.product_id
GROUP BY p.category,p.product_name ORDER BY sales_ars DESC;

-- 5. Segmentos de cliente
SELECT c.customer_segment, COUNT(DISTINCT f.customer_id) AS customers, SUM(f.sales_amount_ars) AS sales_ars
FROM fact_sales f LEFT JOIN dim_customer c ON c.customer_id=f.customer_id
GROUP BY c.customer_segment ORDER BY sales_ars DESC;

-- 6. Diferencias contra importe de referencia
SELECT sale_id, sales_amount_ars,
       ROUND(quantity*unit_price_ars*(1-discount_rate),2) AS expected_amount
FROM fact_sales
WHERE ABS(sales_amount_ars-ROUND(quantity*unit_price_ars*(1-discount_rate),2))>1;
