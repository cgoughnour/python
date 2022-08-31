import pathlib

import mysql.connector
from credentials import QaCredentials as Pc
import log

db = mysql.connector.connect(
    host=Pc.host,
    user=Pc.user,
    password=Pc.password,
    database=Pc.database
)

cursor = db.cursor()


def insert_license(org, count, opty, product, start, end, file):
    query = f'select count(*) from organization where organization_id = "{org}"'
    query1 = f'update organization set status = "ACTIVE" where organization_id = "{org}"'
    query2 = f'select count(*) from license where organization_id = "{org}" and seats = {count} and order_number= "{opty}" and products = "{product}" and start_date = "{start}" and end_date= "{end}"'
    query3 = f'insert into license (license_id, organization_id, seats, order_number, products, start_date, end_date, status) values (uuid(), "{org}", {count}, "{opty}", "{product}", "{start}", "{end}", "ACTIVE")'
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        count = result[0][0]
        if count == 0:
            if log.log_check(pathlib.Path(f'{file[:-4]}errors.txt')):
                log.log_write(f'{file[:-4]}errors.txt', f'Could not add license because {org} does not exist. Please create this district and run again.')
            else:
                log.log_create(f'{file[:-4]}errors.txt', f'Could not add license because {org} does not exist. Please create this district and run again.')
        else:
            try:
                cursor.execute(query1)
                db.commit()
            except mysql.connector.errors.Error as e:
                print(e)
            try:
                cursor.execute(query2)
                result = cursor.fetchall()
                count = result[0][0]
                if count != 0:
                    query = f'select * from license where organization_id = "{org}" and start_date = "{start}" and end_date= "{end}"'
                    cursor.execute(query)
                    result1 = cursor.fetchall()
                    query = f'update license set status = "ACTIVE" where license_id = "{result1[0][0]}"'
                    try:
                        cursor.execute(query)
                        db.commit()
                    except mysql.connector.errors.Error as e:
                        print(e)
                else:
                    try:
                        cursor.execute(query3)
                        db.commit()
                    except mysql.connector.errors.Error as e:
                        print(e)
            except mysql.connector.errors.Error as e:
                print(e)
    except mysql.connector.errors.Error as e:
        print(e)


def insert_product(org, product, file):
    query = f'select count(*) from organization where organization_id = "{org}"'
    query1 = f'update organization set status = "ACTIVE" where organization_id = "{org}"'
    query2 = f'replace into organization_course (organization_id, course_id, create_date, update_date, active) values ("{org}","{product}", now(), now(), 1);'
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        count = result[0][0]
        if count == 0:
            if log.log_check(pathlib.Path(f'{file[:-4]}errors.txt')):
                log.log_write(f'{file[:-4]}errors.txt', f'Could not add product because {org} does not exist. Please create this district and run again.')
            else:
                log.log_create(f'{file[:-4]}errors.txt', f'Could not add product because {org} does not exist. Please create this district and run again.')
        else:
            try:
                cursor.execute(query1)
                db.commit()
            except mysql.connector.errors.Error as e:
                print(e)
            try:
                cursor.execute(query2)
                db.commit()
            except mysql.connector.errors.Error as e:
                print(e)
    except mysql.connector.errors.Error as e:
        print(e)

