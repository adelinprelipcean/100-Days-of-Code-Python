import smtplib
import random
import datetime as dt

def send_motivational_email(my_email, my_app_password, *emails_list):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_app_password)
        with open('quotes.txt', 'r') as file:
            quotes = file.readlines()
        for email in emails_list:
            connection.sendmail(from_addr=my_email, 
                                to_addrs=email, 
                                msg=f'Subject: Motivation Sunday\n\n{random.choice(quotes)}')
    connection.close()

if dt.datetime.now().weekday() == 6:
    send_motivational_email('your_email', 
                            '<your_app_password>', 
                            '<receiver_email>', 
                            '<another_receiver_email')
