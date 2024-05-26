## Rocket Performance and Thrust Chamber Sizing
## Blake Westbrook 10/23/2020
## This program gives performance parameters and 
## system requirements for the fuel/ox combination 
## analyzed in CEA

# Design Conditions

## Assumes Quasi-1D, frozen flow past the combustion chamber
## Run NASA CEA, obtain the following TOTAL (chamber) conditions
# correct for syntax

import math
CEA_dat = [   4.8263E1 , 3.2054E3 , 4.6713 , 2.5795E1 , 1.1499,
   5.1710E1 , 3.2111E3 , 4.9984 , 2.5808E1 , 1.1504,
   5.5158E1 , 3.2164E3 , 5.3252 , 2.5819E1 , 1.1509,
   5.8605E1 , 3.2214E3 , 5.6516 , 2.5830E1 , 1.1513,
   6.2053E1 , 3.2261E3 , 5.9777 , 2.5840E1 , 1.1518,
   6.5500E1 , 3.2305E3 , 6.3035 , 2.5849E1 , 1.1522,
   6.8947E1 , 3.2346E3 , 6.6290 , 2.5858E1 , 1.1525]

# chamber pressure (bar), chamber temp (K), density(kg/m^3), 
#molar mass (1/n), ratio of specific heats

# number for the design case 0-6

d = 0

## SPECIFY THROAT RADIUS !!!!

Rt_in = 0.5 # inches

## SPECIFY DESIGN ATMOSPHERIC PRESSURE

atm = 101325 # Pa

pa = 1 * atm  #(Pa)


## Do not alter 

i = d*5


At_in = (Rt_in**2)*math.pi

At = At_in / 1550.0  # converts inches^2 to meters^2

Rt = Rt_in * 0.0254

R_univ = 8314.472 # J/kgmol*K

g0 = 9.81 # m/s^2


MW = CEA_dat[i + 3]        #obtains molecular weight of mixture
R = R_univ/MW           # obtains the gas constant for the mixture
gamma = CEA_dat[i + 4]    # obtains ratio of specific heats 

# useful parameter for further calculation

f_gam = (gamma*((gamma+1)/2)**-((gamma+1)/(gamma-1)))**0.5

pc = CEA_dat[i] * 14.5 * 6895 # converts pc in bar to Pa

pr = pc/pa #pressure ratio
Tc = CEA_dat[1] #K
Me = ((2/(gamma-1)) * (pr ** ((gamma-1)/gamma) -1))**0.5  #exit mach
Ve = (((2*gamma)/(gamma-1))*R*Tc*(1-(pr**((1-gamma)/gamma))))**0.5 #exit velocity


#area ratio calculation

Ae_At = (1/Me)*((2/(gamma+1))*(1+((gamma-1)/2)*Me**2))**(0.5*((gamma+1)/(gamma-1)))

## SPECIFY THROAT AREA

Te = Tc / (1+((gamma-1)/2)*Me**2) # exit temperature (K)
mdot = ((pc*At)/((R*Tc)**0.5))*f_gam # kg/s



Ae = At * Ae_At
pe = pa
Thrust = mdot*Ve+(pe-pa)*Ae # N



Isp = Thrust / (mdot*g0) #s


Dt = ((4/math.pi)*At)**0.5 #m
De = ((4/math.pi)*Ae)**0.5 #m

print("the nozzle throat diameter in inches is :", Dt * 39.37007874)
print("                               ")
print("the nozzle exit diameter in inches is:" , De * 39.37007874)
print("                               ")
print("The velocity at the exit of the nozzle in m/s is:",Ve)
print("                               ")
print("the required mass flow rate in kg/s is:",mdot)
print("                               ")
print("the required mass flow rate in lbm/s is:", mdot*2.205)
print("                               ")
print ("the total thrust in Newtons is :",Thrust)
print("                               ")
print("the total thrust in lbf is :", Thrust/4.448)
print("                               ")
print("The specific impulse(s) is :", Isp)
print("                               ")
print("the throat diameter in inches is :", Dt * 39.37007874)
print("                               ")
print("the exit diameter in inches is:" , De * 39.37007874)
print("                               ")



## CHAMBER AND NOZZLE SIZING
## produces nominal sizing for chamber and CONICAL nozzle
## user must provide contraction ratio, contraction angle,
# chamber length to diameter ratio, and expansion half angle

## The following parameters can be modified to ensure 
# practical design. However it is NOT recommended to 
# go outside of the suggested ranges unless
# absolutely necessary.

Ec = 6 # Contraction Ratio: typically 2-5
alpha = 15 #expansion half angle: typically 13-17 (degrees)
beta = 40 # contraction angle: typically 35 - 60 (degrees)
Lc_Dc = 4 # Chamber length/diameter: typically 3-5
R_c = Rt ## Throat contour radius. Typically 0.5-1.5*Rt




## Do not alter
B = beta * (math.pi/180)
A = alpha * (math.pi/180)

Ac = Ec * At
Dc = ((4/math.pi)*Ac)**0.5 #m
Lc = Dc * Lc_Dc



CL_n = (Rt*(((Ec)**0.5)-1)+R_c*((1/math.cos(B))-1))/math.tan(B)
# CL is the nozzle's CONVERGING LENGTH
DL_n = (Rt*(((Ec)**0.5)-1)+R_c*((1/math.cos(A))-1))/math.tan(A)
# DL is the nozzle's DIVERGING LENGTH
Vc = At*(Lc*Ec + (1/3)* (At/math.pi)**0.5*(1/math.tan(B))*((Ec)**(1/3)-1))
# Vc is the total chamber volume
L_char = Vc / At
#L_char is the "characteristic length" for use with comparison of other thrust chambers
L_t = Lc+CL_n+DL_n
#L_t is the total length of the chamber and nozzle 

print("The chamber diameter in inches is:", Dc * 39.37007874)
print("                               ")
print("The chamber length in inches is:", Lc * 39.37007874)
print("                               ")
print("The length of the convergent nozzle section  in inches is :" , CL_n * 39.37007874)
print("                               ")
print("The length of the divergent nozzle section in inches is :", DL_n * 39.37007874 )
print("                               ")
print("The total chamber volume in cubic inches is:",Vc/0.000016387064)
print("                               ")
print("The characteristic length (inches) of the chamber is :" , L_char / 0.000016387064)
print("                               ")
print("The total length of the chamber and nozzle in inches is:", L_t * 39.37007874)









