import csv
import psycopg2
import argparse

conn = psycopg2.connect("dbname=panthers user=trishataylor host=/tmp/")

cur = conn.cursor()

cur.execute("CREATE TABLE roster (jersey INT, name TEXT NOT NULL, age INT, pos TEXT, games_played INT, games_started INT, weight INT, height varchar, college TEXT, bday date, years_in_NFL varchar, value INT, drafted TEXT, salary varchar);")

with open('roster.csv') as file:
    players = csv.reader(file, delimiter=',')
    for row in players:
        r = [row[column] for column in range(14)]
        cur.execute("INSERT INTO roster (jersey, name, age, pos, games_played, games_started, weight, height, college, bday, years_in_NFL, value, drafted, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", r)
