import time

t_start = time.time()

def time_report(t0):
    tseconds = time.time() - t0
    seconds = "%0.1f" % tseconds
    minutes = "%0.1f" % (tseconds / 60.)
    hours = "%0.2f" % (tseconds / 3600.)
    print "Time s:{}, m:{}, h:{}".format(seconds, minutes, hours)
    
def time_report_wrapper(func):
    def inner(*args,**kwargs):
        t_start = time.time()
        #print "Arguments were: {}, {}".format(args, kwargs)
        result = func(*args,**kwargs)
        time_report(t_start)
        return result
    return inner

time_report(t_start)