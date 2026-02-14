from src.agents.transaction_agent import process_transaction
from src.agents.audit_agent import audit_transaction
from src.agents.report_agent import generate_report
from src.utils.get_logger import get_logger

logger = get_logger("workflow")

def run_workflow(invoice_no):
    """
    Runs the entire pipeline:
    1. SAP transaction fetch
    2. Anomaly detection
    3. Audit scoring
    4. Report generation
    """

    logger.info(f"Starting workflow for invoice: {invoice_no}")

    # Step 1: Fetch and analyze transaction
    transaction_result = process_transaction(invoice_no)

    # Step 2: Audit anomalies
    audit_result = audit_transaction(transaction_result)

    # Step 3: Generate final report
    report_json = generate_report(audit_result)

    logger.info("Workflow completed successfully")
    return report_json