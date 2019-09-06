import numpy as np



#Variables
f = 100;                      #(* GW or Fourier \frequency *)

#Constans
Pi = np.pi 

#Functions
Cos = np.cos
Sin = np.sin
Sqrt = np.sqrt
Log = np.log
UnitStep = lambda x: np.heaviside(x, 1)


#Coefficients
Gamma = 0.5772156649;         #(* Euler-Gamma constant. Appears in 3PN corrections *) 
Fp = -0.5; Fc = 0.866025;     # (*  Choosing antenna patterns for \Theta=0^\(Degree), Phi= 30^\(Degree) and \(Psi)=30^\(Degree) *)
Phic = 0;                     #(* Orbital phase at coalescence *)
tc = 0;                       #(* \Time of coalescence *)
m1 = 10; m2 = 10;             #(* Mass of the binary \components in solar mass units *)
msun = 1.989e30;              #(* Solar mass in S.I. units  *)
m = (m1 + m2)* msun;          #(* Total mass of the binary in S.I. units *)
delta = (m1 - m2)* msun;      #(* Difference in the masses of the binary components in \S.I. units *)
Eta = (m1*m2*msun**2)/m**2;   #(* Symmetric mass ratio *)
G = 6.67408e-11;              #(* Gravitational constant in S.I. units *)
c = 299792458;                #(* Speed of light in vacuum in S.I. units *)
d = 100*3.086e22;             #(* Distance to the binary in S.I. units *)
f0 = 20.000;                  #(* Lower frequency cut-off of the GW detector *)


ff = c**3/(G*m*Pi*6**(3/2));  # (* Fourier frequency corresponding to second harmonic \of last stable orbit of the system *)
Chi = f/f0;                   #(* Ratio of Fourier frequency to the lower cut-off frequency \*)     
i = Pi/3; Beta = Pi/3;        #(* Choose any value for angles relating line of sight to the \orbital plane of the binary*)
Ci = Cos(i);                  #(* Defining variables as trigonometric functions of \angles iota and beta *)
Si = Sin(i);
S1Beta = Sin(Beta);
C1Beta = Cos(Beta);
S2Beta = Sin(2 * Beta);
C2Beta = Cos(2 * Beta);
S3Beta = Sin(3 * Beta);
C3Beta = Cos(3 * Beta);
S4Beta = Sin(4 * Beta);
C4Beta = Cos(4 * Beta);
et0 = 0.1;                    #(* Eccentricity at lower cut-off frequency of the \detector, f0 i.e. et0 = et(f0) *)


####begin function
k = np.pi / 3
l = np.pi / 5
e = 0.3

Phi = (1+k) * l 
Phip = k * l
##  ##



####internal function######




####final function######
hf0 = 0
hf05 = 0
hf1 = 0




if __name__ == '__main__':


	hf = (G**2*m**2*(hf0/(((f*G*m)/c**3)**1.1666666666666667*Pi**1.1666666666666667) + \
	(delta*hf05)/(m*((f*G*m)/c**3)**0.8333333333333334*Pi**0.8333333333333334) + hf1/(Sqrt((f*G*m)/c**3)*Sqrt(Pi)))*Sqrt((5*Pi)/6.)*Sqrt(Eta))/\
	(8.*c**5*d)


	print(hf)