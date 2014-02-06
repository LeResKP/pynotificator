#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import SocketServer
import json
import models
import transaction


def insert_notification(data):
    dic = json.loads(data)
    if 'title' not in dic or 'msg' not in dic:
        return False

    with transaction.manager:
        notification = models.Notification(
            title=dic['title'],
            msg=dic['msg'],
        )
        models.DBSession.add(notification)
    print 'Notification added %(title)s %(msg)s' % dic


class TaskTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # print "{} wrote:".format(self.client_address[0])
        # print self.data
        insert_notification(self.data)
        self.request.sendall(self.data)


def main():
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), TaskTCPHandler)

    print 'Server running on %s:%s' % (HOST, PORT)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()


if __name__ == "__main__":
    main()
