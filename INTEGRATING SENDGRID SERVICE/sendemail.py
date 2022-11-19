import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SUBJECT = "Personal Expense Tracker Application"

def sendmail(TEXT,email):
    message = Mail(
        from_email='cloudproject15092022@gmail.com',
        to_emails=email,
        subject=SUBJECT,
        html_content=TEXT)
    
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e)
