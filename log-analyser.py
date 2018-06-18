#!/usr/bin/env python

# A log analysing tool
# By 'Adam Spice'

import psycopg2
import sys


def connect(db_name="news"):
    """
    Connect to the PostgreSQL database.
    Returns a database connection and cursor.
    """
    try:
        db = psycopg2.connect(dbname=db_name)
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print("Unable to connect to database")
        sys.exit(1)
        raise e


def run_query(query):
    """
    Connect to the database using the connect function, query, fetch results,
    close connection, return results
    """
    db, c = connect()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_top_articles():
    """Fetch top articles using run_query function, print results"""
    # 1. What are the most popular three articles of all time?
    query1 = """
    SELECT title, count(log.path) as views FROM articles
    LEFT JOIN log ON CONCAT('/article/', articles.slug) = log.path
    WHERE status LIKE '%200%'
    GROUP BY title
    ORDER BY views DESC
    LIMIT 3;
    """
    results = run_query(query1)

    print('1. What are the most popular three articles of all time?')
    for i in results:
        print("- {} -- {} {}".format(str(i[0]), str(i[1]), 'views'))


def print_top_authors():
    """ Fetch top authors using run_queryfunction, print results"""
    # 2. Who are the most popular article authors of all time?
    query2 = """
    SELECT authors.name, count(log.path) AS views FROM articles
    JOIN authors ON authors.id = articles.author
    LEFT JOIN log ON CONCAT('/article/', articles.slug) = log.path
    WHERE status LIKE '%200%'
    GROUP BY authors.id
    ORDER BY views DESC;"""
    results = run_query(query2)
    print('2. Who are the most popular article authors of all time?')
    for i in results:
        print("- {} -- {} {}".format(str(i[0]), str(i[1]), 'views'))


def print_top_error_days():
    """ Fetch top error days using run_query function, print results"""
    # 3. On which days did more than 1% of requests lead to errors?
    query3 = """
    SELECT to_char(day, 'FMMonth DD,YYYY'),  -- For output style only
           error_percent
    FROM (SELECT error.day,
                 ROUND((error_count/total_count)*100, 1) AS error_percent
          FROM (SELECT CAST(time AS DATE) AS day,
                       CAST(count(status) AS DECIMAL) AS error_count
                FROM   log
                WHERE  status LIKE '404%'
                GROUP BY day) AS error,
               (SELECT CAST(time AS DATE) AS day,
                       CAST(count(status) AS DECIMAL) AS total_count
                FROM   log
                GROUP BY day) AS total
          WHERE error.day = total.day
          ORDER BY error_percent DESC) AS percent
    WHERE error_percent > 1.0;"""
    results = run_query(query3)

    print('3. On which days did more than 1% of requests lead to errors?')
    for i in results:
        print("- {} -- {} {}".format(str(i[0]), str(i[1]), '% errors'))


if __name__ == '__main__':
    print_top_articles()
    print("--------------------------------------------------------------")  # For output style only
    print_top_authors()
    print("--------------------------------------------------------------")  # For output style only
    print_top_error_days()
