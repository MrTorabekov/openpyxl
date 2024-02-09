import openpyxl

workbook = openpyxl.Workbook()

sheet = workbook.active

sheet['A1'] = 'Name'
sheet['B1'] = 'address'
sheet['C1'] = 'phone'

sheet['A2'] = 'Diyorbek' # noqa
sheet['B2'] = 'Toshkent' # noqa
sheet['C2'] = '9977777'

workbook.save("data.xlsx")
