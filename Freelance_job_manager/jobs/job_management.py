class JobManager:
    def __init__(self, client_manager):
        self.jobs = {}
        self.job_id_counter = 1
        self.client_manager = client_manager

    def add_job(self, job_details):
        job_id = self.job_id_counter
        self.jobs[job_id] = job_details
        self.job_id_counter += 1
        return job_id

    def view_all_jobs(self):
        return self.jobs
    
    def view_job_details(self, job_id):
        return self.jobs.get(job_id, "Job not found")
    
    def update_job_status(self, job_id, new_status):
        if job_id in self.jobs:
            self.jobs[job_id]["status"] = new_status
            return True
        return False
    
    def delete_job(self, job_id):
        if job_id in self.jobs:
            del self.jobs[job_id]
            return True
        return False