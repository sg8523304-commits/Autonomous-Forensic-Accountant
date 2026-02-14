from src.db.db import query_sap_transactions
from src.utils.anomaly_detector import detect_anomalies
from src.utils.get_logger import get_logger
import pandas as pd

logger = get_logger("transaction_agent")

def process_transaction(invoice_no):
    logger.info(f"Fetching SAP transaction for invoice: {invoice_no}")
    
    result = query_sap_transactions(invoice_no)
    
    # Check if result is a DataFrame or dict
    if isinstance(result, pd.DataFrame):
        df = result
    else:
        # If it's a dict, convert to DataFrame
        df = pd.DataFrame([result]) if result else pd.DataFrame()
    
    if df.empty:
        logger.warning("No SAP data found")
        return {}
    
    logger.info("Running anomaly detection")
    anomalies = detect_anomalies(df)
    
    return {
        "invoice_no": invoice_no,
        "status": "processed",
        "raw_data": df.to_dict(orient="records"),
        "anomalies": anomalies
    }