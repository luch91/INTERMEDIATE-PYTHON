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


