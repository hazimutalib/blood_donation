import schedule
import time

def job():
    print("Job is running...")

# Schedule the job to run every 1 minute
# schedule.every(1).minutes.do(job)

# Keep the script running to allow the scheduled jobs to execute
while True:
    job()
    time.sleep(30)
