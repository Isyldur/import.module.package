import application.salary as salary
import application.db.people as people
from datetime import datetime


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(datetime.now())
