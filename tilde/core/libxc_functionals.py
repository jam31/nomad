# libxc v2.2.1

libxc_functionals = {
1: {'comment': 'Exchange', 'name': 'XC_LDA_X'},
2: {'comment': 'Wigner parametrization', 'name': 'XC_LDA_C_WIGNER'},
3: {'comment': 'Random Phase Approximation', 'name': 'XC_LDA_C_RPA'},
4: {'comment': 'Hedin & Lundqvist', 'name': 'XC_LDA_C_HL'},
5: {'comment': 'Gunnarson & Lundqvist', 'name': 'XC_LDA_C_GL'},
6: {'comment': 'Slater Xalpha', 'name': 'XC_LDA_C_XALPHA'},
7: {'comment': 'Vosko, Wilk, & Nussair (5)', 'name': 'XC_LDA_C_VWN'},
8: {'comment': 'Vosko, Wilk, & Nussair (RPA)', 'name': 'XC_LDA_C_VWN_RPA'},
9: {'comment': 'Perdew & Zunger', 'name': 'XC_LDA_C_PZ'},
10: {'comment': 'Perdew & Zunger (Modified)', 'name': 'XC_LDA_C_PZ_MOD'},
11: {'comment': 'Ortiz & Ballone (PZ)', 'name': 'XC_LDA_C_OB_PZ'},
12: {'comment': 'Perdew & Wang', 'name': 'XC_LDA_C_PW'},
13: {'comment': 'Perdew & Wang (Modified)', 'name': 'XC_LDA_C_PW_MOD'},
14: {'comment': 'Ortiz & Ballone (PW)', 'name': 'XC_LDA_C_OB_PW'},
15: {'comment': 'Attaccalite et al', 'name': 'XC_LDA_C_2D_AMGB'},
16: {'comment': 'Pittalis, Rasanen & Marques correlation in 2D', 'name': 'XC_LDA_C_2D_PRM'},
17: {'comment': 'von Barth & Hedin', 'name': 'XC_LDA_C_vBH'},
18: {'comment': 'Casula, Sorella, and Senatore 1D correlation', 'name': 'XC_LDA_C_1D_CSC'},
19: {'comment': 'Exchange in 2D', 'name': 'XC_LDA_X_2D'},
20: {'comment': 'Teter 93 parametrization', 'name': 'XC_LDA_XC_TETER93'},
21: {'comment': 'Exchange in 1D', 'name': 'XC_LDA_X_1D'},
22: {'comment': 'Modified LSD (version 1) of Proynov and Salahub', 'name': 'XC_LDA_C_ML1'},
23: {'comment': 'Modified LSD (version 2) of Proynov and Salahub', 'name': 'XC_LDA_C_ML2'},
24: {'comment': 'Gombas parametrization', 'name': 'XC_LDA_C_GOMBAS'},
25: {'comment': 'Perdew & Wang fit of the RPA', 'name': 'XC_LDA_C_PW_RPA'},
26: {'comment': 'P-F Loos correlation LDA', 'name': 'XC_LDA_C_1D_LOOS'},
27: {'comment': 'Ragot-Cortona', 'name': 'XC_LDA_C_RC04'},
28: {'comment': 'Vosko, Wilk, & Nussair (1)', 'name': 'XC_LDA_C_VWN_1'},
29: {'comment': 'Vosko, Wilk, & Nussair (2)', 'name': 'XC_LDA_C_VWN_2'},
30: {'comment': 'Vosko, Wilk, & Nussair (3)', 'name': 'XC_LDA_C_VWN_3'},
31: {'comment': 'Vosko, Wilk, & Nussair (4)', 'name': 'XC_LDA_C_VWN_4'},
47: {'comment': 'Chiodo et al', 'name': 'XC_GGA_C_Q2D'},
48: {'comment': 'Chiodo et al', 'name': 'XC_GGA_X_Q2D'},
49: {'comment': 'Del Campo, Gazquez, Trickey and Vela (PBE-like)', 'name': 'XC_GGA_X_PBE_MOL'},
50: {'comment': 'Thomas-Fermi kinetic energy functional', 'name': 'XC_LDA_K_TF'},
51: {'comment': 'Lee and Parr Gaussian ansatz', 'name': 'XC_LDA_K_LP'},
52: {'comment': 'Thomas-Fermi plus von Weiszaecker correction', 'name': 'XC_GGA_K_TFVW'},
53: {'comment': 'interpolated version of REVAPBE', 'name': 'XC_GGA_K_REVAPBEINT'},
54: {'comment': 'interpolated version of APBE', 'name': 'XC_GGA_K_APBEINT'},
55: {'comment': 'revised APBE', 'name': 'XC_GGA_K_REVAPBE'},
56: {'comment': 'Armiento & Kuemmel 2013', 'name': 'XC_GGA_X_AK13'},
57: {'comment': 'Meyer,  Wang, and Young', 'name': 'XC_GGA_K_MEYER'},
58: {'comment': 'Berland and Hyldgaard', 'name': 'XC_GGA_X_LV_RPW86'},
59: {'comment': 'PBE revised by Tognetti et al', 'name': 'XC_GGA_X_PBE_TCA'},
60: {'comment': 'PBE for hybrid interfaces', 'name': 'XC_GGA_X_PBEINT'},
61: {'comment': 'spin-dependent gradient correction to PBEint', 'name': 'XC_GGA_C_ZPBEINT'},
62: {'comment': 'PBE for hybrid interfaces', 'name': 'XC_GGA_C_PBEINT'},
63: {'comment': 'spin-dependent gradient correction to PBEsol', 'name': 'XC_GGA_C_ZPBESOL'},
64: {'comment': 'oTPSS_D functional of Goerigk and Grimme', 'name': 'XC_MGGA_XC_OTPSS_D'},
65: {'comment': 'oPBE_D functional of Goerigk and Grimme', 'name': 'XC_GGA_XC_OPBE_D'},
66: {'comment': 'oPWLYP-D functional of Goerigk and Grimme', 'name': 'XC_GGA_XC_OPWLYP_D'},
67: {'comment': 'oBLYP-D functional of Goerigk and Grimme', 'name': 'XC_GGA_XC_OBLYP_D'},
68: {'comment': 'VMT{8,4} with constraint satisfaction with mu = mu_GE', 'name': 'XC_GGA_X_VMT84_GE'},
69: {'comment': 'VMT{8,4} with constraint satisfaction with mu = mu_PBE', 'name': 'XC_GGA_X_VMT84_PBE'},
70: {'comment': 'Vela, Medel, and Trickey with mu = mu_GE', 'name': 'XC_GGA_X_VMT_GE'},
71: {'comment': 'Vela, Medel, and Trickey with mu = mu_PBE', 'name': 'XC_GGA_X_VMT_PBE'},
72: {'comment': 'Colle and Salvetti', 'name': 'XC_MGGA_C_CS'},
73: {'comment': 'MN12-SX functional of Minnesota', 'name': 'XC_MGGA_C_MN12_SX'},
74: {'comment': 'MN12-L functional of Minnesota', 'name': 'XC_MGGA_C_MN12_L'},
75: {'comment': 'M11-L functional of Minnesota', 'name': 'XC_MGGA_C_M11_L'},
76: {'comment': 'M11 functional of Minnesota', 'name': 'XC_MGGA_C_M11'},
77: {'comment': 'M08-SO functional of Minnesota', 'name': 'XC_MGGA_C_M08_SO'},
78: {'comment': 'M08-HX functional of Minnesota', 'name': 'XC_MGGA_C_M08_HX'},
79: {'comment': 'N12-SX functional from Minnesota', 'name': 'XC_GGA_C_N12_SX'},
80: {'comment': 'N12 functional from Minnesota', 'name': 'XC_GGA_C_N12'},
81: {'comment': 'N12-SX functional from Minnesota', 'name': 'XC_HYB_GGA_X_N12_SX'},
82: {'comment': 'N12 functional from Minnesota', 'name': 'XC_GGA_X_N12'},
83: {'comment': 'variant PBE', 'name': 'XC_GGA_C_VPBE'},
84: {'comment': 'one-parameter progressive functional (XALPHA version)', 'name': 'XC_GGA_C_OP_XALPHA'},
85: {'comment': 'one-parameter progressive functional (G96 version)', 'name': 'XC_GGA_C_OP_G96'},
86: {'comment': 'one-parameter progressive functional (PBE version)', 'name': 'XC_GGA_C_OP_PBE'},
87: {'comment': 'one-parameter progressive functional (B88 version)', 'name': 'XC_GGA_C_OP_B88'},
88: {'comment': 'Filatov & Thiel correlation', 'name': 'XC_GGA_C_FT97'},
89: {'comment': 'PBE correlation to be used with the SSB exchange', 'name': 'XC_GGA_C_SPBE'},
90: {'comment': 'Swarta, Sola and Bickelhaupt correction to PBE', 'name': 'XC_GGA_X_SSB_SW'},
91: {'comment': 'Swarta, Sola and Bickelhaupt', 'name': 'XC_GGA_X_SSB'},
92: {'comment': 'Swarta, Sola and Bickelhaupt dispersion', 'name': 'XC_GGA_X_SSB_D'},
93: {'comment': 'HCTH/407+', 'name': 'XC_GGA_XC_HCTH_407P'},
94: {'comment': 'HCTH p=7/6', 'name': 'XC_GGA_XC_HCTH_P76'},
95: {'comment': 'HCTH p=1/4', 'name': 'XC_GGA_XC_HCTH_P14'},
96: {'comment': 'Becke 97 GGA-1', 'name': 'XC_GGA_XC_B97_GGA1'},
97: {'comment': 'HCTH-A', 'name': 'XC_GGA_XC_HCTH_A'},
98: {'comment': 'BPCCAC (GRAC for the energy)', 'name': 'XC_GGA_X_BPCCAC'},
99: {'comment': 'Tognetti, Cortona, Adamo (revised)', 'name': 'XC_GGA_C_REVTCA'},
100: {'comment': 'Tognetti, Cortona, Adamo', 'name': 'XC_GGA_C_TCA'},
101: {'comment': 'Perdew, Burke & Ernzerhof exchange', 'name': 'XC_GGA_X_PBE'},
102: {'comment': 'Perdew, Burke & Ernzerhof exchange (revised)', 'name': 'XC_GGA_X_PBE_R'},
103: {'comment': 'Becke 86 Xalfa,beta,gamma', 'name': 'XC_GGA_X_B86'},
104: {'comment': 'Herman et al original GGA', 'name': 'XC_GGA_X_HERMAN'},
105: {'comment': 'Becke 86 Xalfa,beta,gamma (with mod. grad. correction)', 'name': 'XC_GGA_X_B86_MGC'},
106: {'comment': 'Becke 88', 'name': 'XC_GGA_X_B88'},
107: {'comment': 'Gill 96', 'name': 'XC_GGA_X_G96'},
108: {'comment': 'Perdew & Wang 86', 'name': 'XC_GGA_X_PW86'},
109: {'comment': 'Perdew & Wang 91', 'name': 'XC_GGA_X_PW91'},
110: {'comment': 'Handy & Cohen OPTX 01', 'name': 'XC_GGA_X_OPTX'},
111: {'comment': 'dePristo & Kress 87 (version R1)', 'name': 'XC_GGA_X_DK87_R1'},
112: {'comment': 'dePristo & Kress 87 (version R2)', 'name': 'XC_GGA_X_DK87_R2'},
113: {'comment': 'Lacks & Gordon 93', 'name': 'XC_GGA_X_LG93'},
114: {'comment': 'Filatov & Thiel 97 (version A)', 'name': 'XC_GGA_X_FT97_A'},
115: {'comment': 'Filatov & Thiel 97 (version B)', 'name': 'XC_GGA_X_FT97_B'},
116: {'comment': 'Perdew, Burke & Ernzerhof exchange (solids)', 'name': 'XC_GGA_X_PBE_SOL'},
117: {'comment': 'Hammer, Hansen & Norskov (PBE-like)', 'name': 'XC_GGA_X_RPBE'},
118: {'comment': 'Wu & Cohen', 'name': 'XC_GGA_X_WC'},
119: {'comment': 'Modified form of PW91 by Adamo & Barone', 'name': 'XC_GGA_X_MPW91'},
120: {'comment': 'Armiento & Mattsson 05 exchange', 'name': 'XC_GGA_X_AM05'},
121: {'comment': 'Madsen (PBE-like)', 'name': 'XC_GGA_X_PBEA'},
122: {'comment': 'Adamo & Barone modification to PBE', 'name': 'XC_GGA_X_MPBE'},
123: {'comment': 'xPBE reparametrization by Xu & Goddard', 'name': 'XC_GGA_X_XPBE'},
124: {'comment': 'Becke 86 MGC for 2D systems', 'name': 'XC_GGA_X_2D_B86_MGC'},
125: {'comment': 'Bayesian best fit for the enhancement factor', 'name': 'XC_GGA_X_BAYESIAN'},
126: {'comment': 'JSJR reparametrization by Pedroza, Silva & Capelle', 'name': 'XC_GGA_X_PBE_JSJR'},
127: {'comment': 'Becke 88 in 2D', 'name': 'XC_GGA_X_2D_B88'},
128: {'comment': 'Becke 86 Xalfa,beta,gamma', 'name': 'XC_GGA_X_2D_B86'},
129: {'comment': 'Perdew, Burke & Ernzerhof exchange in 2D', 'name': 'XC_GGA_X_2D_PBE'},
130: {'comment': 'Perdew, Burke & Ernzerhof correlation', 'name': 'XC_GGA_C_PBE'},
131: {'comment': 'Lee, Yang & Parr', 'name': 'XC_GGA_C_LYP'},
132: {'comment': 'Perdew 86', 'name': 'XC_GGA_C_P86'},
133: {'comment': 'Perdew, Burke & Ernzerhof correlation SOL', 'name': 'XC_GGA_C_PBE_SOL'},
134: {'comment': 'Perdew & Wang 91', 'name': 'XC_GGA_C_PW91'},
135: {'comment': 'Armiento & Mattsson 05 correlation', 'name': 'XC_GGA_C_AM05'},
136: {'comment': 'xPBE reparametrization by Xu & Goddard', 'name': 'XC_GGA_C_XPBE'},
137: {'comment': 'Langreth and Mehl correlation', 'name': 'XC_GGA_C_LM'},
138: {'comment': 'JRGX reparametrization by Pedroza, Silva & Capelle', 'name': 'XC_GGA_C_PBE_JRGX'},
139: {'comment': 'Becke 88 reoptimized to be used with vdW functional of Dion et al', 'name': 'XC_GGA_X_OPTB88_VDW'},
140: {'comment': 'PBE reparametrization for vdW', 'name': 'XC_GGA_X_PBEK1_VDW'},
141: {'comment': 'PBE reparametrization for vdW', 'name': 'XC_GGA_X_OPTPBE_VDW'},
142: {'comment': 'Regularized PBE', 'name': 'XC_GGA_X_RGE2'},
143: {'comment': 'Regularized PBE', 'name': 'XC_GGA_C_RGE2'},
144: {'comment': 'refitted Perdew & Wang 86', 'name': 'XC_GGA_X_RPW86'},
145: {'comment': 'Keal and Tozer version 1', 'name': 'XC_GGA_X_KT1'},
146: {'comment': 'Keal and Tozer version 2', 'name': 'XC_GGA_XC_KT2'},
147: {'comment': 'Wilson & Levy', 'name': 'XC_GGA_C_WL'},
148: {'comment': 'Wilson & Ivanov', 'name': 'XC_GGA_C_WI'},
149: {'comment': 'Modified Becke 88 for proton transfer', 'name': 'XC_GGA_X_MB88'},
150: {'comment': 'Second-order generalized gradient approximation', 'name': 'XC_GGA_X_SOGGA'},
151: {'comment': 'Second-order generalized gradient approximation 2011', 'name': 'XC_GGA_X_SOGGA11'},
152: {'comment': 'Second-order generalized gradient approximation 2011', 'name': 'XC_GGA_C_SOGGA11'},
153: {'comment': 'Wilson & Ivanov initial version', 'name': 'XC_GGA_C_WI0'},
154: {'comment': 'Tozer and Handy v. 1', 'name': 'XC_GGA_XC_TH1'},
155: {'comment': 'Tozer and Handy v. 2', 'name': 'XC_GGA_XC_TH2'},
156: {'comment': 'Tozer and Handy v. 3', 'name': 'XC_GGA_XC_TH3'},
157: {'comment': 'Tozer and Handy v. 4', 'name': 'XC_GGA_XC_TH4'},
158: {'comment': 'C09x to be used with the VdW of Rutgers-Chalmers', 'name': 'XC_GGA_X_C09X'},
159: {'comment': 'To be used with hyb_gga_x_SOGGA11-X', 'name': 'XC_GGA_C_SOGGA11_X'},
160: {'comment': 'van Leeuwen & Baerends', 'name': 'XC_GGA_X_LB'},
161: {'comment': 'HCTH functional fitted to  93 molecules', 'name': 'XC_GGA_XC_HCTH_93'},
162: {'comment': 'HCTH functional fitted to 120 molecules', 'name': 'XC_GGA_XC_HCTH_120'},
163: {'comment': 'HCTH functional fitted to 147 molecules', 'name': 'XC_GGA_XC_HCTH_147'},
164: {'comment': 'HCTH functional fitted to 407 molecules', 'name': 'XC_GGA_XC_HCTH_407'},
165: {'comment': 'Empirical functionals from Adamson, Gill, and Pople', 'name': 'XC_GGA_XC_EDF1'},
166: {'comment': 'XLYP functional', 'name': 'XC_GGA_XC_XLYP'},
167: {'comment': 'Becke 97', 'name': 'XC_GGA_XC_B97'},
168: {'comment': 'Becke 97-1', 'name': 'XC_GGA_XC_B97_1'},
169: {'comment': 'Becke 97-2', 'name': 'XC_GGA_XC_B97_2'},
170: {'comment': 'Grimme functional to be used with C6 vdW term', 'name': 'XC_GGA_XC_B97_D'},
171: {'comment': 'Boese-Martin for Kinetics', 'name': 'XC_GGA_XC_B97_K'},
172: {'comment': 'Becke 97-3', 'name': 'XC_GGA_XC_B97_3'},
173: {'comment': 'Functionals fitted for water', 'name': 'XC_GGA_XC_PBE1W'},
174: {'comment': 'Functionals fitted for water', 'name': 'XC_GGA_XC_MPWLYP1W'},
175: {'comment': 'Functionals fitted for water', 'name': 'XC_GGA_XC_PBELYP1W'},
176: {'comment': 'Schmider-Becke 98 parameterization 1a', 'name': 'XC_GGA_XC_SB98_1a'},
177: {'comment': 'Schmider-Becke 98 parameterization 1b', 'name': 'XC_GGA_XC_SB98_1b'},
178: {'comment': 'Schmider-Becke 98 parameterization 1c', 'name': 'XC_GGA_XC_SB98_1c'},
179: {'comment': 'Schmider-Becke 98 parameterization 2a', 'name': 'XC_GGA_XC_SB98_2a'},
180: {'comment': 'Schmider-Becke 98 parameterization 2b', 'name': 'XC_GGA_XC_SB98_2b'},
181: {'comment': 'Schmider-Becke 98 parameterization 2c', 'name': 'XC_GGA_XC_SB98_2c'},
182: {'comment': 'van Leeuwen & Baerends modified', 'name': 'XC_GGA_X_LBM'},
183: {'comment': 'Exchange form based on Ou-Yang and Levy v.2', 'name': 'XC_GGA_X_OL2'},
184: {'comment': 'mu fixed from the semiclassical neutral atom', 'name': 'XC_GGA_X_APBE'},
185: {'comment': 'mu fixed from the semiclassical neutral atom', 'name': 'XC_GGA_K_APBE'},
186: {'comment': 'mu fixed from the semiclassical neutral atom', 'name': 'XC_GGA_C_APBE'},
187: {'comment': 'Tran and Wesolowski set 1 (Table II)', 'name': 'XC_GGA_K_TW1'},
188: {'comment': 'Tran and Wesolowski set 2 (Table II)', 'name': 'XC_GGA_K_TW2'},
189: {'comment': 'Tran and Wesolowski set 3 (Table II)', 'name': 'XC_GGA_K_TW3'},
190: {'comment': 'Tran and Wesolowski set 4 (Table II)', 'name': 'XC_GGA_K_TW4'},
191: {'comment': 'Haas, Tran, Blaha, and Schwarz', 'name': 'XC_GGA_X_HTBS'},
192: {'comment': 'Constantin et al based on the Airy gas', 'name': 'XC_GGA_X_AIRY'},
193: {'comment': 'Local Airy Gas', 'name': 'XC_GGA_X_LAG'},
194: {'comment': 'Functional for organometallic chemistry', 'name': 'XC_GGA_XC_MOHLYP'},
195: {'comment': 'Functional for barrier heights', 'name': 'XC_GGA_XC_MOHLYP2'},
196: {'comment': 'Tozer and Handy v. FL', 'name': 'XC_GGA_XC_TH_FL'},
197: {'comment': 'Tozer and Handy v. FC', 'name': 'XC_GGA_XC_TH_FC'},
198: {'comment': 'Tozer and Handy v. FCFO', 'name': 'XC_GGA_XC_TH_FCFO'},
199: {'comment': 'Tozer and Handy v. FCO', 'name': 'XC_GGA_XC_TH_FCO'},
200: {'comment': 'Optimized correlation functional of Cohen and Handy', 'name': 'XC_GGA_C_OPTC'},
201: {'comment': 'Local tau approximation of Ernzerhof & Scuseria', 'name': 'XC_MGGA_X_LTA'},
202: {'comment': 'Perdew, Tao, Staroverov & Scuseria exchange', 'name': 'XC_MGGA_X_TPSS'},
203: {'comment': 'M06-Local functional of Minnesota', 'name': 'XC_MGGA_X_M06_L'},
204: {'comment': 'GVT4 from Van Voorhis and Scuseria', 'name': 'XC_MGGA_X_GVT4'},
205: {'comment': 'tau-HCTH from Boese and Handy', 'name': 'XC_MGGA_X_TAU_HCTH'},
206: {'comment': 'Becke-Roussel 89', 'name': 'XC_MGGA_X_BR89'},
207: {'comment': 'Becke & Johnson correction to Becke-Roussel 89', 'name': 'XC_MGGA_X_BJ06'},
208: {'comment': 'Tran & Blaha correction to Becke & Johnson', 'name': 'XC_MGGA_X_TB09'},
209: {'comment': 'Rasanen, Pittalis, and Proetto correction to Becke & Johnson', 'name': 'XC_MGGA_X_RPP09'},
210: {'comment': 'Pittalis, Rasanen, Helbig, Gross Exchange Functional', 'name': 'XC_MGGA_X_2D_PRHG07'},
211: {'comment': 'PRGH07 with PRP10 correction', 'name': 'XC_MGGA_X_2D_PRHG07_PRP10'},
212: {'comment': 'revised Perdew, Tao, Staroverov & Scuseria exchange', 'name': 'XC_MGGA_X_REVTPSS'},
213: {'comment': 'Perdew, Kurth, Zupan, and Blaha', 'name': 'XC_MGGA_X_PKZB'},
214: {'comment': 'M05 functional of Minnesota', 'name': 'XC_MGGA_X_M05'},
215: {'comment': 'M05-2X functional of Minnesota', 'name': 'XC_MGGA_X_M05_2X'},
216: {'comment': 'M06-HF functional of Minnesota', 'name': 'XC_MGGA_X_M06_HF'},
217: {'comment': 'M06 functional of Minnesota', 'name': 'XC_MGGA_X_M06'},
218: {'comment': 'M06-2X functional of Minnesota', 'name': 'XC_MGGA_X_M06_2X'},
219: {'comment': 'M08-HX functional of Minnesota', 'name': 'XC_MGGA_X_M08_HX'},
220: {'comment': 'M08-SO functional of Minnesota', 'name': 'XC_MGGA_X_M08_SO'},
221: {'comment': 'MS exchange of Sun, Xiao, and Ruzsinszky', 'name': 'XC_MGGA_X_MS0'},
222: {'comment': 'MS1 exchange of Sun, et al', 'name': 'XC_MGGA_X_MS1'},
223: {'comment': 'MS2 exchange of Sun, et al', 'name': 'XC_MGGA_X_MS2'},
224: {'comment': 'MS2 hybrid exchange of Sun, et al', 'name': 'XC_MGGA_X_MS2H'},
225: {'comment': 'M11 functional of Minnesota', 'name': 'XC_HYB_MGGA_X_M11'},
226: {'comment': 'M11-L functional of Minnesota', 'name': 'XC_MGGA_X_M11_L'},
227: {'comment': 'MN12-L functional from Minnesota', 'name': 'XC_MGGA_X_MN12_L'},
228: {'comment': 'MN12-SX functional from Minnesota', 'name': 'XC_MGGA_X_MN12_SX'},
229: {'comment': 'Cancio and Chou 2006', 'name': 'XC_MGGA_C_CC06'},
230: {'comment': 'Exchange for accurate virtual orbital energies', 'name': 'XC_MGGA_X_MK00'},
231: {'comment': 'Perdew, Tao, Staroverov & Scuseria correlation', 'name': 'XC_MGGA_C_TPSS'},
232: {'comment': 'VSxc from Van Voorhis and Scuseria (correlation part)', 'name': 'XC_MGGA_C_VSXC'},
233: {'comment': 'M06-Local functional of Minnesota', 'name': 'XC_MGGA_C_M06_L'},
234: {'comment': 'M06-HF functional of Minnesota', 'name': 'XC_MGGA_C_M06_HF'},
235: {'comment': 'M06 functional of Minnesota', 'name': 'XC_MGGA_C_M06'},
236: {'comment': 'M06-2X functional of Minnesota', 'name': 'XC_MGGA_C_M06_2X'},
237: {'comment': 'M05 functional of Minnesota', 'name': 'XC_MGGA_C_M05'},
238: {'comment': 'M05-2X functional of Minnesota', 'name': 'XC_MGGA_C_M05_2X'},
239: {'comment': 'Perdew, Kurth, Zupan, and Blaha', 'name': 'XC_MGGA_C_PKZB'},
240: {'comment': 'Becke correlation 95', 'name': 'XC_MGGA_C_BC95'},
241: {'comment': 'revised TPSS correlation', 'name': 'XC_MGGA_C_REVTPSS'},
242: {'comment': 'Functionals fitted for water', 'name': 'XC_MGGA_XC_TPSSLYP1W'},
243: {'comment': 'Exchange for accurate virtual orbital energies (v. B)', 'name': 'XC_MGGA_X_MK00B'},
244: {'comment': 'functional with balanced localization', 'name': 'XC_MGGA_X_BLOC'},
245: {'comment': 'Modified Perdew, Tao, Staroverov & Scuseria exchange', 'name': 'XC_MGGA_X_MODTPSS'},
401: {'comment': 'The original (ACM) hybrid of Becke', 'name': 'XC_HYB_GGA_XC_B3PW91'},
402: {'comment': 'The (in)famous B3LYP', 'name': 'XC_HYB_GGA_XC_B3LYP'},
403: {'comment': 'Perdew 86 hybrid similar to B3PW91', 'name': 'XC_HYB_GGA_XC_B3P86'},
404: {'comment': 'hybrid using the optx functional', 'name': 'XC_HYB_GGA_XC_O3LYP'},
405: {'comment': 'mixture of mPW91 and PW91 optimized for kinetics', 'name': 'XC_HYB_GGA_XC_mPW1K'},
406: {'comment': 'aka PBE0 or PBE1PBE', 'name': 'XC_HYB_GGA_XC_PBEH'},
407: {'comment': 'Becke 97', 'name': 'XC_HYB_GGA_XC_B97'},
408: {'comment': 'Becke 97-1', 'name': 'XC_HYB_GGA_XC_B97_1'},
410: {'comment': 'Becke 97-2', 'name': 'XC_HYB_GGA_XC_B97_2'},
411: {'comment': 'maybe the best hybrid', 'name': 'XC_HYB_GGA_XC_X3LYP'},
412: {'comment': 'Becke 1-parameter mixture of WC and PBE', 'name': 'XC_HYB_GGA_XC_B1WC'},
413: {'comment': 'Boese-Martin for Kinetics', 'name': 'XC_HYB_GGA_XC_B97_K'},
414: {'comment': 'Becke 97-3', 'name': 'XC_HYB_GGA_XC_B97_3'},
415: {'comment': 'mixture with the mPW functional', 'name': 'XC_HYB_GGA_XC_MPW3PW'},
416: {'comment': 'Becke 1-parameter mixture of B88 and LYP', 'name': 'XC_HYB_GGA_XC_B1LYP'},
417: {'comment': 'Becke 1-parameter mixture of B88 and PW91', 'name': 'XC_HYB_GGA_XC_B1PW91'},
418: {'comment': 'Becke 1-parameter mixture of mPW91 and PW91', 'name': 'XC_HYB_GGA_XC_mPW1PW'},
419: {'comment': 'mixture of mPW and LYP', 'name': 'XC_HYB_GGA_XC_MPW3LYP'},
420: {'comment': 'Schmider-Becke 98 parameterization 1a', 'name': 'XC_HYB_GGA_XC_SB98_1a'},
421: {'comment': 'Schmider-Becke 98 parameterization 1b', 'name': 'XC_HYB_GGA_XC_SB98_1b'},
422: {'comment': 'Schmider-Becke 98 parameterization 1c', 'name': 'XC_HYB_GGA_XC_SB98_1c'},
423: {'comment': 'Schmider-Becke 98 parameterization 2a', 'name': 'XC_HYB_GGA_XC_SB98_2a'},
424: {'comment': 'Schmider-Becke 98 parameterization 2b', 'name': 'XC_HYB_GGA_XC_SB98_2b'},
425: {'comment': 'Schmider-Becke 98 parameterization 2c', 'name': 'XC_HYB_GGA_XC_SB98_2c'},
426: {'comment': 'Hybrid based on SOGGA11 form', 'name': 'XC_HYB_GGA_X_SOGGA11_X'},
427: {'comment': 'the 2003 version of the screened hybrid HSE', 'name': 'XC_HYB_GGA_XC_HSE03'},
428: {'comment': 'the 2006 version of the screened hybrid HSE', 'name': 'XC_HYB_GGA_XC_HSE06'},
429: {'comment': 'HJS hybrid screened exchange PBE version', 'name': 'XC_HYB_GGA_XC_HJS_PBE'},
430: {'comment': 'HJS hybrid screened exchange PBE_SOL version', 'name': 'XC_HYB_GGA_XC_HJS_PBE_SOL'},
431: {'comment': 'HJS hybrid screened exchange B88 version', 'name': 'XC_HYB_GGA_XC_HJS_B88'},
432: {'comment': 'HJS hybrid screened exchange B97x version', 'name': 'XC_HYB_GGA_XC_HJS_B97X'},
433: {'comment': 'CAM version of B3LYP', 'name': 'XC_HYB_GGA_XC_CAM_B3LYP'},
434: {'comment': 'CAM version of B3LYP tunes for excitations', 'name': 'XC_HYB_GGA_XC_TUNED_CAM_B3LYP'},
435: {'comment': 'Becke half-and-half', 'name': 'XC_HYB_GGA_XC_BHANDH'},
436: {'comment': 'Becke half-and-half with B88 exchange', 'name': 'XC_HYB_GGA_XC_BHANDHLYP'},
437: {'comment': 'B3LYP with RC04 LDA', 'name': 'XC_HYB_GGA_XC_MB3LYP_RC04'},
438: {'comment': 'M05 functional of Minnesota', 'name': 'XC_HYB_MGGA_XC_M05'},
439: {'comment': 'M05-2X functional of Minnesota', 'name': 'XC_HYB_MGGA_XC_M05_2X'},
440: {'comment': 'Mixture of B88 with BC95 (B1B95)', 'name': 'XC_HYB_MGGA_XC_B88B95'},
441: {'comment': 'Mixture of B86 with BC95', 'name': 'XC_HYB_MGGA_XC_B86B95'},
442: {'comment': 'Mixture of PW86 with BC95', 'name': 'XC_HYB_MGGA_XC_PW86B95'},
443: {'comment': 'Mixture of B88 with BC95 from Zhao and Truhlar', 'name': 'XC_HYB_MGGA_XC_BB1K'},
444: {'comment': 'M06-HF functional of Minnesota', 'name': 'XC_HYB_MGGA_XC_M06_HF'},
445: {'comment': 'Mixture of mPW91 with BC95 from Zhao and Truhlar', 'name': 'XC_HYB_MGGA_XC_MPW1B95'},
446: {'comment': 'Mixture of mPW91 with BC95 for kinetics', 'name': 'XC_HYB_MGGA_XC_MPWB1K'},
447: {'comment': 'Mixture of X with BC95', 'name': 'XC_HYB_MGGA_XC_X1B95'},
448: {'comment': 'Mixture of X with BC95 for kinetics', 'name': 'XC_HYB_MGGA_XC_XB1K'},
449: {'comment': 'M06 functional of Minnesota', 'name': 'XC_HYB_MGGA_XC_M06'},
450: {'comment': 'M06-2X functional of Minnesota', 'name': 'XC_HYB_MGGA_XC_M06_2X'},
451: {'comment': 'Mixture of PW91 with BC95 from Zhao and Truhlar', 'name': 'XC_HYB_MGGA_XC_PW6B95'},
452: {'comment': 'Mixture of PW91 with BC95 from Zhao and Truhlar for kinetics', 'name': 'XC_HYB_MGGA_XC_PWB6K'},
453: {'comment': 'MPW with 1 par. for metals/LYP', 'name': 'XC_HYB_GGA_XC_MPWLYP1M'},
454: {'comment': 'Revised B3LYP', 'name': 'XC_HYB_GGA_XC_REVB3LYP'},
455: {'comment': 'BLYP with yukawa screening', 'name': 'XC_HYB_GGA_XC_CAMY_BLYP'},
456: {'comment': 'PBE0-1/3', 'name': 'XC_HYB_GGA_XC_PBE0_13'},
457: {'comment': 'TPSS hybrid', 'name': 'XC_HYB_MGGA_XC_TPSSH'},
458: {'comment': 'revTPSS hybrid', 'name': 'XC_HYB_MGGA_XC_REVTPSSH'},
500: {'comment': 'von Weiszaecker functional', 'name': 'XC_GGA_K_VW'},
501: {'comment': 'Second-order gradient expansion (l = 1/9)', 'name': 'XC_GGA_K_GE2'},
502: {'comment': 'TF-lambda-vW form by Golden (l = 13/45)', 'name': 'XC_GGA_K_GOLDEN'},
503: {'comment': 'TF-lambda-vW form by Yonei and Tomishima (l = 1/5)', 'name': 'XC_GGA_K_YT65'},
504: {'comment': 'TF-lambda-vW form by Baltin (l = 5/9)', 'name': 'XC_GGA_K_BALTIN'},
505: {'comment': 'TF-lambda-vW form by Lieb (l = 0.185909191)', 'name': 'XC_GGA_K_LIEB'},
506: {'comment': 'gamma-TFvW form by Acharya et al [g = 1 - 1.412/N^(1/3)]', 'name': 'XC_GGA_K_ABSP1'},
507: {'comment': 'gamma-TFvW form by Acharya et al [g = 1 - 1.332/N^(1/3)]', 'name': 'XC_GGA_K_ABSP2'},
508: {'comment': 'gamma-TFvW form by G\xc3\xa1zquez and Robles', 'name': 'XC_GGA_K_GR'},
509: {'comment': 'gamma-TFvW form by Lude\xc3\xb1a', 'name': 'XC_GGA_K_LUDENA'},
510: {'comment': 'gamma-TFvW form by Ghosh and Parr', 'name': 'XC_GGA_K_GP85'},
511: {'comment': 'Pearson', 'name': 'XC_GGA_K_PEARSON'},
512: {'comment': 'Ou-Yang and Levy v.1', 'name': 'XC_GGA_K_OL1'},
513: {'comment': 'Ou-Yang and Levy v.2', 'name': 'XC_GGA_K_OL2'},
514: {'comment': 'Fuentealba & Reyes (B88 version)', 'name': 'XC_GGA_K_FR_B88'},
515: {'comment': 'Fuentealba & Reyes (PW86 version)', 'name': 'XC_GGA_K_FR_PW86'},
516: {'comment': 'DePristo and Kress', 'name': 'XC_GGA_K_DK'},
517: {'comment': 'Perdew', 'name': 'XC_GGA_K_PERDEW'},
518: {'comment': 'Vitos, Skriver, and Kollar', 'name': 'XC_GGA_K_VSK'},
519: {'comment': 'Vitos, Johansson, Kollar, and Skriver', 'name': 'XC_GGA_K_VJKS'},
520: {'comment': 'Ernzerhof', 'name': 'XC_GGA_K_ERNZERHOF'},
521: {'comment': 'Lembarki & Chermette', 'name': 'XC_GGA_K_LC94'},
522: {'comment': 'Lee, Lee & Parr', 'name': 'XC_GGA_K_LLP'},
523: {'comment': 'Thakkar 1992', 'name': 'XC_GGA_K_THAKKAR'},
524: {'comment': 'short-range version of the PBE', 'name': 'XC_GGA_X_WPBEH'},
525: {'comment': 'HJS screened exchange PBE version', 'name': 'XC_GGA_X_HJS_PBE'},
526: {'comment': 'HJS screened exchange PBE_SOL version', 'name': 'XC_GGA_X_HJS_PBE_SOL'},
527: {'comment': 'HJS screened exchange B88 version', 'name': 'XC_GGA_X_HJS_B88'},
528: {'comment': 'HJS screened exchange B97x version', 'name': 'XC_GGA_X_HJS_B97X'},
529: {'comment': 'short-range recipe for exchange GGA functionals', 'name': 'XC_GGA_X_ITYH'},
530: {'comment': 'short-range recipe for exchange GGA functionals', 'name': 'XC_GGA_X_SFAT'},
}

for k, v in libxc_functionals.iteritems():
    if v['name'].startswith('XC_LDA'):
        libxc_functionals[k].update({'type': ['LDA']})
    elif v['name'].startswith('XC_GGA'):
        libxc_functionals[k].update({'type': ['GGA']})
    elif v['name'].startswith('XC_MGGA'):
        libxc_functionals[k].update({'type': ['meta-GGA']})
    elif v['name'].startswith('XC_HYB_GGA'):
        libxc_functionals[k].update({'type': ['GGA', 'hybrid']})
    elif v['name'].startswith('XC_HYB_MGGA'):
        libxc_functionals[k].update({'type': ['meta-GGA', 'hybrid']})
    else:
        raise RuntimeError("Classification of libxc_functionals failed! Unknown type in name: %s" % v['name'])
