from src.graph.workflow import run_workflow
from src.utils.get_logger import get_logger

logger = get_logger("main")

if __name__ == "__main__":
    invoice_no = input("Enter Invoice Number: ")
    logger.info(f"Running autonomous forensic workflow for invoice: {invoice_no}")

    result = run_workflow(invoice_no)

    print("\n===== FINAL REPORT =====\n")
    print(result)