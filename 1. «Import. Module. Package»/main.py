import datetime
from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    date = datetime.date.today().strftime('%d-%m-%Y')
    get_employees(date)
    calculate_salary(date)
