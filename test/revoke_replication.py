 def revoke_replication (self, user_name, ip):
        """
        Grant replication privileges on the master to a slave
        """

        query = "REVOKE REPLICATION SLAVE ON *.* FROM '%s'@'%s'" % (user_name, ip)

        try:
            self.curs.execute(query)
            self.curs.execute("FLUSH PRIVILEGES")
            print self.ip_addr + " Revoked replication privilege from " + user_name + "@" + ip
        except Exception, e:
            print self.ip_addr + " *** Couldn't revoke replication privilege from " + user_name
            print_exception(e)
