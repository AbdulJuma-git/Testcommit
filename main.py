import schedule
import time
import subprocess
from datetime import datetime

def create_new_file_and_commit():
    # Get the current date and time
    now = datetime.now()
    current_time_in_words = now.strftime("%A, %B %d, %Y %I:%M %p")
    file_name = now.strftime("timestamp_%Y%m%d%H%M%S.txt")

    # Write the current time in words to a new file
    with open(file_name, "w") as file:
        file.write(f"{current_time_in_words}\n")

    # Git add, commit, and push
    subprocess.run(["git", "add", file_name])
    commit_message = f"Add new timestamp file: {file_name}"
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push"])

# Schedule the job every 30 minutes
schedule.every(1).minutes.do(create_new_file_and_commit)

while True:
    schedule.run_pending()
    time.sleep(1)
