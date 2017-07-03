    def __init__ (self, host, rt_password):

        try:
            self.conn = MySQLdb.connect(host, 'root', rt_password, '')
            self.curs = self.conn.cursor()
            self.ip_addr = host
        except Exception, e:
            self.ip_addr = host
            print self.ip_addr + " Failed to connect"
            print_exception(e)

#        print self.ip_addr + " Connected successfully"


    def __del__ (self):
        # close the connection to the database
        self.conn.close()
#        print self.ip_addr + " DB Connection closed\n"



    def init_server (self, db_name, usr_pass, slv_pass):

        self.create_db (db_name)
        self.create_users (usr_pass, slv_pass)
