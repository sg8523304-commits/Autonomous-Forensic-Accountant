import pandas as pd
import logging

logger = logging.getLogger(__name__)

def detect_anomalies(df):
    """
    Detect anomalies in transaction data
    
    Args:
        df: DataFrame containing transaction data
        
    Returns:
        list: List of detected anomalies
    """
    logger.info("Detecting anomalies in transaction data")
    
    anomalies = []
    
    # If DataFrame is empty, return empty list
    if df.empty:
        return anomalies
    
    # Example anomaly detection logic
    # Check for unusually high amounts (above 3 standard deviations)
    if 'amount' in df.columns:
        mean_amount = df['amount'].mean()
        std_amount = df['amount'].std()
        
        high_amount_threshold = mean_amount + (3 * std_amount)
        high_amounts = df[df['amount'] > high_amount_threshold]
        
        for _, row in high_amounts.iterrows():
            anomalies.append({
                'type': 'high_amount',
                'description': f"Transaction amount {row['amount']} exceeds threshold {high_amount_threshold:.2f}",
                'row': row.to_dict()
            })
    
    # Check for unusual patterns (you can add more checks here)
    
    logger.info(f"Found {len(anomalies)} anomalies")
    return anomalies