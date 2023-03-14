import calendar
import locale

locale.setlocale(locale.LC_ALL, '') # ou 'pt_BR.utf8'

print(calendar.calendar(2023))
print(locale.getlocale())

