import pandas as pd
import smtplib
import datetime as dt
import random
my_email = "paulljoel30@gmail.com"
password="HIDDEN"

month = dt.datetime.now().month
day = dt.datetime.now().day
today = (month, day)
birthday_data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_data.iterrows()}

if today in birthday_dict:
    data_row = birthday_dict[today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        data = file.read()
        new_data = data.replace("[NAME]", data_row["name"])
        print(new_data)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=data_row['email'],
                                msg=f"Subject:Happy Birthday\n\n{new_data}")
                              
