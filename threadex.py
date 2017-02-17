#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    "customer define thread"

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting: " + self.name
        self.print_time(self.name, self.counter, 3)
        print "Exiting " + self.name + "--the exitFlag =" + str(exitFlag)

    @staticmethod
    def print_time(threadName, delay, counter):
        while counter:
            if exitFlag:
                thread.exit()   #this line never be executed
            time.sleep(delay)
            print "%s: %s" % (threadName, time.ctime(time.time()))
            counter -= 1


# create new thread
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# start thread
thread1.start()
thread2.start()

print "Exiting Main Thread"
