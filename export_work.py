from timer.models import WorkSession as w
from datetime import datetime as d
from pprint import pprint

def pretty_print(td):
    hm = td.seconds//3600, (td.seconds//60)%60
    return "%s hours %s minutes" % (hm[0], hm[1])

ws = w.objects.filter(start__gte=d(2013, 5, 18))
hours = [(str(s.start.month)+'/'+str(s.start.day), s.stop-s.start) for s in ws]

totals = {}
for hour in hours:
    if not hour[0] in totals: totals[hour[0]] = hour[1]
    else: totals[hour[0]] = totals[hour[0]] + hour[1]

for k, v in totals.iteritems():
    totals[k] = pretty_print(v)


pprint(totals)