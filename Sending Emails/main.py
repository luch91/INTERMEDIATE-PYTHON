"""
import smtplib

my_email = "orluchee91@gmail.com"
password = "orluchee-9191"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="luchijudith@gmail.com",
                        msg="Subject: Welcome Onboard\n\nThis is your appointment letter"
                        )


"""

import datetime as dt
import random
import smtplib

"""
now = dt.datetime.now()
print(now)
year = now.year
month = now.month
week_day = now.weekday()

date_of_birth = dt.datetime(year=1990, month=2, hour=13)
print(date_of_birth)

"""
my_email = "olr91@gmail.com"
password = "acbd96@w"

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 0:
    with open("quotes.txt") as quote_files:
        all_quotes = quote_files.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email, msg=f"Subject: Monday Motivation\n\n{quote}"
        )




