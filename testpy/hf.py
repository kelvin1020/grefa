num_prec = 15
####final function######
hf0 = \
Sum([(xi(j, -2, hx0(e,Phi,Phip), hp0(e,Phi,Phip))*(j/2)**(2/3)*Exp(-sp.I* (fp(j, -2) + Pi/4))*UnitStep((j - (j - 2)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, -2)},n=num_prec) for j in range(1, 8+1)]) + \
Sum([(xi(j, 2, hx0(e,Phi,Phip), hp0(e,Phi,Phip))*(j/2)**(2/3)*Exp(-sp.I* (fp(j, 2) + Pi/4))*UnitStep((j - (j + 2)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, 2)},n=num_prec) for j in range(1, 4+1)]) +\
Sum([(xi(j, 0, hx0(e,Phi,Phip), hp0(e,Phi,Phip))*(j/2)**(2/3)*Exp(-sp.I* (fp(j, 0) + Pi/4))*UnitStep((j - j*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, 0)},n=num_prec) for j in range( 1, 6+1)]);   
# (* Newtonian amplitude of the frequency domain GW waveform *)


hf05 = \
Sum([(xi(j, -1, hx05(e,Phi,Phip), hp05(e,Phi,Phip))*(j/2)**(1/3)*Exp(-sp.I* (fp(j, -1) + Pi/4))*UnitStep((j - (j - 1)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, -1)},n=num_prec) for j in range( 1, 7+1)]) + \
Sum([(xi(j, 1, hx05(e,Phi,Phip), hp05(e,Phi,Phip))*(j/2)**(1/3)*Exp(-sp.I* (fp(j, 1) + Pi/4))*UnitStep((j - (j + 1)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, 1)},n=num_prec) for j in range(1, 5+1)]) + \
Sum([(xi(j, -3, hx05(e,Phi,Phip), hp05(e,Phi,Phip))*(j/2)**(1/3)*Exp(-sp.I* (fp(j, -3) + Pi/4))*UnitStep((j - (j - 3)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, -3)},n=num_prec) for j in range( 1, 9+1)]) + \
Sum([(xi(j, 3, hx05(e,Phi,Phip), hp05(e,Phi,Phip))*(j/2)**(1/3)*Exp(-sp.I* (fp(j, 3) + Pi/4))*UnitStep((j - (j + 3)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, 3)},n=num_prec) for j in range(1, 3+1)]); 
#(* 0.5PN amplitude of the frequency domain GW waveform *)


hf1 = \
Sum([((xi(j, -2, hx1(e,Phi,Phip), hp1(e,Phi,Phip)) + xipn(j, -2))*Exp(-sp.I* (fp(j, -2) + Pi/4))*UnitStep((j - (j - 2)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, -2)},n=num_prec) for j in range( 1, 8+1)]) + \
Sum([((xi(j, 2, hx1(e,Phi,Phip), hp1(e,Phi,Phip)) + xipn(j, 2))*Exp(-sp.I* (fp(j, 2) + Pi/4))*UnitStep((j - (j + 2)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, 2)},n=num_prec) for j in range(1, 4+1)]) + \
Sum([((xi(j, 0, hx1(e,Phi,Phip), hp1(e,Phi,Phip)) + xipn(j, 0))*Exp(-sp.I* (fp(j, 0) + Pi/4))*UnitStep((j - j*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, 0)},n=num_prec) for j in range( 1, 6+1)]) + \
Sum([(xi(j, -4, hx1(e,Phi,Phip), hp1(e,Phi,Phip))*Exp(-sp.I* (fp(j, -4) + Pi/4))*UnitStep((j - (j - 4)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, -4)},n=num_prec) for j in range( 1, 10+1)]) + \
Sum([(xi(j, 4, hx1(e,Phi,Phip), hp1(e,Phi,Phip))*Exp(-sp.I* (fp(j, 4) + Pi/4))*UnitStep((j - (j + 4)*k(j)/(1 + k(j))) * ff - 2 * f)).evalf(subs={e:et(j, 4)},n=num_prec) for j in range(1, 2+1)]); 
