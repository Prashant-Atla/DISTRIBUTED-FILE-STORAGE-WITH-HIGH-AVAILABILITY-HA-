    def grant_replication (self, user_name, ip, password):
        """
        Grant replication privileges on the master to a slave
        """

        query = "GRANT REPLICATION SLAVE ON *.* TO '%s'@'%s' IDENTIFIED BY '%s'" % (user_name, ip, password)

        try:
            self.curs.execute(query)
            self.curs.execute("FLUSH PRIVILEGES")
            print self.ip_addr + " Granted replication privilege to " + user_name + "@" + ip + " id'd by " + password
        except Exception, e:
            print self.ip_addr + " *** Couldn't grant replication privilege to " + user_name
            print_exception(e)
