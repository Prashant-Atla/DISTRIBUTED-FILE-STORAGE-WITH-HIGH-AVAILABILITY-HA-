 def demote_master (self, slave_list, slave_password):
        """
        Make a host a slave
        """

        # Grant replication rights to slaves
        for host in slave_list:
            self.revoke_replication ('slave_user', host)
