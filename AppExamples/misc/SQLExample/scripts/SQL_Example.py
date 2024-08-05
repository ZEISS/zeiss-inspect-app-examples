# -*- coding: utf-8 -*-

import gom
import mysql.connector
from mysql.connector import Error
import pandas as pd

PW = 'SqlT3st!'
HOST_NAME =
USER_NAME
PASSWORD
DATABASE

DIALOG=gom.script.sys.create_user_defined_dialog (file='dialog.gdlg')
DIALOG=gom.script.sys.create_user_defined_dialog (file='dialog.gdlg')

#
# Event handler function called if anything happens inside of the dialog
#
def dialog_event_handler (widget):
	pass

DIALOG.handler = dialog_event_handler

RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)

#
# Event handler function called if anything happens inside of the dialog
#
def dialog_event_handler (widget):
	pass

DIALOG.handler = dialog_event_handler

RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)

def create_server_connection(host_name, user_name, user_password):
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host_name,
			user=user_name,
			passwd=user_password
		)
		print("MySQL Database connection successful")
	except Error as err:
		print(f"Error: '{err}'")

	return connection

def create_database(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		print("Database created successfully")
	except Error as err:
		print(f"Error: '{err}'")

def execute_query(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
		print("Query successful")
	except Error as err:
		print(f"Error: '{err}'")

connection = create_server_connection("localhost", "root", PW)


create_database_query = "CREATE DATABASE school"	# FIXME
create_database(connection, create_database_query)



