# Import module 
import sqlite3
from functools import reduce

# Task 1: Create connection object
con = sqlite3.connect('hotel_booking.db')

# Task 2: Create cursor object
curs = con.cursor()

# Task 3: View first row of booking_summary
fetch_one = curs.execute("SELECT * FROM booking_summary").fetchone()

# Task 4: View first ten rows of booking_summary 
fetch_ten = curs.execute("SELECT * FROM booking_summary").fetchmany(10)

# Task 5: Create object bra and print first 5 rows to view data
bra = curs.execute("SELECT * FROM booking_summary WHERE country == 'BRA'").fetchall()
#print(bra[1:5])

# Task 6: Create new table called bra_customers
curs.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
  num INTEGER,
  hotel TEXT,
  is_cancelled INTEGER,
  lead_time INTEGER,
  arrival_date_year INTEGER,
  arrival_date_month INTEGER,
  arrival_date_day_of_month INTEGER,
  adults INTEGER,
  children INTEGER,
  country TEXT,
  adr REAL,
  special_requests INTEGER
)''')

# Task 7: Insert the object bra into the table bra_customers 
curs.executemany('''INSERT INTO bra_customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', bra)

# Task 8: View the first 10 rows of bra_customers
#print(curs.execute('''SELECT * FROM bra_customers''').fetchmany(10))

# Task 9: Retrieve lead_time rows where the bookings were canceled
lead_time_can = curs.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled == 1;''').fetchall()

# Task 10: Find average lead time for those who canceled and print results
lead_time_sum = 0
for num in lead_time_can:
  lead_time_sum += num[0]

lead_time_avg = lead_time_sum / len(lead_time_can)
#print(lead_time_avg)
# Task 11: Retrieve lead_time rows where the bookings were not canceled
lead_time = curs.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled == 0;''').fetchall()

# Task 12: Find average lead time for those who did not cancel and print results
lead_time_sum2 = 0
for num in lead_time:
  lead_time_sum2 += num[0]

lead_time_avg2 = lead_time_sum2 / len(lead_time_can)
#print(lead_time_avg2)

# Task 13: Retrieve special_requests rows where the bookings were canceled
special_requests_can = curs.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled == 1''').fetchall()
# Task 14: Find total speacial requests for those who canceled and print results
total_special_requests_can = 0
for num in special_requests_can:
  total_special_requests_can += num[0]
print(f'the number of special requests for those who cancelled: {total_special_requests_can}')
print(f'special requests per booking: {total_special_requests_can / len(special_requests_can)}')
# Task 15: Retrieve special_requests rows where the bookings were not canceled
special_requests = curs.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled == 0''').fetchall()

# Task 16: Find total speacial requests for those who did not cancel and print results
total_special_requests = 0
for num in special_requests:
  total_special_requests += num[0]
print(f'the number of special requests for those who did not cancel: {total_special_requests}')
print(f'special requests per booking: {total_special_requests / len(special_requests)}')
# Task 17: Commit changes and close the connection
con.commit()
con.close()
