
import datetime
import random
import smtplib
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pandas_datareader.data as web
import yfinance
from email.mime.text import MIMEText

MY_EMAIL = "___"
MY_PASSWORD = "____"


 
# start_date , as per our convenience we can modify
start_date = datetime.datetime(2021, 2, 1)
end_date = datetime.datetime.now()
 
# current_date , as per our convenience we can modify
def get_fund_data(fund_name):
    fund_info = yfinance.Ticker(fund_name)
 
    fund_status = fund_info.history(start=start_date, end=end_date)

    stocks = web.DataReader([fund_name], 'yahoo', start_date, end_date)
    stocks_close = pd.DataFrame(web.DataReader([fund_name], 'yahoo', start_date, end_date)['Close'])

    # Area chart

    fund_graph = px.area(stocks_close[fund_name], title = f'{fund_name} PRICE ({start_date} - {end_date})')

    fund_graph.update_xaxes(title_text = 'Date')
    fund_graph.update_yaxes(title_text = f'{fund_name} Close Price', tickprefix = '$')
    fund_graph.update_layout(showlegend = False)


    return fund_name, fund_status, fund_graph


fund_1_name, fund_1_status, fund_1_graph = get_fund_data("0P0000ZT9I")
fund_2_name, fund_2_status, fund_2_graph = get_fund_data("0P0000WDVS")

print(fund_1_name)
print(fund_1_status)
fund_1_graph.write_html(f"{fund_1_name}.html")

print(fund_2_name)
print(fund_2_status)
fund_2_graph.write_html(f"{fund_2_name}.html")

# fund_2_graph.show()



with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    # connection.starttls()
    connection.ehlo()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="___",
        msg=f"Subject:Funds status\n\n{fund_1_name}\n{fund_1_status}\n{fund_2_name}\n{fund_2_status}"
        )

# html = open(f"{fund_1_name}.html")
# msg = MIMEText(html.read(), 'html')
# msg['From'] = MY_EMAI32L
# msg['To'] = MY_EMAIL
# msg['Subject'] = f"{fund_1_name} Report"

# debug = False
# if debug:
#     print(msg.as_string())
# else:
#     server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     # server.starttls()
#     server.ehlo()
#     server.login(MY_EMAIL, MY_PASSWORD)
#     text = msg.as_string()
#     from_addr=MY_EMAIL
#     to_addr=MY_EMAIL
#     server.sendmail(from_addr, to_addr, text)
#     server.quit()
