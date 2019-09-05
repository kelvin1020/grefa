k = np.pi / 3
l = np.pi / 5
e = 0.3

Phi = (1+k) * l 
Phip = k * l

hx0 = Fc*(4*Ci*S2Beta*Cos(2*Phi) - 4*C2Beta*Ci*Sin(2*Phi) + e**6*((-65*Ci*S2Beta*Cos(2*Phi))/72. - (11*Ci*S2Beta*Cos(4*Phi - 6*Phip))/45. + \
(4096*Ci*S2Beta*Cos(8*Phi - 6*Phip))/45. - (11*Ci*S2Beta*Cos(2*Phi - 4*Phip))/120. - (2349*Ci*S2Beta*Cos(6*Phi - 4*Phip))/20. + \
(101*Ci*S2Beta*Cos(4*Phi - 2*Phip))/3. + (65*C2Beta*Ci*Sin(2*Phi))/72. - (11*C2Beta*Ci*Sin(4*Phi - 6*Phip))/45. - \
(4096*C2Beta*Ci*Sin(8*Phi - 6*Phip))/45. - (11*C2Beta*Ci*Sin(2*Phi - 4*Phip))/120. + (2349*C2Beta*Ci*Sin(6*Phi - 4*Phip))/20. - \
(101*C2Beta*Ci*Sin(4*Phi - 2*Phip))/3.) + e**2*\
(-10*Ci*S2Beta*Cos(2*Phi) + 16*Ci*S2Beta*Cos(4*Phi - 2*Phip) + 10*C2Beta*Ci*Sin(2*Phi) - 16*C2Beta*Ci*Sin(4*Phi - 2*Phip)) + \
e**4*((23*Ci*S2Beta*Cos(2*Phi))/4. - (Ci*S2Beta*Cos(2*Phi - 4*Phip))/4. + (81*Ci*S2Beta*Cos(6*Phi - 4*Phip))/2. - \
40*Ci*S2Beta*Cos(4*Phi - 2*Phip) - (23*C2Beta*Ci*Sin(2*Phi))/4. - (C2Beta*Ci*Sin(2*Phi - 4*Phip))/4. - \
(81*C2Beta*Ci*Sin(6*Phi - 4*Phip))/2. + 40*C2Beta*Ci*Sin(4*Phi - 2*Phip)) + \
e**3*((-7*Ci*S2Beta*Cos(Phi - 3*Phip))/24. + (625*Ci*S2Beta*Cos(5*Phi - 3*Phip))/24. - (171*Ci*S2Beta*Cos(3*Phi - Phip))/8. + \
(13*Ci*S2Beta*Cos(Phi + Phip))/8. - (7*C2Beta*Ci*Sin(Phi - 3*Phip))/24. - (625*C2Beta*Ci*Sin(5*Phi - 3*Phip))/24. + \
(171*C2Beta*Ci*Sin(3*Phi - Phip))/8. - (13*C2Beta*Ci*Sin(Phi + Phip))/8.) + \
e**5*((-153*Ci*S2Beta*Cos(3*Phi - 5*Phip))/640. + (117649*Ci*S2Beta*Cos(7*Phi - 5*Phip))/1920. - \
(47*Ci*S2Beta*Cos(Phi - 3*Phip))/384. - (26875*Ci*S2Beta*Cos(5*Phi - 3*Phip))/384. + (963*Ci*S2Beta*Cos(3*Phi - Phip))/64. + \
(5*Ci*S2Beta*Cos(Phi + Phip))/192. - (153*C2Beta*Ci*Sin(3*Phi - 5*Phip))/640. - (117649*C2Beta*Ci*Sin(7*Phi - 5*Phip))/1920. - \
(47*C2Beta*Ci*Sin(Phi - 3*Phip))/384. + (26875*C2Beta*Ci*Sin(5*Phi - 3*Phip))/384. - (963*C2Beta*Ci*Sin(3*Phi - Phip))/64. - \
(5*C2Beta*Ci*Sin(Phi + Phip))/192.) + e*(9*Ci*S2Beta*Cos(3*Phi - Phip) - 3*Ci*S2Beta*Cos(Phi + Phip) - \
9*C2Beta*Ci*Sin(3*Phi - Phip) + 3*C2Beta*Ci*Sin(Phi + Phip)))


# (* Newtonian amplitude of GW Cross polarisation accurate to e^6 with  antenna pattern Fc multiplied . 
# Here \[Phi] = (1+k)l and  \[Phi]' = k l are orbital phase and shifted  phase respectively 
# with l = mean anomaly and k = rate of advance of \ periastron  *)
# hx0