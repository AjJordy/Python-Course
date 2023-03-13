# https://pt.wikipedia.org/wiki/Era_Unix
# https://docs.python.org/3/library/datetime.html
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pytz import timezone

# datetime(ano, mes, dia)
# datetime(ano, mes, dia, hora, minuto, segundo)
# datetime.strptime('DATA', 'FORMATO') 

data = datetime(2022, 4, 20, 7, 49, 23)
print('data =',data)

data_str_data = '2022/04/20 07:49:23'
data_str_fmt = '%Y/%m/%d %H:%M:%S'
data2 = datetime.strptime(data_str_data, data_str_fmt)
print('data from string =',data2)


# data_now = datetime.now()
data_now = datetime.now(timezone('America/Sao_Paulo'))
print('now =',data_now)
print('timestamp =',data_now.timestamp())
print('from timestamp =',datetime.fromtimestamp(1678724483.96961))


fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
delta = data_fim - data_inicio
print('delta =', delta)
print('total_seconds =', delta.total_seconds())

new_delta = timedelta(days=10, hours=2)
print('fim =',data_fim)
print('fim + delta =',data_fim + new_delta)

relative_delta = relativedelta(data_fim, data_inicio)
print('relative_delta =',relative_delta)



data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print('data original =',data)
print('data formatada =',data.strftime('%d/%m/%Y'))