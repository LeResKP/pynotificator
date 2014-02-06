# Daemon + logging
# http://www.gavinj.net/2012/06/building-python-daemon-process.html
import os
import sys
import time

from datetime import datetime
from daemon import runner
import models
import transaction

# http://galago-project.org/news/index.php
# sudo yum install notify-python
# Demo https://ole.im/blog/2011/oct/20/python-notify
import pynotify


if not pynotify.init("Daemon notificator"):
    sys.exit(1)


class DisplayNotification():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/tmp/mydaemon.pid'
        self.pidfile_timeout = 5

    def run(self):
        while True:
            notifications = models.Notification.query.filter_by(sent=False).all()
            for notification in notifications:
                n = pynotify.Notification(notification.title,
                                          notification.msg)
                n.show()
                with transaction.manager:
                    notification.sent = True
                    models.DBSession.add(notification)
                time.sleep(5)
                n.close()

            time.sleep(2)
        # n = pynotify.Notification("Moo title", "test")
        # n.show()
        # raise Exception('plop')

        # filepath = '/tmp/mydaemon/currenttime.txt'
        # dirpath = os.path.dirname(filepath)
        # while True:
        #     if not os.path.exists(dirpath) or not os.path.isdir(dirpath):
        #         os.makedirs(dirpath)
        #     f = open(filepath, 'w')
        #     f.write(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        #     f.close()
        #     time.sleep(10)


def main():
    app = DisplayNotification()
    daemon_runner = runner.DaemonRunner(app)
    daemon_runner.do_action()


if __name__ == '__main__':
    main()
