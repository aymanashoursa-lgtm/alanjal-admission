<<<<<<< HEAD
# Test export functionality
import sqlite3
from openpyxl import Workbook

DB = "exam.db"

print("Testing export...")
print("1. Checking database...")
conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM results")
count = cur.fetchone()[0]
print(f"   Results count: {count}")

print("2. Creating Excel file...")
wb = Workbook()
ws = wb.active
ws.append(['Name', 'Value'])
ws.append(['Test', 123])
file_path = "test_export.xlsx"
wb.save(file_path)
print(f"   Created test file: {file_path}")

conn.close()
print("All tests passed!")
=======
# Test export functionality
import sqlite3
from openpyxl import Workbook

DB = "exam.db"

print("Testing export...")
print("1. Checking database...")
conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM results")
count = cur.fetchone()[0]
print(f"   Results count: {count}")

print("2. Creating Excel file...")
wb = Workbook()
ws = wb.active
ws.append(['Name', 'Value'])
ws.append(['Test', 123])
file_path = "test_export.xlsx"
wb.save(file_path)
print(f"   Created test file: {file_path}")

conn.close()
print("All tests passed!")
>>>>>>> ddcfc68 (first commit)
