import csv
import os
import pathlib
import sql
import log

substringSeats = 'Seats'
substringProducts = 'Products'

if __name__ == '__main__':
    os.chdir("order_entry")
    files = [f for f in os.listdir('.') if os.path.isfile(f) and '.csv' in f]
    for f in files:
        if substringSeats in f:
            seatsFile = pathlib.Path(f).absolute()
            seatsShort = f
            if log.log_check(pathlib.Path(f'{seatsShort[:-4]}errors.txt')):
                log.log_delete(f'{seatsShort[:-4]}errors.txt')
            with open(seatsFile, "r") as csvfile:
                csvreader = csv.DictReader(csvfile)
                for row in csvreader:
                    sql.insert_license(row['Org Id'], row['Quantity'], row['Opty#'], row['Product'], row['Start'], row['End'], seatsShort)
            if log.log_check(pathlib.Path(f'{seatsShort[:-4]}errors.txt')):
                pass
            else:
                log.move_file(seatsShort)
        if substringProducts in f:
            productsFile = pathlib.Path(f).absolute()
            productsShort = f
            if log.log_check(pathlib.Path(f'{productsShort[:-4]}errors.txt')):
                log.log_delete(f'{productsShort[:-4]}errors.txt')
            with open(productsFile, "r") as csvfile:
                csvreader = csv.DictReader(csvfile)
                for row in csvreader:
                    sql.insert_product(row['Org Id'], row['COURSE_ID'], productsShort)
            if log.log_check(pathlib.Path(f'{productsShort[:-4]}errors.txt')):
                pass
            else:
                log.move_file(productsShort)

