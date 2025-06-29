#!/usr/bin/env python3
"""
Script to create the 'alx_book_store' database in MySQL server.
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (replace with your actual username/password)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # <-- replace with your real password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
