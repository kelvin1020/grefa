import numpy as np

#Constans
Pi = np.pi 

#Functions
Cos = np.cos
Sin = np.sin


#Variables
f = 100;                      #(* GW or Fourier \frequency *)


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
S1Beta = Sin( Beta);
C1Beta = Cos( Beta);
S2Beta = Sin(2 * Beta);
C2Beta = Cos(2 * Beta);
S3Beta = Sin(3 * Beta);
C3Beta = Cos(3 * Beta);
S4Beta = Sin(4 * Beta);
C4Beta = Cos(4 * Beta);
et0 = 0.1;                    #(* Eccentricity at lower cut-off frequency of the \detector, f0 i.e. et0 = et(f0) *)



k = np.pi / 3
l = np.pi / 5
e = 0.3

Phi = (1+k) * l 
Phip = k * l

Log = np.log

x = lambda j,n:((f*G*m)/(c**3*(j - (k*(j + n))/(1 + k))))**0.6666666666666666*(2*Pi)**0.6666666666666666


def et(j, n):
    return x(j,n)**1.5*(et0**5*((94739615555*Pi)/(9.58169088e8*Chi**6.277777777777778) - (1586634546601*Pi)/(2.7786903552e10*Chi**5.277777777777778) - \
    (1422200801*Pi)/(1.3307904e7*Chi**4.166666666666667) + (1318556431*Pi)/(2.6615808e7*Chi**3.1666666666666665) + \
    (607032981553*Pi)/(2.7786903552e10*Chi**2.0555555555555554) - (6029825087*Pi)/(9.58169088e8*Chi**1.0555555555555556)) + \
    et0**3*((-1252771*Pi)/(87552.*Chi**4.166666666666667) + (396797*Pi)/(43776.*Chi**3.1666666666666665) + (1315151*Pi)/(131328.*Chi**2.0555555555555554) - \
    (1252771*Pi)/(262656.*Chi**1.0555555555555556)) + et0*((377*Pi)/(144.*Chi**2.0555555555555554) - (377*Pi)/(144.*Chi**1.0555555555555556))) + \
    x(j,n)*(et0*((1.4052579365079365 - (197*Eta)/72.)/Chi**1.7222222222222223 + (-1.4052579365079365 + (197*Eta)/72.)/Chi**1.0555555555555556) + \
    et0**3*((-7.680381781276107 + (654631*Eta)/43776.)/Chi**3.8333333333333335 + (2.148560817608926 - (378697*Eta)/43776.)/Chi**3.1666666666666665 + \
    (8.09194822409255 - (1482433*Eta)/131328.)/Chi**1.7222222222222223 + (-2.560127260425369 + (654631*Eta)/131328.)/Chi**1.0555555555555556) + \
    et0**5*((53.07214625052841 - (49505846855*Eta)/4.79084544e8)/Chi**5.944444444444445 + \
    (-6.782320707168325 + (24493152461*Eta)/4.79084544e8)/Chi**5.277777777777778 + \
    (-72.21077256816866 + (3092267495*Eta)/2.6615808e7)/Chi**3.8333333333333335 + \
    (11.742874337030365 - (1258410131*Eta)/2.6615808e7)/Chi**3.1666666666666665 + \
    (17.55591792187236 - (11147601665*Eta)/4.79084544e8)/Chi**1.7222222222222223 + \
    (-3.377845234094155 + (3150863507*Eta)/4.79084544e8)/Chi**1.0555555555555556)) + \
    x(j,n)**2.5*(et0**5*(((158961967498087*Pi)/2.75952697344e11 - (773693508027443*Pi*Eta)/4.82917220352e11)/Chi**6.944444444444445 + \
    ((-171498319127425*Pi)/1.931668881408e12 + (46169592388985*Pi*Eta)/6.8988174336e10)/Chi**6.277777777777778 + \
    ((-22474678352603165*Pi)/5.6018397560832e13 + (1562835028401985*Pi*Eta)/2.000657055744e12)/Chi**5.944444444444445 + \
    ((966616778184203239*Pi)/2.392785838669824e15 - (102851838418889831*Pi*Eta)/3.22105785974784e14)/Chi**5.277777777777778 + \
    ((-156129856813559*Pi)/1.7885822976e11 + (70761454761383*Pi*Eta)/4.471455744e10)/Chi**4.833333333333333 + \
    ((697744454755*Pi)/5.536088064e9 - (162077392939*Pi*Eta)/3.19389696e8)/Chi**4.166666666666667 + \
    ((83537422031093*Pi)/2.32515698688e11 - (369245400305*Pi*Eta)/6.38779392e8)/Chi**3.8333333333333335 + \
    ((-6837459307169*Pi)/1.987313664e10 + (7877941103477*Pi*Eta)/4.471455744e10)/Chi**3.1666666666666665 + \
    ((3611887558130624419*Pi)/1.196392919334912e16 - (517791739629486467*Pi*Eta)/1.61052892987392e15)/Chi**2.7222222222222223 + \
    ((-1719724436739649*Pi)/5.6018397560832e13 + (119585497365941*Pi*Eta)/2.000657055744e12)/Chi**2.0555555555555554 + \
    ((-88784076847265*Pi)/1.931668881408e12 + (4202645827705*Pi*Eta)/6.8988174336e10)/Chi**1.7222222222222223 + \
    ((158367949859977*Pi)/9.65834440704e12 - (3240255264059*Pi*Eta)/2.41458610176e12)/Chi**1.0555555555555556) + \
    et0**3*(((-12693032573*Pi)/2.9417472e8 + (11292740311*Pi*Eta)/7.354368e7)/Chi**4.833333333333333 + \
    ((330949595*Pi)/1.9611648e7 - (142768769*Pi*Eta)/2.101248e6)/Chi**4.166666666666667 + \
    ((1124125901*Pi)/2.9417472e7 - (78169009*Pi*Eta)/1.050624e6)/Chi**3.8333333333333335 + \
    ((-2057616403*Pi)/3.268608e7 + (2370731599*Pi*Eta)/7.354368e7)/Chi**3.1666666666666665 + \
    ((195499289159*Pi)/2.64757248e9 - (65776041763*Pi*Eta)/6.6189312e8)/Chi**2.7222222222222223 + \
    ((-3725822783*Pi)/2.64757248e8 + (259084747*Pi*Eta)/9.455616e6)/Chi**2.0555555555555554 + \
    ((-11217854617*Pi)/5.29514496e8 + (558877241*Pi*Eta)/1.8911232e7)/Chi**1.7222222222222223 + \
    ((32902907141*Pi)/2.64757248e9 - (673203247*Pi*Eta)/6.6189312e8)/Chi**1.0555555555555556) + \
    et0*(((778843*Pi)/1.45152e6 - (4996241*Pi*Eta)/362880.)/Chi**2.7222222222222223 + \
    ((-1068041*Pi)/290304. + (74269*Pi*Eta)/10368.)/Chi**2.0555555555555554 + ((-1068041*Pi)/290304. + (74269*Pi*Eta)/10368.)/Chi**1.7222222222222223 + \
    ((9901567*Pi)/1.45152e6 - (202589*Pi*Eta)/362880.)/Chi**1.0555555555555556)) + \
    x(j,n)**2*(et0*((-1.183105878829155 + (27565*Eta)/145152. + (33811*Eta**2)/10368.)/Chi**2.388888888888889 + \
    (-1.9747498681185438 + (558101*Eta)/72576. - (38809*Eta**2)/5184.)/Chi**1.7222222222222223 + \
    (3.157855746947699 - (1143767*Eta)/145152. + (43807*Eta**2)/10368.)/Chi**1.0555555555555556) + \
    et0**3*((-4.326698974356313 + (1205846917*Eta)/2.9417472e7 - (13714021*Eta**2)/233472.)/Chi**4.5 + \
    (9.057846423044774 - (10345778159*Eta)/1.91213568e8 + (74603309*Eta**2)/1.050624e6)/Chi**3.8333333333333335 + \
    (6.0635658127542085 + (14604819923*Eta)/2.676989952e9 - (317361763*Eta**2)/1.4708736e7)/Chi**3.1666666666666665 + \
    (-5.1764841086393485 - (385200824731*Eta)/2.4092909568e10 + (4301644427*Eta**2)/1.32378624e8)/Chi**2.388888888888889 + \
    (-11.371274463717358 + (65400285919*Eta)/1.720922112e9 - (292039301*Eta**2)/9.455616e6)/Chi**1.7222222222222223 + \
    (5.753045310914037 - (3800737741*Eta)/2.64757248e8 + (145570661*Eta**2)/1.8911232e7)/Chi**1.0555555555555556) + \
    et0**5*((104.47794356654612 - (79153315354555*Eta)/1.37976348672e11 + (47507268174605*Eta**2)/6.8988174336e10)/Chi**6.611111111111111 + \
    (-47.65455000845204 + (2837648691484435*Eta)/6.277923864576e12 - (24125755174085*Eta**2)/3.4494087168e10)/Chi**5.944444444444445 + \
    (-41.34875431268422 - (1089957759112387*Eta)/8.7890934104064e13 + (1121044759543031*Eta**2)/6.277923864576e12)/Chi**5.277777777777778 + \
    (-92.10881407017492 + (936816311138573*Eta)/1.627609890816e12 - (1951606822255*Eta**2)/2.980970496e9)/Chi**4.5 + \
    (85.16166339627074 - (55792908667709*Eta)/1.16257849344e11 + (352402173805*Eta**2)/6.38779392e8)/Chi**3.8333333333333335 + \
    (33.14017959832605 + (48531816604129*Eta)/1.627609890816e12 - (1054593138449*Eta**2)/8.942911488e9)/Chi**3.1666666666666665 + \
    (-24.587673108015718 - (4676818769915975*Eta)/8.7890934104064e13 + (669607180808035*Eta**2)/6.277923864576e12)/Chi**2.388888888888889 + \
    (-24.670592992393058 + (506837220151715*Eta)/6.277923864576e12 - (2196077528005*Eta**2)/3.4494087168e10)/Chi**1.7222222222222223 + \
    (7.590597930577053 - (18293673608177*Eta)/9.65834440704e11 + (700659277417*Eta**2)/6.8988174336e10)/Chi**1.0555555555555556)) + \
    et0**3*(-3323/(1824.*Chi**3.1666666666666665) + 3323/(1824.*Chi**1.0555555555555556)) + \
    et0**5*(50259743/(6.653952e6*Chi**5.277777777777778) - 11042329/(1.108992e6*Chi**3.1666666666666665) + 15994231/(6.653952e6*Chi**1.0555555555555556)) + \
    et0/Chi**1.0555555555555556 + x(j,n)**3*(et0**3*((5.102685770648402 - (318662569276073*Eta)/4.625838637056e12 + (4844584781833*Eta**2)/1.8356502528e10 - \
    (1562882519*Eta**3)/5.603328e6)/Chi**4.5 + (149592469*Pi**2)/(2.101248e6*Chi**4.166666666666667) + \
    (25.562621945733145 - (866895029665039*Eta)/3.2380870459392e13 - (5814138473063*Eta**2)/4.2831839232e10 + (62520267311*Eta**3)/3.53009664e8)/\
    Chi**3.8333333333333335 + (7.274295376872655 + (2420024232862595*Eta)/2.91427834134528e14 - (103398129181999*Eta**2)/1.156459659264e12 + \
    (847423952119*Eta**3)/9.531260928e9)/Chi**2.388888888888889 - (495811927*Pi**2)/(1.8911232e7*Chi**2.0555555555555554) + \
    (25.55320520345388 - (591234360321013*Eta)/5.947506819072e12 + (107636760191*Eta**2)/8.74119168e8 - (64940942431*Eta**3)/1.361608704e9)/\
    Chi**1.7222222222222223 + (2248.4766299647 - (95207357*Pi**2)/8.404992e6 - (245954159*Gamma)/766080. + (12374839994637661*Eta)/1.0793623486464e13 - \
    (116237911*Pi**2*Eta)/1.400832e6 - (3908281091711*Eta**2)/1.28495517696e11 - (42680326813*Eta**3)/1.059028992e9 - (33962745773*Log(2))/2.29824e6 + \
    (5362264233*Log(3))/680960. - (245954159*Log(x(j,n)))/1.53216e6)/Chi**3.1666666666666665 + \
    (-157.1562428930778 + (600535883*Pi**2)/7.5644928e7 + (11022391*Gamma)/459648. + (536131194179051*Eta)/1.601251835904e13 + \
    (13215571*Pi**2*Eta)/4.202496e6 - (1193082406697*Eta**2)/3.8125043712e10 + (35382609493*Eta**3)/4.084826112e9 + (40178393*Log(2))/6.89472e6 + \
    (28800441*Log(3))/680960. + (11022391*Log(x(j,n)))/919296.)/Chi**1.0555555555555556 + \
    (-1729.8025079772005 + (720177509*Pi**2)/7.5644928e7 + (517414657*Gamma)/2.29824e6 - (1395931720786001359*Eta)/1.45713917067264e15 + \
    (295851449*Pi**2*Eta)/4.202496e6 - (112681906698415*Eta**2)/3.469378977792e12 - (1549239851389*Eta**3)/2.8593782784e10 + \
    (101727523747*Log(2))/6.89472e6 - (5477465997*Log(3))/680960. + (517414657*Log(x(j,n)))/4.59648e6 - (517414657*Log(Chi))/6.89472e6)/\
    Chi**3.0555555555555554 + (-425.01068739112964 - (429547595*Pi**2)/8.404992e6 + (11022391*Gamma)/153216. - (62659748948903*Eta)/1.77916870656e12 + \
    (13215571*Pi**2*Eta)/1.400832e6 - (95613034561*Eta**2)/1.412038656e9 + (22151672941*Eta**3)/1.51289856e8 + (40178393*Log(2))/2.29824e6 + \
    (86401323*Log(3))/680960. + (11022391*Log(x(j,n)))/306432. - (11022391*Log(Chi))/459648.)/Chi**5.166666666666667) + \
    et0*((1.6625689259538672 - (6152132057*Eta)/1.755758592e9 - (1348031*Eta**2)/331776. + (6660767*Eta**3)/746496.)/Chi**2.388888888888889 - \
    (142129*Pi**2)/(20736.*Chi**2.0555555555555554) + (4.437601850745452 - (34611934451*Eta)/1.755758592e9 + (191583143*Eta**2)/6.967296e6 - \
    (8629979*Eta**3)/746496.)/Chi**1.7222222222222223 + \
    (-86.26331237946852 + (180721*Pi**2)/41472. + (3317*Gamma)/252. + (161339510737*Eta)/8.77879296e9 + (3977*Pi**2*Eta)/2304. - \
    (359037739*Eta**2)/2.0901888e7 + (10647791*Eta**3)/2.239488e6 + (12091*Log(2))/3780. + (26001*Log(3))/1120. + (3317*Log(x(j,n)))/504.)/\
    Chi**1.0555555555555556 + (80.1631416027692 + (103537*Pi**2)/41472. - (3317*Gamma)/252. + (866955547*Eta)/1.7915904e8 - (3977*Pi**2*Eta)/2304. - \
    (130785737*Eta**2)/2.0901888e7 - (4740155*Eta**3)/2.239488e6 - (12091*Log(2))/3780. - (26001*Log(3))/1120. - (3317*Log(x(j,n)))/504. + \
    (3317*Log(Chi))/756.)/Chi**3.0555555555555554) + et0**5*\
    ((-93.81285171640539 + (751550699250552365*Eta)/6.14880704987136e14 - (2712807799571918515*Eta**2)/6.02680690999296e14 + \
    (23151784966473335*Eta**3)/4.967148552192e12)/Chi**6.611111111111111 - (103131245529065*Pi**2)/(1.37976348672e11*Chi**6.277777777777778) + \
    (-290.5283258130814 + (6613733131933528864325*Eta)/1.3820673605995856e19 + (6008938601459478835*Eta**2)/4.218764836995072e15 - \
    (1104229088149885535*Eta**3)/4.52010518249472e14)/Chi**5.944444444444445 + \
    (108.62838799112515 - (5011810129939409773*Eta)/4.490147370369024e15 + (273844614114965969*Eta**2)/7.8125274759168e13 - \
    (222409764901445*Eta**3)/7.1543291904e10)/Chi**4.5 + (169823957639*Pi**2)/(3.19389696e8*Chi**4.166666666666667) + \
    (240.3391826262463 - (43622763718525097819*Eta)/2.5593840011103437e17 - (93995440212410537*Eta**2)/7.8125274759168e13 + \
    (295325748986095*Eta**3)/2.14629875712e11)/Chi**3.8333333333333335 + \
    (34.55202277530185 + (5456578161604350265*Eta)/7.274038739997819e17 - (95888813809642495*Eta**2)/3.24520372076544e14 + \
    (131912614619182895*Eta**3)/4.52010518249472e14)/Chi**2.388888888888889 - (7891428760189*Pi**2)/(1.37976348672e11*Chi**2.0555555555555554) + \
    (55.439056302526744 - (4595658861880171685*Eta)/2.1696504875974656e16 + (22172511125256925*Eta**2)/8.6097241571328e13 - \
    (488342986138655*Eta**3)/4.967148552192e12)/Chi**1.7222222222222223 + \
    (12288.960265415622 - (316374047311*Pi**2)/5.110235136e9 - (817305670357*Gamma)/4.6577664e8 + (41121593302180947503*Eta)/6.562523079770112e15 - \
    (386258578253*Pi**2*Eta)/8.51705856e8 - (12987218067755653*Eta**2)/7.8125274759168e13 - (141826725999599*Eta**3)/6.43889627136e11 - \
    (112858204203679*Log(2))/1.39732992e9 + (17818804046259*Log(3))/4.1402368e8 - (817305670357*Log(x(j,n)))/9.3155328e8)/Chi**3.1666666666666665 + \
    (-207.35276494666317 + (2890493420551*Pi**2)/2.75952697344e11 + (53052864227*Gamma)/1.676795904e9 + (2580501404154558247*Eta)/5.841366697377792e16 + \
    (63609056687*Pi**2*Eta)/1.5330705408e10 - (5742532535283709*Eta**2)/1.39080159461376e14 + (170303228893721*Eta**3)/1.4901445656576e13 + \
    (193386247021*Log(2))/2.515193856e10 + (46207333359*Log(3))/8.2804736e8 + (53052864227*Log(x(j,n)))/3.353591808e9)/Chi**1.0555555555555556 + \
    (-12981.634459807407 + (210263419125757*Pi**2)/1.37976348672e12 + (76993944487871*Gamma)/4.19198976e10 - \
    (459744548596452548880253*Eta)/6.910336802997928e19 + (36313178438959*Pi**2*Eta)/7.665352704e10 + \
    (15325478660942336659*Eta**2)/6.328147255492608e16 + (602052690061119545*Eta**3)/1.356031554748416e15 + \
    (11797275511817693*Log(2))/1.257596928e11 - (196321353899121*Log(3))/4.1402368e9 - (208984375*Log(5))/86016. + \
    (76993944487871*Log(x(j,n)))/8.38397952e10)/Chi**5.277777777777778 + \
    (-10128.268311299631 + (22839987538133*Pi**2)/1.37976348672e12 + (56669035748389*Gamma)/4.19198976e10 - \
    (332702882500991633514587*Eta)/6.910336802997928e19 + (29987633672981*Pi**2*Eta)/7.665352704e10 - \
    (9909009804994157899*Eta**2)/6.328147255492608e16 - (394569227909087057*Eta**3)/1.356031554748416e15 + \
    (8507394273435727*Log(2))/1.257596928e11 - (162397985681259*Log(3))/4.1402368e9 + (208984375*Log(5))/86016. + \
    (56669035748389*Log(x(j,n)))/8.38397952e10 - (56669035748389*Log(Chi))/1.257596928e11)/Chi**3.0555555555555554 + \
    (2985.9567896702633 + (168886055311895*Pi**2)/2.75952697344e11 - (833557837655*Gamma)/1.676795904e9 - (854950976221006253*Eta)/1.668961913536512e15 - \
    (999414989555*Pi**2*Eta)/1.5330705408e10 + (384051995415241885*Eta**2)/1.39080159461376e14 - (44332570043722025*Eta**3)/1.4901445656576e13 - \
    (607690552613*Log(2))/5.030387712e9 - (145200397527*Log(3))/1.65609472e8 - (833557837655*Log(x(j,n)))/3.353591808e9 + \
    (833557837655*Log(Chi))/5.030387712e9)/Chi**7.277777777777778 + \
    (7987.721008802102 - (2333251524667*Pi**2)/5.110235136e9 - (451031617427*Gamma)/4.6577664e8 + (41341286137777666139*Eta)/7.57214201511936e15 - \
    (298427893387*Pi**2*Eta)/8.51705856e8 - (142707649066100323*Eta**2)/7.8125274759168e13 + (1514475909193295*Eta**3)/6.43889627136e11 - \
    (112591178603801*Log(2))/1.39732992e9 + (18393027238917*Log(3))/4.1402368e8 - (451031617427*Log(x(j,n)))/9.3155328e8 + \
    (451031617427*Log(Chi))/1.39732992e9)/Chi**5.166666666666667))


et(2,3)

# (* 3PN accurate et upto order et0^5. For SPA et has to be computed at \
# the shifted harmonic of orbital frequency F by putting x = ((G m 2 \
# \[Pi] f)/( c^3(j-(j+n)*k/(1+k))))^(2/3)  *) 