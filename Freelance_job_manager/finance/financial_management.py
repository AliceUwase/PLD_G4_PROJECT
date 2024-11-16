class FinancialManager:
    def __init__(self, job_manager):
        self.job_manager = job_manager

    def calculate_total_income(self):
        total_income = sum(job['rate'] * job['hours'] for job in self.job_manager.jobs)
        print(f"Total income from all jobs: ${total_income:.2f}")
        return total_income

    def view_summary(self):
        print("\nFinancial Summary")
        self.calculate_total_income()
