from decimal import Decimal
import datetime

class PowerMeter:
    def __init__(self,tarrif1 = Decimal(6.5), tarrif2: Decimal=(8), tarrif2_starts: datetime.time = datetime.time(17), tarrif2_ends: datetime.time = datetime.time(20), power = Decimal(), charges : dict[datetime.date,Decimal] = dict()):
        self.tarrif1 = Decimal(tarrif1)
        self.tarrif2 = Decimal(tarrif2)
        self.tarrif2_starts = tarrif2_starts
        self.tarrif2_ends = tarrif2_ends
        self.power = Decimal(power)
        self.charges = charges
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: {float(self.power)} кВт/ч>'
    def __str__(self):
        return f"({datetime.date.today().strftime('%b')}) {self.charges[datetime.date.today().strftime('%Y,%m')]:.2f}"
    
    def meter(self, numb):
        today = datetime.datetime.today()
        if self.tarrif2_starts <= datetime.time(today.hour )<= self.tarrif2_ends:
            res1 = Decimal(numb)* self.tarrif2
            self.power += Decimal(numb)
            self.charges[today.strftime('%Y,%m')] = self.charges.get(today.strftime('%Y,%m'), Decimal(0)) + res1
            return f'{res1:.2f}'
        else:
            res1 = Decimal(numb)* self.tarrif1
            self.power += Decimal(numb)
            self.charges[today.strftime('%Y,%m')] = self.charges.get(today.strftime('%Y,%m'), Decimal(0)) + res1
            return f'{res1:.2f}'
            
# ПРОВЕРКА:
# >>> pm1 = PowerMeter()
# >>> pm1.meter(2)
# '16.00'
# >>> pm1.meter(1.2)
# '9.60'
# >>> pm1
# <PowerMeter: 3.2 кВт/ч>
# >>> print(pm1)
# (Feb) 25.60