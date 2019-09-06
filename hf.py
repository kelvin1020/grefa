hf0 = \
Sum([xi(j, -2, hx0, hp0)*(j/2)**(2/3)*Exp(-1j* (fp(j, -2) + Pi/4))*UnitStep((j - (j - 2)*k/(1 + k)) ff - 2 f) /. e -> et(j, -2), for j in range(1, 8+1)]) + \
Sum([xi(j, 2, hx0, hp0)*(j/2)**(2/3)*Exp(-1j* (fp(j, 2) + Pi/4))*UnitStep((j - (j + 2)*k/(1 + k)) ff - 2 f) /. e -> et(j, 2), for j in range(1, 4+1)]) +\
Sum([xi(j, 0, hx0, hp0)*(j/2)**(2/3)*Exp(-1j* (fp(j, 0) + Pi/4))*UnitStep((j - j*k/(1 + k)) ff - 2 f) /. e -> et(j, 0), for j in range( 1, 6+1)]);   
# (* Newtonian amplitude of the frequency domain GW waveform *)


hf05 = \
Sum([xi(j, -1, hx05, hp05)*(j/2)**(1/3)*Exp(-1j* (fp(j, -1) + Pi/4))*UnitStep((j - (j - 1)*k/(1 + k)) ff - 2 f) /. e -> et(j, -1), for j in range( 1, 7+1)]) + \
Sum([xi(j, 1, hx05, hp05)*(j/2)**(1/3)*Exp(-1j* (fp(j, 1) + Pi/4))*UnitStep((j - (j + 1)*k/(1 + k)) ff - 2 f) /. e -> et(j, 1), for j in range(1, 5+1)]) + \
Sum([xi(j, -3, hx05, hp05)*(j/2)**(1/3)*Exp(-1j* (fp(j, -3) + Pi/4))*UnitStep((j - (j - 3)*k/(1 + k)) ff - 2 f) /. e -> et(j, -3), for j in range( 1, 9+1)]) + \
Sum([xi(j, 3, hx05, hp05)*(j/2)**(1/3)*Exp(-1j* (fp(j, 3) + Pi/4))*UnitStep((j - (j + 3)*k/(1 + k)) ff - 2 f) /. e -> et(j, 3), for j in range(1, 3+1)]); 
#(* 0.5PN amplitude of the frequency domain GW waveform *)


hf1 = \
Sum([(xi(j, -2, hx1, hp1) + xipn(j, -2))*Exp(-1j* (fp(j, -2) + Pi/4))*UnitStep((j - (j - 2)*k/(1 + k)) ff - 2 f) /. e -> et(j, -2), for j in range( 1, 8+1)]) + \
Sum([(xi(j, 2, hx1, hp1) + xipn(j, 2))*Exp(-1j* (fp(j, 2) + Pi/4))*UnitStep((j - (j + 2)*k/(1 + k)) ff - 2 f) /. e -> et(j, 2), for j in range(1, 4+1)]) + \
Sum([(xi(j, 0, hx1, hp1) + xipn(j, 0))*Exp(-1j* (fp(j, 0) + Pi/4))*UnitStep((j - j*k/(1 + k)) ff - 2 f) /. e -> et(j, 0), for j in range( 1, 6+1)]) + \
Sum([xi(j, -4, hx1, hp1)*Exp(-1j* (fp(j, -4) + Pi/4))*UnitStep((j - (j - 4)*k/(1 + k)) ff - 2 f) /. e -> et(j, -4), for j in range( 1, 10+1)]) + \
Sum([xi(j, 4, hx1, hp1)*Exp(-1j* (fp(j, 4) + Pi/4))*UnitStep((j - (j + 4)*k/(1 + k)) ff - 2 f) /. e -> et(j, 4), for j in range(1, 2+1)]); 
#(* 1PN amplitude of the frequency domain GW waveform *)