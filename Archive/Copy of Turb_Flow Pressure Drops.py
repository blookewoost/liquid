## Turbulent Flow Analysis.... Pipe Network for Injector Geometries

## Blake Westbrook/Space Cowboys Design Team


Oxidizer = 'NitrousOxide'
Fuel = 'Ethanol'

import math
import sympy
from CoolProp.CoolProp import PropsSI

FuelTemp = 298 # Kelvin
OxTemp = 255 # Kelvin

InjectionP = 925 #psi
InjectionP = InjectionP*6895

E = 5*10E-6 # m

## Calculation of Colebrook Friction Factor

def findF(E,Re,D):
    for f in range(1,100000):
        f = f/100000
        eq_f = (1/math.sqrt(f)+2*math.log10((E/3.7*D)+(2.51/(Re*math.sqrt(f)))))
        if eq_f < 0.0000001:
            break
    return f


## Densities and Viscosities
Dens_Ox = PropsSI('D','T', OxTemp, 'P' , InjectionP, Oxidizer)
Dens_Fuel = PropsSI('D', 'T' , FuelTemp , 'P' , InjectionP, Fuel)

Visc_Fuel = PropsSI('V' , 'T' , FuelTemp , 'P' , InjectionP , Fuel)

# Data for Nitrous Oxide viscosity unavailable. Empirical Eq. Incoming!!
T_crit = 309.57 # Kelvin...Critical Temperature
b_1 = 1.6089
b_2 = 2.0439
b_3 = 5.24
b_4 = 0.0293423

var = (T_crit - b_3)/(OxTemp - b_3)


Visc_Ox = b_4*math.exp(b_1*(var-1)**(1/3) + b_2*(var-1)**(4/3))*0.001


## (Maximum Mixing Effeciency) Empirical Eq. from NASA SP LRE Injectors
mdot = 3.456 # kg/s

percfuel = 0.161

num_F = 3
num_O = 6

mdot_Fuel = (percfuel*mdot)/3
mdot_Ox = ((1-percfuel)*mdot)/6

D_Fuel = 2E-3 # meters
A_Fuel = math.pi*(D_Fuel/2)**2

A = sympy.Symbol('A')
eq1 = sympy.Eq(((mdot_Ox*2)/(mdot_Fuel))**2*(Dens_Fuel/Dens_Ox)*(A_Fuel/(2*A))**1.75 - 0.66,0)
A_Ox = sympy.solve(eq1,A) ## SUPPOSED TO BE WEIGHT FLOW RATE (wait it doesnt matter)


D_Ox = 2*math.sqrt(A_Ox[0]/math.pi)

## Free stream length / orifice diameter should be 5-7
## Orifice L/D should be at least 4 to produce a jet along its centerline
## Feed system pressure drop should be kept to less than 25% of orifice pressure drop

#DE_Fuel = 1.5*D_Fuel
#DE_Ox = 1.5*D_Ox

L_Ox = 12*D_Ox
L_Fuel = 14*D_Fuel
DE_Ox = 3*D_Ox
DE_Fuel= 1*D_Fuel
LE_Ox= 0.5*L_Ox
LE_Fuel= 0.8*L_Fuel




def pipedrop(P1,E,mdot,rho,Visc,D,L):
    Q = mdot/rho
    A = math.pi*(D/2)**2
    Velocity = Q/A
    Re = (rho*Velocity*D)/Visc
    f = findF(E,Re,D)
    Pdrop = f*(L/D)*0.5*rho*Velocity**2
    P = P1 - Pdrop
    return P

def squeezedrop(P1,D1,D2,rho,mdot):
    V1 = (mdot/rho)/(math.pi*(D1/2)**2)
    V2 = V1*(D1/D2)**2
    P2 = P1 + (rho/2)*(V1**2-V2**2)
    return P2


P_O = pipedrop(InjectionP,E,mdot_Ox,Dens_Ox,Visc_Ox,DE_Ox,LE_Ox)
P_F = pipedrop(InjectionP,E,mdot_Fuel,Dens_Fuel,Visc_Fuel,DE_Fuel,LE_Fuel)

P_Ox1 = squeezedrop(P_O,DE_Ox,D_Ox,Dens_Ox,mdot_Ox)
P_Fuel1 = squeezedrop(P_F,DE_Fuel,D_Fuel,Dens_Fuel,mdot_Fuel)

P_Oxe = pipedrop(P_Ox1,E,mdot_Ox,Dens_Ox,Visc_Ox,D_Ox,L_Ox)
P_Fuele = pipedrop(P_Fuel1,E,mdot_Fuel,Dens_Fuel,Visc_Fuel,D_Fuel,L_Fuel)



print("The pressure drop across the fuel orifices is:" , round((InjectionP-P_Fuele)/6895,3) , "psi")
print("The pressure drop across the oxidizer orifices is:" , round((InjectionP-P_Oxe)/6895,3) , "psi")

print("The pressure drop across the fuel orifices is " , round(((InjectionP-P_Fuele)/6895)/(P_Fuele/6895),3) , "of the chamber pressure")
print("The pressure drop across the oxidizer orifices is " , round(((InjectionP-P_Oxe)/6895)/(P_Oxe/6895),3) , "of the chamber pressure")


print("                                                                ")
print("The oxidizer orifices are " , round(L_Ox*39.370,3) , "inches in length")
print("The fuel orifices are " , round(L_Fuel*39.370,3) , "inches in length")
print("The oxidizer orifices are " , round(D_Ox*39.370,3) , "inches in diameter")
print("The fuel orifices are " , round(D_Fuel*39.370,3) , "inches in diameter")

print("                                              ")
print("The oxidizer entries are " , round(LE_Ox*39.370,3), " inches in length")
print("The fuel entries are " , round(LE_Fuel*39.370,3) , "inches in length")
print("The oxidizer entries are " , round(DE_Ox*39.370,3) , "inches in diameter")
print("The fuel entries are " , round(DE_Fuel*39.370,3) , "inches in diameter") 

print("                                                               ")

print("Total oxidizer element length is" , round((L_Ox+LE_Ox)*39.370,3) , "inches")  

print("Total fuel element length is" , round((L_Fuel+LE_Fuel)*39.370,3) , "inches")






    

"""
Created on Mon Feb  1 12:31:42 2021

@author: 12282
"""

