
    def create_db(self, db_name):

	
        create_query = "CREATE DATABASE %s" % db_name
        use_query = "USE %s" % db_name

        try:
            self.curs.execute(create_query)
            self.curs.execute(use_query)
            print self.ip_addr + " Created database " + db_name
        except Exception, e:
            print self.ip_addr + " *** Failed to create database " + db_name
            print_exception(e)



"""error 2003 will detected in cluster when it does not properly config in master server"""