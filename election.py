import mysql.connector
import datetime
import smtplib
from email.mime.text import MIMEText

# Function to get voter details
def get_voter_details():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    return name, email

# Function to display candidates
def display_candidates():
    print("Select the Candidate listed below")
    print("1. Atchaya")
    print("2. Ananth")
    print("3. Priya")

# Function to update vote in the database
def update_vote(candidate_number):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='election'
    )
    cursor = conn.cursor()
    
    candidate_fields = {1: "Atchaya", 2: "Ananth", 3: "Priya"}
    candidate = candidate_fields[candidate_number]
    
    query = f'''
    UPDATE election_candidate
    SET {candidate} = {candidate} + 1
    WHERE id = 1
    '''
    
    cursor.execute(query)
    conn.commit()
    conn.close()

# Function to record voter details
def record_voter(name, email):
    with open('voters.txt', 'a') as file:
        file.write(f"{name}, {email}, {datetime.datetime.now()}\n")

# Function to send email confirmation
def send_email(email):
    msg = MIMEText("Thank you for voting!")
    msg['Subject'] = "Voting Confirmation"
    msg['From'] = 'atchayaananth2005@gmail.com'
    msg['To'] = email
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('atchayaananth2005@gmail.com', 'qiuf oyvp fpzc wfvz')
        server.send_message(msg)

# Main function
def main():
    name, email = get_voter_details()
    display_candidates()
    
    choice = int(input("Enter the number of the candidate you want to vote for: "))
    update_vote(choice)
    
    record_voter(name, email)
    send_email(email)
    print("Thank you for voting!")

if __name__ == "__main__":
    main()
