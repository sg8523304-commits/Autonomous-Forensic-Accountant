from src.utils.get_logger import get_logger

logger = get_logger("audit_agent")

def audit_transaction(transaction_result):
    """Audit the transaction based on anomalies detected"""
    logger.info("Starting audit evaluation...")
    
    if not transaction_result:
        logger.warning("No transaction data to audit")
        return {"status": "no_data", "findings": []}
    
    anomalies = transaction_result.get("anomalies", [])
    
    # Initialize findings
    findings = []
    
    # Check if anomalies list is not empty
    if anomalies:
        logger.info(f"Found {len(anomalies)} anomalies")
        
        # Process each anomaly
        for anomaly in anomalies:
            if isinstance(anomaly, dict):
                finding = {
                    "type": anomaly.get("type", "unknown"),
                    "description": anomaly.get("description", "Anomaly detected"),
                    "severity": determine_severity(anomaly)
                }
                findings.append(finding)
        
        audit_status = "flagged"
    else:
        logger.info("No anomalies found")
        audit_status = "clean"
    
    # Prepare audit result
    audit_result = {
        "invoice_no": transaction_result.get("invoice_no"),
        "status": audit_status,
        "findings": findings,
        "summary": generate_summary(audit_status, len(findings))
    }
    
    logger.info(f"Audit completed. Status: {audit_status}")
    return audit_result

def determine_severity(anomaly):
    """Determine severity level of an anomaly"""
    anomaly_type = anomaly.get("type", "")
    
    if "high_amount" in anomaly_type:
        return "high"
    elif "unusual_pattern" in anomaly_type:
        return "medium"
    else:
        return "low"

def generate_summary(status, finding_count):
    """Generate a summary of the audit"""
    if status == "clean":
        return "Transaction appears normal with no anomalies detected"
    else:
        return f"Transaction flagged with {finding_count} anomaly/findings"