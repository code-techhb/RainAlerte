# 100 DAYS OF CODE USING PYTHON
# INSTRUCTOR: ANGELA YU
# Project 35 : Rain alert
# BY HOULAYMATOU B. | @code_techhb
# January 30, 2024

# ----------------------- import section ---------------------------------------
import requests
import key
import smtplib

# --------------------------------- API Call -------------------------------------------
parameters = {
    "lat": "Get your latitude",
    "lon": "Get your longitude",
    "cnt": 4,
    "appid": key.api_key,

}
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameters,

)
response.raise_for_status()
data = response.json()
print(data)

# loop through the data
sender = key.email
pass_code = key.password

for condition_dictionary in data["list"]:
    weather = condition_dictionary["weather"]
    weather_id = weather[0]["id"]
    if weather_id < 700:
        # create an smtp object
        with smtplib.SMTP("smtp.gmail.com") as new_email:
            # secure the connection created
            new_email.starttls()
            # login in
            new_email.login(user=sender, password=pass_code)
            # sendmail
            new_email.sendmail(
                from_addr=sender,
                to_addrs=key.email2,
                msg=f"Subject: Rain alert \n\nHey friend,\n\nIt's gonna rain today. "
                    f"So remember to bring an Umbrella :)\n\n-Have a blessed day!",
            )
            break
