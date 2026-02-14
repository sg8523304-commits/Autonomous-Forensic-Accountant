def query_sap_transactions(invoice_no):
    """
    Dummy function for now.
    Later we connect to real SAP DB.
    """
    return {
        "invoice_no": invoice_no,
        "vendor": "ABC Supplies",
        "amount": 1500,
        "date": "2025-01-01",
        "status": "Posted"
    }