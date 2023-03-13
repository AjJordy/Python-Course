# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html

# Dias da semana
# 0 = segunda | 6 = domingo

import calendar

print(calendar.calendar(2023))
print(calendar.month(2023, 12))

numero_primeiro_dia, ultimo_dia = calendar.monthrange(2023, 12)
print('Range de Dezembro =', numero_primeiro_dia, ultimo_dia)
print(list(calendar.day_name))
print('primeiro dia de dezembro =',calendar.day_name[numero_primeiro_dia])
print('ultimo dia de dezembro =',calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)])


for week in calendar.monthcalendar(2023, 12):
	print(list(week))