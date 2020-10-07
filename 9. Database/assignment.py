# Top Organizational count
import sqlite3

conn = sqlite3.connect('assignment.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    dom = pieces[1].split("@")
    dom = dom[len(dom) - 1]
    # print(email)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (dom,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (dom,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (dom,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
# sqlstr = '''SELECT * FROM Counts'''

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()