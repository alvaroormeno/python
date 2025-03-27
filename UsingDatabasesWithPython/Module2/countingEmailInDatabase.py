
import sqlite3


conn = sqlite3.connect('emaildb.sqlite')  # Connect to (or create) a SQLite database file
cur = conn.cursor()  # Create a cursor object to execute SQL commands


cur.execute('DROP TABLE IF EXISTS Counts')  # Delete the table if it already exists to start fresh


cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')  # Create a table named Counts with two columns:
# org (text) — stores the domain (e.g., gmail.com)
# count (integer) — tracks how many times the domain appears


# Open the text file containing email data
fh = open('UsingDatabasesWithPython/Module2/mbox.txt')


for line in fh:
    # Skip lines that don't start with 'From: '
    if not line.startswith('From: '): continue
    # print(line)

    pieces = line.split()
    email = pieces[1]
    print(email)

    emailOrg = email.split('@')[1]
    print(emailOrg)
    
    # Try to fetch the current count for this domain
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (emailOrg,))
    row = cur.fetchone()


    if row is None:
        # First time seeing this domain, insert it with count = 1
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (emailOrg,))
    else:
        # Domain already exists, increment count by 1
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (emailOrg,))
        
    # Save (commit) changes to the database after each update
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()