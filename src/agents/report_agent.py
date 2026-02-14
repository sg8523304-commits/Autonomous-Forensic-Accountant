import json
from src.utils.get_logger import get_logger

logger = get_logger("report_agent")

def generate_report(audit_result):
    """Generate a JSON report from audit results"""
    logger.info("Generating JSON report...")
    
    if not audit_result:
        logger.warning("No audit data to generate report")
        return json.dumps({"error": "No audit data available"})
    
    # Determine risk level based on findings
    findings = audit_result.get("findings", [])
    
    if len(findings) > 2:
        risk_level = "HIGH"
    elif len(findings) > 0:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    
    # Create report structure
    report = {
        "invoice_number": audit_result.get("invoice_no", "UNKNOWN"),
        "audit_status": audit_result.get("status", "unknown"),
        "risk_level": risk_level,
        "findings_summary": audit_result.get("summary", "No summary available"),
        "findings": findings,
        "total_findings": len(findings)
    }
    
    # Convert to JSON
    report_json = json.dumps(report, indent=2)
    
    logger.info(f"Report generated. Risk level: {risk_level}")
    
    # Optional: Save to file
    save_report_to_file(report, audit_result.get("invoice_no", "unknown"))
    
    return report_json

def save_report_to_file(report, invoice_no):
    """Save report to a JSON file"""
    try:
        filename = f"reports/report_{invoice_no}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        logger.info(f"Report saved to {filename}")
    except Exception as e:
        logger.error(f"Failed to save report: {e}")