def view_financial_summary():
    """Display financial overview"""
    total_earnings = 0
    pending_amount = 0

    for job in jobs.values():
        if job['status'] == 'completed':
            total_earnings += job['price']
        else:
            pending_amount += job['price']

    print("\n-- Financial Summary --")
    print(f"Total Earnings: ${total_earnings:.2f}")
    print(f"Pending Payments: ${pending_amount:.2f}")
    print(f"Total Value: ${(total_earnings + pending_amount):.2f}")


