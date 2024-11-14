import smtplib
import requests
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email notification to multiple recipients
def send_email(subject, body, to_emails):
    from_email = "shahzaib.kkhowaja@gmail.com"  # Replace with your email address
    from_password = "sldv vmiz sieb pquq"  # Replace with your email password (or App Password if using 2FA)
    smtp_server = "smtp.gmail.com"  # Example for Gmail
    smtp_port = 587

    # Convert the list of emails to a comma-separated string
    to_email_str = ", ".join(to_emails)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email_str  # Multiple recipients
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server and send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(from_email, from_password)  # Login to the Gmail account
        server.sendmail(from_email, to_emails, msg.as_string())  # Send email to multiple recipients
        server.quit()  # Logout from the server
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to check the URL's status code
def check_url_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 500:
            print(f"Server error (500) occurred at {url}")
            subject = f"Error: 500 Server Error at {url}"
            body = f"The URL {url} returned a 500 Internal Server Error. Please investigate the issue."
            
            # List of recipients
            recipients = [
                "shahzaib.kkhowaja@gmail.com",  # Replace with actual email addresses
                "muhammad.usman.ashraf.10@gmail.com"
            ]
            send_email(subject, body, recipients)  # Send email only if status is 500
        else:
            print(f"URL {url} returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking URL: {e}")

# Example URL to check
url_to_check = "https://httpstat.us/500"  # Replace with your target URL

# Infinite loop to check the URL every minute
while True:
    check_url_status(url_to_check)  # Call the function to check the URL
    print("Waiting for the next check...")
    time.sleep(60)  # Wait for 1 minute before checking again

