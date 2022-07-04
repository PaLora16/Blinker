from colorama import init
from blinker import signal

from bulbs import BulbFactory

# colorama init
init()

bf = BulbFactory()
# create list of 20 bulb objects
bulbs = bf.get_20_bulbs()

switcher = signal("switcher")
# subscribe all bulb object to send event
for bulb in bulbs:
    # each bulb class implement switcher interface (here function accepting payloads)
    switcher.connect(bulb.switcher)

# list object handling bulb status, implicit status - all bulbs are off
statuses = bf.get_bulbs_status_off()

# Switch on bulb 3 and bulb 11
statuses["bulb_3"] = "ON"
statuses["bulb_11"] = "ON"

# fan out required new bulb statuses at once to all connected bulbs.
# Each bulb class can implement differently switch on request
switcher.send(statuses)
