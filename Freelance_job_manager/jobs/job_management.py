class JobManager:
    def __init__(self, client_manager):
        self.jobs = {}
        self.job_id_counter = 1
        self.client_manager = client_manager

