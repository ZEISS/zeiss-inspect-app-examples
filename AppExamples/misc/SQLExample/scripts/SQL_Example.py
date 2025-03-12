# -*- coding: utf-8 -*-
#
# sql_example.py
#
# Example for storing/loading project keywords to/from SQL database
#
# Table 'projects':
#  --------------------------------------------------------------------------------------------------
# | project_no (auto_increment) | project_name (unique) | company_name | department_name | part_name | 
#  --------------------------------------------------------------------------------------------------
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/main/python_examples/
# ---

import gom
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

PW = 'SqlT3st!' # Password for testing

# Database - projects table
TABLES = {}
TABLES['projects'] = (
    "CREATE TABLE `projects` ("
    "  `project_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `project_name` varchar(80) NOT NULL UNIQUE,"
    "  `company_name` varchar(80) NOT NULL,"
    "  `department_name` varchar(80),"
    "  `part_name` varchar(80) NOT NULL,"
    "  PRIMARY KEY (`project_no`)"
    ") ENGINE=InnoDB")

def create_server_connection(host_name, user_name, user_password, database):
    """Create server connection with specific database
    
    Parameters:
        host_name (string): hostname
        user_name (string): username
        user_password (string): password
        database (string): database name
        
    Returns:
    (connection, Error): MySQLConnection object, Error object
    """
    connection = None
    error = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
        error = err

    return connection, error


def create_database(host_name, user_name, user_password, database):
    """Connect to server and create database and default tables
    
    Parameters:
        host_name (string): hostname
        user_name (string): username
        user_password (string): password
        database (string): database name
        
    Returns:
    Error: Error object
    """
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
    except Error as err:
        print(f"Error: '{err}'")
        return err

    cursor = connection.cursor()
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        #return err
    else:
        print(f"Created database {database}")

    try:
        cursor.execute("USE {}".format(database))
    except mysql.connector.Error as err:
        print(f"Database {database} does not exists.")
        print(err)
    else:
        print(f"Using database {database}")

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
                return err
        else:
            print("OK")

    cursor.close()
    connection.close()
    return None


def execute_commit(connection, query, values):
    """Execute/commit transacion
    
    Parameters:
        connection (MySQLConnection): MySQLConnection object
        query (string): query string
        values (tuple): query parameters
        
    Returns:
    (mySQLCursor, Error): mySQLCursor object, Error object
    """
    cursor = connection.cursor(buffered=True)
    err = None
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        return None, err
    cursor.close()

    return cursor, err

def execute_query(connection, query, values):
    """Execute query transacion with a single row as result
    
    Parameters:
        connection (MySQLConnection): MySQLConnection object
        query (string): query string
        values (tuple): query parameters
        
    Returns:
    (dict, Error): Result dictionary, Error object
    """
    cursor = connection.cursor(buffered=True, dictionary=True)
    err = None
    try:
        cursor.execute(query, values)
        result = cursor.fetchone()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        return None, err
    cursor.close()

    return result, err

if not hasattr(gom.app, 'project'):
    gom.script.sys.execute_user_defined_dialog (file='no_project.gdlg')
    quit(0)

DIALOG=gom.script.sys.create_user_defined_dialog (file='main.gdlg')
DIALOG.width = 800
CONNECTION = None

