from CoolProp.CoolProp import PropsSI

# Constructor inputs: fuel name, fuel temperature (K), fuel injection pressure (psi). 
class Fuel:
    def __init__(self, name, temp, ip):
        self.name = name
        self.temp = temp
        self.ip = ip*6895

        self.get_fuel_density()

    def get_fuel_density(self):
        self.dens = PropsSI('D', 'T', self.temp, 'P', self.ip, self.name)
        print(self.dens)

Fuel('Ethanol', 298, 925)