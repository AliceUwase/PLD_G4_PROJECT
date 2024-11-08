from Freelance_job_manager.finance.financial_management import FinancialManager
from Freelance_job_manager.jobs.job_management import JobManager


def test_view_summary():
    job_manager = JobManager()
    financial_manager = FinancialManager(job_manager)
    assert financial_manager.view_summary() == {}