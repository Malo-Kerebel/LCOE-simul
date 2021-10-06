import numpy as np
import matplotlib.pyplot as plt


class source(object):
    def __init__(self, name, power, capacity_factor,
                 construction, monthly, lifespan,
                 maintenance=0, maintenance_year=-1):
        """
        power is the power of the power plant
        capacity_factor is the capacity factor of the power plant
        construction is the cost of construction of the power plant
        monthly is the monthly cost of the power plant
        lifespan is the lifespan of the plant
        maintenance is the cost of the maintenance
        on year maintenance_year
        """
        self.name = name
        self.power = power
        self.capacity_factor = capacity_factor
        self.construction = construction
        self.monthly = monthly
        self.lifespan = lifespan
        self.maintenance = maintenance
        self.maintenance_year = maintenance_year

    def __str__(self):
        return (self.name)

    def LCOE(self, year):

        LCOE = []
        cost = 0
        energy = 0
        for y in range(year):
            if y % self.lifespan == 0:
                cost += self.construction
            energy += self.power * 365.25 * 24 * self.capacity_factor
            cost += self.monthly * 12
            if y % self.lifespan == self.maintenance_year:
                cost += self.maintenance
            LCOE.append(cost/energy * 1000000)  # to get €/MWh

        print(self.name, LCOE[-1])

        return LCOE


solar = source("solar, 30 ans", 20.3, 0.15, 18.8, 0.02, 25)
EPR_flammanville_60 = source("Flammanville-3, 60 ans", 1630, 0.75, 19100,
                             10, 60, 1000, 40)
EPR_flammanville_40 = source("Flammanville-3, 40 ans", 1630, 0.75, 19100,
                             10, 40)
EPR_expertise = source("EPR_expertise, 60 ans", 1630, 0.75, 10000,
                       10, 60, 1000, 40)
# I theorize a monthly cost of 10M€ per month which seem rather
# high
year = 120
y = np.arange(year)
plt.plot(y, solar.LCOE(year), label=solar)
plt.plot(y, EPR_flammanville_60.LCOE(year), label=EPR_flammanville_60)
plt.plot(y, EPR_flammanville_40.LCOE(year), label=EPR_flammanville_40)
plt.plot(y, EPR_expertise.LCOE(year), label=EPR_expertise)
plt.legend()
plt.xlabel("years")
plt.ylabel("€/MWh")
plt.show()
