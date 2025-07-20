##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import smtplib
import random


def send_email(my_email, my_password, name, email):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        with open(f'letter_templates/letter_{random.randint(1,3)}.txt', 'r') as file:
            letter = file.read()
            letter = letter.replace('[NAME]', name)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f'Subject: Happy Birthday!\n\n{letter}')


data = pandas.read_csv('birthdays.csv')
emails_list = {}

for element in data.values:
    name = element[0]
    email = element[1]
    month = element[3]
    day = element[4]
    today = dt.datetime.now()
    if month == today.month and day == today.now().day:
        emails_list[name] = email
        
for name, email in emails_list.items():
    send_email('<your_email>', '<your_password>', name, email)
