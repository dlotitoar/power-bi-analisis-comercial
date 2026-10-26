from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data"/"raw"
OUT=ROOT/"data"/"processed"
DOCS=ROOT/"docs"
OUT.mkdir(parents=True,exist_ok=True)

def main():
    raw=pd.read_csv(RAW/"sales_raw.csv",dtype={"sale_id":"string","customer_id":"string","product_id":"string"})
    initial=len(raw)
    for c in ["sale_id","customer_id","product_id","product_name","category","region","channel"]:
        raw[c]=raw[c].astype("string").str.strip()
    raw["sale_date"]=pd.to_datetime(raw["sale_date"],errors="coerce",dayfirst=True)
    for c in ["quantity","unit_price_ars","discount_rate","sales_amount_ars"]:
        raw[c]=pd.to_numeric(raw[c],errors="coerce")
    dup=int(raw.duplicated("sale_id").sum())
    data=raw.drop_duplicates("sale_id",keep="first").copy()
    missing_region=int(data.region.isna().sum())
    missing_customer=int(data.customer_id.isna().sum())
    invalid_date=int(data.sale_date.isna().sum())
    invalid_numeric=int(data[["quantity","unit_price_ars","discount_rate","sales_amount_ars"]].isna().any(axis=1).sum())
    invalid_rules=int(((data.quantity<=0)|(data.unit_price_ars<=0)|(data.discount_rate<0)|(data.discount_rate>1)|(data.sales_amount_ars<0)).fillna(True).sum())
    data=data[data.sale_date.notna() & data.sale_id.notna() & data.product_id.notna()].copy()
    data["region"]=data.region.fillna("Sin informar")
    data["customer_id"]=data.customer_id.fillna("CLIENTE_SIN_ID")
    data=data.dropna(subset=["quantity","unit_price_ars","discount_rate","sales_amount_ars"])
    data=data[(data.quantity>0)&(data.unit_price_ars>0)&data.discount_rate.between(0,1)&(data.sales_amount_ars>=0)]
    data["expected_sales_ars"]=(data.quantity*data.unit_price_ars*(1-data.discount_rate)).round(2)
    data["amount_variance_ars"]=(data.sales_amount_ars-data.expected_sales_ars).round(2)
    data["sale_month"]=data.sale_date.dt.to_period("M").astype(str)
    data["sale_date"]=data.sale_date.dt.strftime("%Y-%m-%d")
    products=pd.read_csv(RAW/"products.csv")
    customers=pd.read_csv(RAW/"customers.csv")
    data=data.merge(products[["product_id","list_price_ars"]],on="product_id",how="left",validate="many_to_one")
    data=data.merge(customers[["customer_id","customer_segment","customer_province"]],on="customer_id",how="left",validate="many_to_one")
    data["customer_segment"]=data.customer_segment.fillna("Sin clasificar")
    data["customer_province"]=data.customer_province.fillna("Sin informar")
    data.to_csv(OUT/"sales_analytics.csv",index=False,encoding="utf-8-sig")
    report=pd.DataFrame([
      ["Filas originales",initial,"Conteo de filas fuente"],
      ["Duplicados por sale_id",dup,"Se conserva la primera ocurrencia"],
      ["Fechas inválidas",invalid_date,"Se excluyen del dataset analítico"],
      ["Región faltante",missing_region,"Se etiqueta Sin informar"],
      ["Cliente faltante",missing_customer,"Se etiqueta CLIENTE_SIN_ID"],
      ["Campos numéricos faltantes/no convertibles",invalid_numeric,"Se excluyen del dataset analítico"],
      ["Reglas numéricas incumplidas",invalid_rules,"Se excluyen del dataset analítico"],
      ["Filas finales",len(data),"Registros después de limpieza y enriquecimiento"],
      ["Diferencias de importe > ARS 1",int((data.amount_variance_ars.abs()>1).sum()),"Investigar; no se sobrescribe el importe fuente"]
    ],columns=["control","count","decision"])
    report.to_csv(DOCS/"quality_report.csv",index=False,encoding="utf-8-sig")
    print(f"ETL finalizado: {initial} filas fuente -> {len(data)} filas analíticas")
if __name__=="__main__": main()
