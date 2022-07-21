import random
import datetime as dt
import smtplib

MY_EMAIL = "_______"
MY_PASSWORD = "______"

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
print(quote)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    # connection.starttls()
    connection.ehlo()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="______",
        msg=f"Subject:Motivation\n\n{quote}"
    )