#
# Event handler function called if anything happens inside of the dialog
#
def dialog_event_handler (widget):
    """Dialog event handler
    
    Parameters:
        widget (widget): widget object
    """
    global CONNECTION

    if str(widget) == 'initialize':
        # Initialize dialog
        # Disable buttons until connection is established
        DIALOG.bt_query.enabled = False
        DIALOG.bt_save.enabled = False
        DIALOG.bt_load.enabled = False
        DIALOG.bt_delete.enabled = False
        DIALOG.out_trans_status.value = "(Not connected)"

        # Init input fields from settings
        DIALOG.in_host.value = gom.api.settings.get ('dialog.in_host')
        DIALOG.in_user.value = gom.api.settings.get ('dialog.in_user')
        DIALOG.in_password.value = PW # TODO remove
        DIALOG.in_database.value = gom.api.settings.get ('dialog.in_database')

        # Update inputs fields from project valiables
        if 'user_project' in gom.app.project.project_keywords:
            DIALOG.project_zi.value = getattr(gom.app.project, 'user_project')
        if 'user_company' in gom.app.project.project_keywords:
            DIALOG.company_zi.value = getattr(gom.app.project, 'user_company')
        if 'user_department' in gom.app.project.project_keywords:
            DIALOG.department_zi.value = getattr(gom.app.project, 'user_department')        
        if 'user_company' in gom.app.project.project_keywords:
            DIALOG.part_zi.value = getattr(gom.app.project, 'user_part')

    elif widget == DIALOG.in_host:
        # Update settings from input field - 'host'
        gom.api.settings.set ('dialog.in_host', DIALOG.in_host.value)

    elif widget == DIALOG.in_user:
        # Update settings from input field - 'user'
        gom.api.settings.set ('dialog.in_user', DIALOG.in_user.value)

    elif widget == DIALOG.in_database:
        # Update settings from input field - 'database'
        gom.api.settings.set ('dialog.in_database', DIALOG.in_database.value)

    elif widget == DIALOG.bt_connect:
        # Connect to server and use specified database 
        DIALOG.out_conn_status.value = 'Connecting...'
        CONNECTION, err = create_server_connection(DIALOG.in_host.value, DIALOG.in_user.value, DIALOG.in_password.value, DIALOG.in_database.value)
        if err is None:
            DIALOG.out_conn_status.value = 'Connected'
            DIALOG.bt_query.enabled = True
            DIALOG.bt_save.enabled = True
            DIALOG.bt_load.enabled = True
            DIALOG.bt_delete.enabled = True
            DIALOG.out_trans_status.value = '(Ready)'
        else:
            DIALOG.out_conn_status.value = err.msg

    elif widget == DIALOG.bt_create:
        # Create database and tables
        DIALOG.out_conn_status.value = 'Creating database...'
        err = create_database(DIALOG.in_host.value, DIALOG.in_user.value, DIALOG.in_password.value, DIALOG.in_database.value)
        if err is None:
            DIALOG.out_conn_status.value = 'Database created'
        else:
            DIALOG.out_conn_status.value = err.msg

    elif widget == DIALOG.bt_query or widget == DIALOG.bt_load or widget == DIALOG.bt_delete:
        # Query database or load temporary project keywords from database
        # The actual project keywords are updated when the dialog is closed via 'Ok' button
        query = """SELECT company_name, department_name, part_name FROM projects
                WHERE project_name=%s"""
        values = (DIALOG.project_zi.value, )
        result, err = execute_query(CONNECTION, query, values)
        if err is not None:
            print(err.msg)
            DIALOG.out_trans_status.value = err.msg
            return

        print(f"Query result: {result}")
        if result is None:
            DIALOG.project_db.value = ""
            DIALOG.company_db.value = ""
            DIALOG.department_db.value = ""
            DIALOG.part_db.value = ""
            DIALOG.out_trans_status.value = "Project not found"
            return

        if widget == DIALOG.bt_query or widget == DIALOG.bt_load:
            DIALOG.project_db.value = DIALOG.project_zi.value
            DIALOG.company_db.value = result['company_name']
            DIALOG.department_db.value = result['department_name'] or ""
            DIALOG.part_db.value = result['part_name']
            DIALOG.out_trans_status.value = "Project found"

        if widget == DIALOG.bt_load:
            DIALOG.company_zi.value = result['company_name']
            DIALOG.department_zi.value = result['department_name'] or ""
            DIALOG.part_zi.value = result['part_name']
            DIALOG.out_trans_status.value = "Loaded"

        elif widget == DIALOG.bt_delete:
            try:
                gom.script.sys.execute_user_defined_dialog (file='delete_confirm.gdlg')
            except gom.BreakError:
                # Dialog window was closed or 'Cancel' button was pressed
                return

            query = """DELETE FROM projects WHERE project_name=%s"""
            values = (DIALOG.project_zi.value, )
            result, err = execute_query(CONNECTION, query, values)
            if err is None:
                DIALOG.project_db.value = ""
                DIALOG.company_db.value = ""
                DIALOG.department_db.value = ""
                DIALOG.part_db.value = ""
                DIALOG.out_trans_status.value = "Deleted"
            else:
                print(err.msg)
                DIALOG.out_trans_status.value = err.msg

    elif widget == DIALOG.bt_save:
        # Save project keywords to database
        query = """SELECT * FROM projects WHERE project_name=%s"""
        values = (DIALOG.project_zi.value, )
        result, err = execute_query(CONNECTION, query, values)
        if err is None and result is not None:
            # Project already exists, update
            query = """UPDATE projects SET company_name=%s, department_name=%s, part_name=%s
                    WHERE project_name=%s;"""
            values = (DIALOG.company_zi.value, DIALOG.department_zi.value, DIALOG.part_zi.value, DIALOG.project_zi.value)
            result, err = execute_commit(CONNECTION, query, values)
            if err is not None:
                print(err.msg)
                DIALOG.out_trans_status.value = err.msg
            else:
                DIALOG.out_trans_status.value = "Saved (updated)"            
        else:
            # New project, insert
            query = """INSERT INTO projects
                   (project_name, company_name, department_name, part_name)
                   VALUES (%s, %s, %s, %s)"""
            values = (DIALOG.project_zi.value, DIALOG.company_zi.value, DIALOG.department_zi.value, DIALOG.part_zi.value)
            result, err = execute_commit(CONNECTION, query, values)
            if err is not None:
                print(err.msg)
                DIALOG.out_trans_status.value = err.msg
            else:
                DIALOG.out_trans_status.value = "Saved (inserted)"

        if err is None:
            DIALOG.project_db.value = DIALOG.project_zi.value
            DIALOG.company_db.value = DIALOG.company_zi.value
            DIALOG.department_db.value = DIALOG.department_zi.value
            DIALOG.part_db.value = DIALOG.part_zi.value


DIALOG.handler = dialog_event_handler

try:
    RESULT = gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
except gom.BreakError as e:
    # Dialog window was closed or 'Cancel' button was pressed
    pass
else:
    # 'Ok' button was pressed
    gom.script.sys.set_project_keywords (keywords = {
        'project': RESULT.project_zi,
        'company': RESULT.company_zi,
        'department':  RESULT.department_zi,
        'part': RESULT.part_zi
    })
