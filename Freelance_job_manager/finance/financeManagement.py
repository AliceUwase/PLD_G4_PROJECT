from db.db import cursor, conn
from decimal import Decimal

class FinancialSummary:
    def __init__(self, job_manager):
        """Initialize with job_manager instance"""
        self.job_manager = job_manager
        self.tax_rate = Decimal('0.20')
    # display summary
    def display_summary(self):
        """Display financial overview"""
        cursor.execute("""
            SELECT 
                job_name,
                company_name,
                rate,
                hours,
                rate * hours as price
            FROM jobs
        """)
        jobs = cursor.fetchall()
        
        total_earnings = 0
        companies = set()
        total_hours = 0
        
        print("\n-- Financial Summary --")
        print("\nDetailed Job Breakdown:")
        print("-" * 60)
        print(f"{'Job Name':<20} {'Company':<15} {'Hours':>8} {'Rate':>8} {'Total':>10}")
        print("-" * 60)
        
        for job in jobs:
            job_name, company_name, rate, hours, price = job
            companies.add(company_name)
            total_earnings += price
            total_hours += hours
            print(f"{job_name[:20]:<20} {company_name[:15]:<15} {hours:>8.1f} ${rate:>7.2f} ${price:>9.2f}")
        
        total_jobs = len(jobs)
        avg_job_value = total_earnings / total_jobs if total_jobs > 0 else 0
        avg_hourly_rate = total_earnings / total_hours if total_hours > 0 else 0
        estimated_tax = total_earnings * self.tax_rate
        net_earnings = total_earnings - estimated_tax
        
        print("\n-- Summary Statistics --")
        print(f"Total Earnings: ${total_earnings:.2f}")
        print(f"Total Hours Worked: {total_hours:.1f}")
        print(f"Average Hourly Rate: ${avg_hourly_rate:.2f}")
        print(f"\nTotal Companies: {len(companies)}")
        print(f"Total Jobs: {total_jobs}")
        print(f"Average Job Value: ${avg_job_value:.2f}")
        print(f"\nEstimated Tax (20%): ${estimated_tax:.2f}")
        print(f"Net Earnings: ${net_earnings:.2f}")