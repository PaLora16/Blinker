from colorama import Fore
from typing import Dict, List
from threading import Thread


class Bulb:
    """class implementing switcher interface for switching on/off a bulb
        This is a demo usage as switcher interface can accept any payload type
        thus behavior of workers can vary wildely
    """

    def __init__(self, bulb_name):
        # bulb ID is bulb name
        self.bulb_name = bulb_name

    def get_name(self) -> str:
        return self.bulb_name

    # Action according to the requested state - here just print info in a given color
    def switcher(self, kwargs: Dict[str, str]) -> None:
        # here we accept ON/OFF, others options are discarded
        def on_off(status: str) -> None:
            if status == "ON":
                print(Fore.YELLOW +
                      f"{self.bulb_name} is on set by {self.bulb_name} objects")
                print(Fore.RESET)

            elif status == "OFF":
                print(Fore.WHITE + f"{self.bulb_name} is off")
                print(Fore.RESET)

        try:
            # according to key in parameters list we select correspondig payload  = worker behavior
            self.payload = kwargs[self.bulb_name]
        except:
            # silently discard exception, when there is no payload
            # for this worker
            pass
        else:
            # According to the payload - call action particular to this bulb,
            # In this demo actions are same for all bulb objects.
            # Here we accept payload ON/OFF, but other workers can
            # can accept completely differrent payloads.
            # In this demo threading may be overkill, but in other cases
            # as http requests, SQL SELECT etc may be reasanoble
            thread = Thread(target=on_off, args=(self.payload.upper(),))
            thread.start()
            thread.join()


class BulbFactory:
    """Helper class supporting main.py script
    """

    def __init__(self):
        def create_bulb(i: int) -> Bulb:
            return Bulb(i)

        # List bulb objects
        self.bulbs = list(map(lambda x: create_bulb(f"bulb_{x}"),
                              [i for i in range(1, 21)]))

        self.bulbs_status_off = {}
        # Implict bulb values - all bulbes OFF = dict {"bulb_1" : "OFF"}
        for bulb in self.bulbs:
            self.bulbs_status_off[bulb.get_name()] = "OFF"

    def get_20_bulbs(self) -> List[Bulb]:
        return self.bulbs

    def get_bulbs_status_off(self) -> Dict[str, str]:
        return self.bulbs_status_off
