#!/usr/bin/env python





import MySQLdb
import sys

import db_cluster_utils


def print_exception(e):
    """
    print exception messages
    """

    line_number = sys.exc_info()[2].tb_lineno
    print "Line: " + str(line_number)
    print e





def query (server, query):

    try:

        server.curs.execute (query)
        server.conn.commit()

        print "Done"

    except Exception, e:
        server.conn.rollback()
        print "Query Failed: " + query
        print_exception(e)





def main(argv):
    """
    the program starts here
    """

    cluster = db_cluster_utils.db_cluster()
    server = db_cluster_utils.db_server (cluster.master_ip, cluster.root_password)

    query(server, "Use %s;" % cluster.database_name)


    # create tables
    query(server, """CREATE TABLE pages (
                            path TEXT, 
                            title TEXT, 
                            category TEXT,
                            description TEXT,
                            tags TEXT,
                            status TEXT,
                            pubdate DATETIME, 
                            updated DATETIME
                          )""")


    query(server, """CREATE TABLE categories (
                            name TEXT,
                            path TEXT,
                            description TEXT,
                            tags TEXT,
                            status TEXT,
                            pubdate DATETIME, 
                            updated DATETIME
                          )""")


    query(server, """CREATE TABLE users (
                            username TEXT, 
                            password TEXT,
                            email_addr TEXT,
                            joined DATETIME
                          )""")


    query(server, "INSERT INTO users VALUES ('suhail', '123456', 'mahammad.suhail.94@gmail.com', CURRENT_DATE());")



if __name__ == "__main__":
    main(sys.argv[1:])

