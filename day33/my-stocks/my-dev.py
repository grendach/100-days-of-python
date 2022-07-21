
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import plotly.express as px


# Data

start = dt.datetime(2017,1,1)
end = dt.datetime.now()

stocks = web.DataReader(['0P0000ZT9I'], 'yahoo', start, end)
stocks_close = pd.DataFrame(web.DataReader(['0P0000ZT9I'], 'yahoo', start, end)['Close'])

# Area chart

area_chart = px.area(stocks_close['0P0000ZT9I'], title = f'0P0000ZT9I PRICE ({start}-{end})')

area_chart.update_xaxes(title_text = 'Date')
area_chart.update_yaxes(title_text = '0P0000ZT9I Close Price', tickprefix = '$')
area_chart.update_layout(showlegend = False)

area_chart.show()
area_chart.write_html("0P0000ZT9I.html")
