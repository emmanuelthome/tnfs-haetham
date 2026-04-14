This is a follow-up to example_6_p_37_auto.md
---


Date :  11_04_2026
d =  1
# inside __SM1x_setup (should be called only once)
# inside __SM2x_setup (should be called only once)
 p :  37
ell :  43
Polynomial h :  x^3 - x^2 - 2*x + 1
Polynomial f1 :  x^4 + 3*x^2 + 1
Polynomial f2 :  6*x^2 - x + 6
Parameters:
example6b
{'p': 37, 'ell': 43, 'E': 3, 'S': 3600, 'q0': 200, 'q1': 1800, 'external_source': ['example6b_37_3_3600.qrels', 'example6b_37_3_3600.cube_rels'], 'multithreaded': 1}
Computing unit groups
Minimum polynomial (in number fields) of units
[x^4 + 3*x^2 + 1, x^6 + 5*x^4 + 6*x^2 + 1, x^3 + x^2 - 2*x - 1, x^12 + 17*x^10 + 92*x^8 + 179*x^6 + 137*x^4 + 34*x^2 + 1, x^12 + 17*x^10 + 92*x^8 + 179*x^6 + 137*x^4 + 34*x^2 + 1]
[x^3 - x^2 - 2*x + 1, x^3 - x^2 - 2*x + 1]
Minimum polynomial (in GF(p^n)) of images of units
[x^2 + 6*x + 1, x^3 + 31*x^2 + 2*x + 31, x^3 + x^2 + 35*x + 36, x^6 + 6*x^5 + 8*x^4 + 30*x^3 + 9*x^2 + 24*x + 1, x^6 + 31*x^5 + 8*x^4 + 7*x^3 + 9*x^2 + 13*x + 1]
[x^3 + 36*x^2 + 35*x + 1, x^3 + 36*x^2 + 35*x + 1]
Looking for smooth a,b pairs
Size of [-3,3]^6: 15.84 bits
Search space size (per q): 20.0 bits
Search space size (all qs): A=15.8 bits
Expected number of lattice points per q: 5086.0 down to 565.0
Norm bits in [-3,3]^6: (34.54, 23.33)
Special-q on f1 side
############################################################
############################################################
##
## importing relations from example6b_37_3_3600.qrels
##
############################################################
############################################################
1 1 -iota*T + 1
2 2 (3*iota^2 - 6*iota - 1)*T - 3*iota
3 3 (iota^2 - 2*iota - 1)*T - iota - 4
4 4 (iota^2 - 3*iota - 1)*T - iota - 3
5 5 (iota^2 - 4*iota - 1)*T - iota - 2
6 6 -T - 6
7 7 (-2*iota^2 + iota - 1)*T + 2*iota - 7
8 8 -2*T - iota^2 + iota - 4
9 9 (3*iota^2 - 2*iota - 3)*T - 2*iota^2 - iota
10 10 (2*iota^2 - iota - 3)*T - 2*iota^2 - 1
11 11 (iota^2 - iota - 3)*T - 2*iota^2 + iota - 1
12 12 (-iota^2 - 3*iota - 3)*T - 2*iota^2 + 3*iota + 1
13 13 (-2*iota^2 - 3)*T - 2*iota^2 + 4*iota - 2
14 14 (-4*iota^2 - 3)*T - 2*iota^2 + 6*iota - 2
15 15 (iota^2 - iota - 4)*T - 3*iota^2 + 2*iota + 1
16 16 (-3*iota^2 + 3*iota + 3)*T + 2*iota^2 - 5*iota - 2
17 17 (-iota^2 - iota + 1)*T + iota^2 - 6*iota - 2
18 18 (-2*iota^2 + 2*iota - 4)*T - 3*iota^2 - iota - 3
19 19 (-iota^2 + iota - 5)*T - 4*iota^2 - iota
20 20 -2*T + 4*iota^2 - 3*iota + 3
21 21 (-2*iota^2 - 5*iota - 6)*T + 2*iota^2 + iota
22 22 (-6*iota^2 + 3*iota - 3)*T + 3*iota^2 - 2*iota + 1
23 23 (-iota^2 + iota - 6)*T + iota^2 - 5*iota + 1
24 24 -T - iota
25 25 (4*iota^2 + iota - 2)*T + 5*iota^2 - 5
26 26 (2*iota^2 + iota)*T + 3*iota^2 - 2*iota - 3
27 27 (2*iota^2 - 2)*T + 2*iota^2 - 4*iota - 3
28 28 (iota^2 - iota + 4)*T - 2
29 29 (iota^2 - iota + 1)*T - 3*iota - 2
30 30 (iota^2 - iota)*T - 4*iota - 2
31 31 6*T - 1
32 32 (-4*iota + 2)*T - 4*iota^2 - 4*iota - 1
33 33 (-2*iota^2 + 3*iota + 7)*T + iota^2 - 3*iota + 1
34 34 (2*iota^2 + iota + 6)*T + 3*iota^2 - 2*iota - 4
35 35 (-2*iota - 6)*T + 4*iota^2 + iota + 1
36 36 (-2*iota^2 + 2)*T + 4*iota^2 + 5*iota + 3
37 37 (-iota^2 - 5*iota + 5)*T + 4*iota + 1
38 38 (-2*iota^2 + 4)*T + 4*iota^2 + iota + 2
39 39 (iota^2 - 5*iota - 1)*T + 2*iota^2 - 4*iota - 2
40 40 (-iota^2 - 5*iota)*T + 6*iota^2 + 1
41 41 (-3*iota^2 + 2*iota - 1)*T - 6*iota^2 + 3*iota - 3
42 42 (-3*iota^2 - 2*iota - 2)*T - 4*iota^2 - 3*iota - 4
43 43 (-3*iota^2 - 4*iota - 2)*T + 4*iota - 3
44 44 iota*T - 2*iota - 2
45 45 -T + 2*iota^2 - 4*iota - 3
46 46 (iota^2 - 2*iota)*T + 4*iota^2 - 3*iota - 1
47 47 (-iota^2 + 3*iota + 2)*T - 2*iota^2 + 4*iota
48 48 (-2*iota^2 + 3*iota - 1)*T - iota - 4
49 49 (-3*iota^2 + iota - 4)*T + 2*iota^2 - 2*iota - 4
50 50 (iota^2 - iota + 2)*T + 6*iota^2 - 2*iota - 2
51 51 (-4*iota^2 + 5*iota - 1)*T - 2*iota^2 + 4*iota - 3
52 52 (-iota^2 + iota + 2)*T + 4*iota^2 + 3*iota - 1
53 53 (-3*iota^2 + iota - 2)*T + 4*iota^2 + iota - 3
54 54 (2*iota^2 - iota + 3)*T - 6*iota^2 + 4*iota + 2
55 55 (iota^2 - 4*iota - 1)*T - 2*iota^2 + iota + 1
56 56 (-2*iota^2 - iota - 4)*T - 2*iota^2 - iota - 4
57 57 (2*iota^2 + iota + 4)*T - 2*iota^2 - iota - 4
58 58 (2*iota^2 - 2*iota + 3)*T + iota - 1
59 59 (4*iota^2 + 3*iota + 4)*T + 3*iota^2 + 2*iota + 2
60 60 (-2*iota - 2)*T - iota
61 61 (-2*iota^2 + 4*iota)*T + iota^2 - 3*iota - 2
62 62 (iota - 2)*T + 2*iota^2 - 2*iota + 1
63 63 (6*iota^2 - 2*iota - 2)*T - iota^2 + iota - 2
64 64 (4*iota^2 + 3*iota - 1)*T + iota^2 - iota - 2
65 65 (4*iota^2 + iota - 3)*T + 3*iota^2 - iota + 2
66 66 (-2*iota^2 - 2*iota + 5)*T - 3*iota^2 - 2
67 67 (2*iota^2 - 4*iota + 2)*T + iota + 3
68 68 (-2*iota^2 + iota + 2)*T - 4*iota - 2
69 69 (-iota + 1)*T + 2*iota^2 - 2*iota + 3
70 70 2*iota^2*T - 4*iota - 3
71 71 (2*iota^2 - 3*iota - 3)*T + iota^2 - 5*iota - 1
72 72 (-2*iota^2 - 6*iota + 3)*T - 3*iota + 3
73 73 (-5*iota^2 + iota - 1)*T + 5*iota^2 - 3*iota + 1
74 74 (iota^2 - 4*iota - 3)*T + 4*iota^2 + 2
75 75 (5*iota^2 + iota + 1)*T + 4*iota^2 + 3*iota + 1
76 76 (2*iota^2 + 2*iota + 2)*T + 3*iota^2 + 5*iota - 5
77 77 (-iota^2 + iota + 1)*T + iota^2
78 78 3*iota*T - 3*iota + 4
79 79 (iota^2 + iota)*T - iota + 3
80 80 (3*iota^2 - iota - 3)*T + 2
81 81 (2*iota^2 - iota - 2)*T + 4*iota^2 + 3*iota
82 82 2*T + 5*iota^2 + 4*iota
83 83 (iota^2 - iota)*T + 6*iota^2 + 5*iota - 1
84 84 (5*iota^2 - 3*iota - 2)*T + iota^2 + 3*iota + 3
85 85 (-2*iota^2 + 6*iota + 2)*T + 3*iota^2 - 3*iota - 3
86 86 (2*iota^2 + 1)*T - iota^2 - 4
87 87 (4*iota^2 - iota + 3)*T - 5*iota^2 - iota
88 88 (3*iota^2 + 3*iota)*T + 4*iota^2
89 89 (-iota^2 - 4*iota - 1)*T + 5*iota^2 + iota - 3
90 90 (-iota^2 - iota + 4)*T + 4*iota^2 - iota + 4
91 91 (4*iota^2 + 2)*T + iota^2 - 4*iota - 3
92 92 (3*iota^2 + 3)*T + 5*iota^2 - iota - 5
93 93 (4*iota^2 + 3*iota + 1)*T + 3*iota^2 - 6*iota
94 94 -iota^2*T - iota^2 + iota + 1
95 95 (-iota^2 - iota - 2)*T + iota^2 + 1
96 96 (2*iota^2 + 2*iota - 4)*T + iota^2 + iota + 1
97 97 (-iota^2 + 2*iota - 4)*T - 2*iota^2 + 4*iota + 4
98 98 (-4*iota^2 + 2*iota - 2)*T + iota^2 + 3*iota - 5
99 99 (3*iota - 3)*T + 3*iota^2 + iota - 6
100 100 (-3*iota^2 + 3*iota + 3)*T - 2*iota^2 + 6*iota + 2
101 101 (5*iota^2 + 4*iota + 2)*T + 4*iota^2 - 3
102 102 (2*iota^2 + 5*iota + 1)*T - iota^2 + 5*iota + 3
103 103 (-iota^2 - 4*iota + 4)*T + 5*iota^2 - 3*iota
104 104 -4*iota^2*T + 3*iota^2 + 3*iota
105 105 (2*iota + 5)*T + 4*iota^2 + 3*iota + 1
106 106 (-iota + 1)*T - iota - 1
107 107 (4*iota^2 - iota + 1)*T + 7*iota^2 + iota - 2
108 108 (4*iota^2 - 1)*T + 5*iota^2 + 2*iota + 2
109 109 (2*iota + 1)*T + iota^2 - 4*iota
110 110 2*iota^2*T + iota^2 - 2*iota + 3
111 111 (2*iota^2 - 2*iota + 2)*T + iota^2 - 4*iota + 1
112 112 (iota^2 + iota)*T - 3*iota + 3
113 113 (iota^2 + 5*iota)*T + 3*iota^2 - 5*iota + 2
114 114 (-2*iota^2 + 2*iota - 4)*T + 2*iota^2 + 2*iota - 3
115 115 (-iota^2 - 3*iota)*T - 2*iota^2 - 7*iota
116 116 (iota^2 - 6*iota - 5)*T - 2*iota + 2
117 117 (-iota + 7)*T + 4*iota^2 - 1
118 118 (-2*iota + 7)*T + 2*iota^2 - iota + 1
119 119 (-6*iota^2 + 2*iota + 2)*T - iota^2 + iota - 2
120 120 -3*iota^2*T + 5*iota + 2
121 121 (-iota^2 + 3*iota + 2)*T + 6*iota^2
122 122 (-3*iota^2 + 3*iota - 3)*T + 2*iota^2 + 4
123 123 -iota*T + 4*iota^2 - 4*iota + 4
124 124 (-4*iota^2 - 2*iota - 4)*T - iota^2 - 3*iota + 4
125 125 (-4*iota^2 + 1)*T + 5*iota^2 + 3
126 126 (-iota - 1)*T + iota - 1
127 127 (-2*iota^2 + 4*iota + 2)*T - iota^2 + 4*iota + 1
128 128 (-6*iota^2 + 2)*T + 3*iota^2 + 1
129 129 (-iota^2 + 3*iota - 1)*T + 3*iota
130 130 (-2*iota^2 + 2*iota - 1)*T + iota^2 + 2*iota
131 131 (iota^2 + 5*iota - 2)*T + iota + 1
132 132 (iota^2 + 3*iota - 4)*T + 3*iota - 1
133 133 (3*iota - 3)*T + iota^2 + iota
134 134 (2*iota - 4)*T + iota^2 + 2*iota - 1
135 135 (-iota^2 + 2*iota - 3)*T + 2*iota^2
136 136 (iota^2 + 5*iota - 3)*T + 2*iota^2 - 3*iota + 2
137 137 (-2*iota^2 - 2*iota + 3)*T - 2*iota^2 + 2*iota - 4
138 138 (3*iota^2 + 5*iota - 4)*T - 3*iota - 2
139 139 (-4*iota^2 + 1)*T - iota + 7
140 140 (iota^2 - iota + 2)*T - 6*iota^2 + 2*iota + 2
141 141 (-3*iota^2 - 7*iota)*T - 2*iota^2
142 142 (2*iota^2 - 5*iota - 5)*T - 3*iota^2 - 1
143 143 -6*iota^2*T - iota^2 + 3*iota + 2
144 144 (-iota^2 + 6*iota + 1)*T - 4*iota^2 - iota + 2
145 145 (iota^2 + 3*iota - 5)*T - 4*iota^2 + 2*iota - 2
146 146 (-4*iota^2 + 4*iota - 4)*T - iota
147 147 (-iota - 1)*T + 2*iota
148 148 (-iota^2 - iota - 2)*T + iota - 1
149 149 (3*iota + 1)*T - 2*iota^2 - 5*iota - 1
150 150 (-2*iota^2 + 1)*T + iota^2 + 3*iota + 3
151 151 (-iota^2 + 3*iota + 1)*T - 3*iota^2 + 2
152 152 (-2*iota^2 + 3*iota - 2)*T - 5*iota^2
153 153 (-6*iota^2 + 3*iota - 1)*T - 2*iota^2 + 2
154 154 (-3*iota^2 + 3*iota)*T - 4*iota^2 + 4*iota + 4
155 155 (3*iota^2 + 1)*T + 3*iota^2 - 7*iota + 1
156 156 (-2*iota - 1)*T + 4*iota^2 - iota + 3
157 157 (2*iota^2 - 5)*T - 4*iota^2 + iota + 1
158 158 (-4*iota^2 + 2*iota - 2)*T + iota^2 - 6*iota + 2
159 159 (-3*iota^2 + 3*iota - 2)*T - iota^2 - 6*iota + 2
160 160 (iota^2 + 2*iota + 1)*T - iota^2 + 6
161 161 (-2*iota^2 - 2*iota - 2)*T - iota^2 - 7*iota
162 162 (-3*iota^2 - 5*iota + 5)*T - 2*iota^2 - 2*iota - 2
163 163 (-iota + 1)*T - iota^2 - iota - 2
164 164 -2*iota*T - iota - 1
165 165 (2*iota^2 + iota + 1)*T + iota - 1
166 166 (2*iota^2 - iota + 1)*T - 2
167 167 (-iota^2 + 3*iota - 1)*T - 4*iota^2 + 2*iota + 1
168 168 (3*iota^2 + 4*iota - 2)*T - iota^2 + 5*iota + 3
169 169 (4*iota^2 - 4*iota - 4)*T - 3*iota^2 + 3*iota
170 170 (-3*iota^2 - 3*iota + 3)*T + iota^2 - 3*iota + 2
171 171 (iota^2 - 6*iota + 2)*T + 4*iota^2 - 2*iota + 2
172 172 (2*iota^2 - 4*iota + 4)*T - 2*iota^2 - iota - 2
173 173 (3*iota^2 - 7*iota + 1)*T - 3*iota^2 - 1
174 174 (-iota^2 + 3*iota + 4)*T + 6*iota^2 + 2*iota - 1
175 175 (-6*iota^2 - 1)*T - 5*iota^2 + 2*iota - 1
176 176 (-4*iota^2 + iota - 1)*T + 2*iota^2 + 7*iota + 1
177 177 (-2*iota^2 - iota - 1)*T + 3*iota^2 + 7*iota
178 178 -2*iota^2*T - iota^2 + iota + 1
179 179 (2*iota^2 - 1)*T + 3*iota^2 - 3*iota
180 180 (3*iota^2 - 3)*T + 2*iota^2 - 5*iota + 2
181 181 (-2*iota + 1)*T - 3*iota^2 + 2*iota + 2
182 182 (4*iota^2 - 2*iota - 1)*T + 3*iota^2 - 4*iota + 2
183 183 (5*iota^2 - 4*iota + 1)*T + 4*iota^2 - 3*iota + 2
184 184 (iota^2 - 2*iota - 1)*T - 4*iota^2 + 4
185 185 -7*iota^2*T - 2*iota^2
186 186 (5*iota^2 - 4*iota + 2)*T - 2*iota^2 - 2*iota - 2
187 187 (-iota^2 - 1)*T - iota^2 - 6*iota - 5
188 188 (3*iota - 4)*T + 3*iota^2 + 3*iota
189 189 (4*iota^2 - iota - 2)*T - 5*iota^2 + 4*iota - 1
190 190 (-5*iota - 1)*T - 4*iota^2 + 2*iota + 2
191 191 (3*iota^2 - 5*iota - 3)*T - 4*iota^2 - iota + 3
192 192 (-iota^2 + iota + 1)*T + 2*iota^2
193 193 (iota^2 + iota)*T - iota^2 + 2*iota - 2
194 194 (2*iota^2 - 5*iota + 2)*T - 3*iota^2 + 3
195 195 (-2*iota^2 - iota + 3)*T + iota^2 + 2
196 196 (-4*iota^2 + 4)*T - iota^2 + 2*iota + 1
197 197 (-6*iota^2 + 2*iota)*T - 5*iota^2 + 2*iota - 1
198 198 (2*iota^2 + 5*iota - 2)*T + 4*iota^2 - 4*iota - 1
199 199 (6*iota^2 + 3*iota - 2)*T + iota^2 - 2*iota - 2
200 200 2*iota^2*T - 7*iota^2
201 201 (5*iota + 2)*T - 4*iota^2 - 2*iota
202 202 (5*iota^2 - 4*iota + 1)*T + 4*iota^2 - iota - 2
203 203 (-5*iota^2 + iota - 4)*T - 3*iota - 3
204 204 2*iota*T + iota^2 + 3*iota - 7
205 205 (-2*iota^2 + iota)*T - 2*iota^2 + 3*iota - 6
206 206 (4*iota^2 - 2*iota - 2)*T - 5*iota - 1
207 207 (-3*iota^2 + 2*iota + 1)*T - iota^2 - 7*iota + 1
208 208 (-3*iota^2 - 3*iota - 2)*T + 3*iota^2 - 4*iota - 4
209 209 (iota + 5)*T - 2*iota^2 - 6*iota - 2
210 210 (iota^2 + 4*iota + 3)*T - 3*iota^2
211 211 (-iota^2 + iota + 5)*T - 2*iota^2
212 212 (-iota^2 - 2*iota + 6)*T - iota^2 - iota
213 213 (2*iota^2 - 2)*T - iota - 5
214 214 -T - 5
215 215 (-2*iota + 2)*T - iota - 3
216 216 (2*iota + 2)*T - iota^2 + 5*iota + 2
217 217 (iota + 6)*T - 2*iota^2 + 4*iota + 1
218 218 (2*iota^2 + 2*iota + 6)*T - 3*iota^2 + 3*iota - 2
219 219 (iota^2 + 4*iota - 3)*T + 4*iota^2 - 3*iota + 3
220 220 (iota^2 + 7*iota)*T + 2*iota^2 + 2*iota + 2
221 221 (5*iota^2 + 3*iota + 2)*T + 2*iota^2 - 2*iota - 4
222 222 (3*iota^2 + 3*iota + 3)*T + 3*iota^2 + 4*iota + 4
223 223 (-iota + 1)*T - iota^2 + iota - 1
224 224 (-2*iota - 1)*T + 4*iota - 5
225 225 -5*T + 1
226 226 (-4*iota - 2)*T - 5*iota^2 + 3*iota - 1
227 227 (-iota^2 + iota - 3)*T + 2*iota^2 - iota - 2
228 228 (-iota^2 - 3)*T - iota - 1
229 229 (-iota^2 - iota - 2)*T - iota^2 - 2
230 230 -2*iota^2*T + iota^2 - iota - 5
231 231 (-3*iota^2 - 3)*T + iota^2 - 2*iota - 6
232 232 (6*iota + 1)*T + 3*iota^2 - 3
233 233 (-4*iota^2 - 2*iota - 6)*T - 2*iota^2 + 2*iota + 3
234 234 (-iota^2 - 2*iota + 1)*T + iota^2 + 1
235 235 (iota^2 + iota - 3)*T + iota^2
236 236 (3*iota^2 - 2*iota + 2)*T + 2*iota^2 - 2*iota - 5
237 237 (4*iota^2 - 4)*T + 3*iota^2 - 3
238 238 (-iota + 4)*T - 3*iota^2 + 4*iota
239 239 (2*iota^2 - 4)*T + iota^2 + 4*iota + 1
240 240 (-2*iota^2 + 2*iota + 4)*T + 3*iota^2 - iota + 4
241 241 (2*iota^2 - iota + 3)*T + iota^2 + 2*iota + 2
242 242 (4*iota^2 - 2*iota + 1)*T - 3*iota^2 + 6
243 243 (-iota^2 - 1)*T - iota^2 - 2*iota + 1
244 244 (iota^2 + 4*iota + 2)*T + 3*iota
245 245 (4*iota + 1)*T - iota^2 + iota + 1
246 246 (-2*iota^2 + 2*iota - 2)*T - iota^2 + iota - 4
247 247 (3*iota^2 - 3)*T - 4*iota^2 + 4
248 248 (-3*iota^2 - 7*iota - 3)*T - 2
249 249 (iota^2 - 3*iota + 1)*T + iota^2 + 6*iota - 1
250 250 (-3*iota^2 - 2*iota - 2)*T - 4*iota^2 + 3*iota + 4
251 251 (2*iota^2 - iota + 2)*T - iota^2 - 7*iota + 1
252 252 (iota^2 + 4)*T + iota^2 + 2*iota - 5
253 253 (2*iota^2 + iota + 4)*T - 3*iota^2 + 3*iota + 3
254 254 (-3*iota^2 + 6)*T - 4*iota^2 + 2*iota - 1
255 255 (-iota^2 - iota + 1)*T + iota^2 + iota + 1
256 256 (-2*iota^2 + 3)*T - 3*iota^2 + 3*iota
257 257 (-3*iota^2 - 2*iota + 4)*T + 3*iota - 1
258 258 (-iota^2 + iota + 1)*T - 2*iota^2 + 2*iota - 6
259 259 (-iota^2 - 3*iota + 4)*T - 2*iota + 1
260 260 (-3*iota^2 - 4*iota + 5)*T + 2*iota^2 + iota
261 261 (-2*iota^2 - iota + 2)*T + iota^2 + 2*iota - 7
262 262 (-4*iota + 4)*T + iota^2 - 5*iota + 1
263 263 (-2*iota^2 - 3*iota + 3)*T + 3*iota^2 - 6
264 264 (4*iota^2 + 5*iota - 3)*T + iota^2 - 2*iota + 3
265 265 (4*iota^2 + 4*iota + 1)*T - 3*iota^2 - 5*iota - 1
266 266 (-iota^2 + iota + 7)*T - 3*iota^2 + iota + 2
267 267 (2*iota^2 + 4*iota + 4)*T + 3*iota^2 - iota - 1
268 268 (-3*iota^2 + 3*iota - 3)*T + iota^2 + 2*iota + 6
269 269 (-6*iota^2 + iota + 1)*T + iota^2 - 4*iota + 4
270 270 (-iota^2 - iota - 1)*T - iota^2 - iota + 1
271 271 (3*iota^2 + 2*iota - 2)*T - iota + 3
272 272 (3*iota^2 + iota + 1)*T + 2
273 273 (-2*iota^2 + iota + 7)*T - iota^2 - 2*iota + 2
274 274 (-iota^2 - 2*iota - 5)*T + 4*iota^2 - 3
275 275 2*iota^2*T - 1
276 276 (2*iota^2 - 5*iota - 1)*T + iota^2 + 2*iota + 2
277 277 (-5*iota^2 + 4*iota - 2)*T - 2
278 278 (5*iota^2 - iota - 3)*T + iota^2 + 2*iota - 4
279 279 (3*iota^2 - 3*iota + 5)*T - iota^2 - iota - 1
280 280 (-3*iota^2 - 3*iota + 3)*T + 6*iota^2 - 2*iota - 2
281 281 (-6*iota^2 + iota)*T - 3*iota^2 - 4*iota + 1
282 282 (-4*iota - 3)*T + 5*iota^2 - 3*iota - 3
283 283 (-4*iota^2 + 3)*T - 5*iota^2 - 4*iota - 2
284 284 -T - 2*iota^2
285 285 (6*iota^2 - 3*iota - 3)*T - iota^2 - iota - 1
286 286 (iota^2 + 2*iota + 2)*T - 2*iota^2 + 5*iota + 1
287 287 (2*iota^2 + iota - 5)*T - 3*iota^2 - iota + 3
288 288 (iota^2 + 2*iota - 4)*T - 5*iota^2 + iota + 3
289 289 (3*iota - 2)*T - 5*iota^2 + 3*iota + 3
290 290 (-iota^2 + 4*iota + 1)*T - 3*iota^2 + 5*iota + 3
291 291 (-4*iota + 5)*T - 3*iota - 3
292 292 (-6*iota^2 + 2*iota + 2)*T - 3*iota^2 - 3*iota + 3
293 293 (-3*iota^2 + 2*iota - 2)*T - 4*iota - 5
294 294 (6*iota^2 + 1)*T - iota^2 - 5*iota
295 295 -3*T - 5*iota^2 - 3*iota + 2
296 296 (-2*iota - 3)*T - 3*iota^2 + iota + 2
297 297 (-3*iota - 3)*T - 2*iota^2 + 3*iota + 2
298 298 (-5*iota + 1)*T + 3*iota - 6
299 299 -2*iota^2*T + iota^2 - 2*iota - 6
300 300 (-2*iota^2 - 2*iota - 3)*T + 3*iota^2 + 5*iota
301 301 (-4*iota^2 + 2*iota - 2)*T + 5*iota^2 - 4
302 302 (-3*iota + 5)*T + 2*iota^2 - iota + 3
303 303 (-4*iota^2 + 2)*T + 6*iota^2 - 2*iota + 1
304 304 (2*iota^2 - 2*iota - 4)*T + 5*iota^2 + iota
305 305 (5*iota^2 + 3*iota - 2)*T - 3
306 306 (2*iota^2 - 3*iota - 2)*T - 3*iota - 3
307 307 (iota^2 + 1)*T - iota^2 - iota - 2
308 308 (-iota^2 + 2*iota + 6)*T - 2*iota^2
309 309 (4*iota^2 - 3*iota + 4)*T - iota^2 + 4*iota + 2
310 310 (-2*iota^2 - 1)*T - 2*iota
311 311 (iota^2 + 1)*T - iota^2 - 4*iota
312 312 (iota^2 - iota - 2)*T - iota^2 - 3*iota + 1
313 313 (-3*iota + 1)*T - 3*iota
314 314 (3*iota^2 - 4*iota)*T - iota^2 - 4*iota + 1
315 315 (-2*iota^2 + 2*iota - 2)*T + iota^2 + 5*iota + 3
316 316 (iota^2 + 2)*T - 3*iota^2 + 3*iota - 6
317 317 (-iota^2 - iota - 2)*T - 2*iota^2 + 2
318 318 (-iota^2 - 5*iota - 1)*T - iota^2 - iota - 4
319 319 (iota^2 + 5*iota + 3)*T + 2*iota^2 - 2*iota + 2
320 320 (-iota^2 + 3*iota + 5)*T - 4*iota^2 + 4
321 321 -2*iota^2*T - 4*iota^2 - 6*iota - 1
322 322 (-3*iota^2 + 3*iota - 6)*T - iota^2 - 2
323 323 (-4*iota^2 - 3*iota - 1)*T - 2*iota - 5
324 324 -iota*T - 2*iota^2 + iota - 1
325 325 (-2*iota^2 - 2*iota - 2)*T - iota^2 - 3*iota - 1
326 326 (-2*iota^2 - 3*iota - 3)*T - 2*iota^2 - 5*iota - 3
327 327 (2*iota^2 - iota + 5)*T - 2*iota
328 328 (-iota^2 - iota + 4)*T + 4*iota^2 + 2*iota + 3
329 329 (-iota^2 + iota + 5)*T + 6*iota^2 + iota - 3
330 330 (2*iota^2 - 1)*T + 3*iota^2 + 2*iota + 3
331 331 (-iota - 1)*T - 2*iota^2 + 1
332 332 (4*iota^2 + iota - 3)*T + 4
333 333 (iota^2 + iota + 2)*T - 2*iota^2 - iota + 3
334 334 (2*iota + 5)*T - iota^2 + 1
335 335 3*T - 5*iota^2 + 3
336 336 2*T - 4*iota^2 - 4*iota + 5
337 337 (-iota^2 + 4*iota + 2)*T + 4*iota^2 + 4*iota
338 338 (-5*iota^2 + iota + 2)*T - 4*iota^2 - 2*iota - 4
339 339 (iota^2 + 6*iota - 4)*T - 3*iota^2 + iota - 3
340 340 (iota^2 - 1)*T + 2*iota + 5
341 341 (3*iota - 5)*T + 3*iota^2 + iota - 2
342 342 -4*T + 4*iota^2 + iota - 3
343 343 (-iota^2 + 3*iota + 4)*T - iota + 3
344 344 (4*iota^2 + 4*iota)*T + iota^2 - 4*iota - 2
345 345 (5*iota^2 + iota)*T + 2*iota^2 - 2*iota + 2
346 346 (-4*iota^2 - iota - 2)*T + 2*iota^2 + 4
347 347 (-2*iota^2 - 7*iota - 1)*T + 4*iota^2 - iota + 1
348 348 (-iota^2 - iota - 2)*T - iota + 1
349 349 (-2*iota^2 - 3*iota - 5)*T + iota^2 + 4
350 350 (-2*iota^2 - iota)*T + 3*iota^2 - 2*iota - 3
351 351 (-2*iota^2 - 2*iota)*T + 5*iota^2 - 3*iota - 2
352 352 (-2*iota^2 - iota - 1)*T + 2*iota^2 + iota - 2
353 353 (-2*iota^2 - 2*iota - 2)*T + 3*iota^2 + 3*iota
354 354 (-3*iota^2 - 2*iota - 1)*T + 5*iota^2 + 5*iota - 3
355 355 (-4*iota^2 + 2*iota + 2)*T - 5*iota - 1
356 356 (2*iota^2 - iota + 1)*T + iota
357 357 (-iota + 1)*T + iota^2 + iota + 2
358 358 (3*iota^2 - 2*iota - 3)*T + 2*iota^2 + iota
359 359 (5*iota^2 - 3*iota - 2)*T + 2*iota^2 + 2*iota
360 360 (3*iota^2 + 3*iota)*T + 2*iota^2 + 2*iota + 2
361 361 (3*iota^2 - 6)*T + 4*iota^2 + iota + 1
362 362 (-5*iota - 1)*T + 4*iota^2 - 2*iota - 2
363 363 2*T + 4*iota^2 - iota
364 364 (-2*iota^2 + 2)*T + 5*iota^2 - iota + 2
365 365 (4*iota^2 - iota + 4)*T - iota^2 - iota + 4
366 366 (iota^2 - 3*iota + 3)*T - 2*iota^2 - iota + 1
367 367 2*T - 5*iota - 2
368 368 (5*iota^2 - 4)*T - 4*iota^2 + 2*iota - 2
369 369 (-5*iota^2 + 2*iota - 1)*T - 6*iota^2 - 1
370 370 (-5*iota^2 + 3*iota)*T + iota^2 + 4*iota - 4
371 371 -3*iota^2*T + 4*iota - 3
372 372 (-2*iota^2 + 2*iota)*T - 3*iota^2 + iota - 2
373 373 (-iota^2 - 1)*T - 3*iota^2 + 2*iota - 1
374 374 (-3*iota^2 + 6*iota - 2)*T - 4*iota^2 - 1
375 375 (-4*iota^2 - 3*iota - 1)*T + 4*iota^2 - 2*iota + 2
376 376 (3*iota^2 + 4*iota - 1)*T - 2*iota^2 + 3*iota - 1
377 377 (iota^2 + iota)*T - 2*iota^2 + 2*iota - 2
378 378 (-iota^2 - 5*iota - 1)*T - 6*iota^2 + 2*iota + 2
379 379 (iota^2 - iota + 4)*T + 2*iota^2 - 2*iota
380 380 (2*iota^2 - 2*iota)*T + 5*iota^2 - 3*iota + 2
381 381 (4*iota^2 - 3*iota - 1)*T - 3*iota^2 + 4*iota + 1
382 382 (-3*iota^2 - 3)*T - 3*iota^2 + iota - 4
383 383 (2*iota + 3)*T + iota
384 384 (-3*iota + 3)*T - 4*iota^2 + 2*iota - 2
385 385 (7*iota^2 + 3*iota - 1)*T - 2*iota^2 - 2*iota + 2
386 386 (iota^2 - 3*iota - 4)*T - iota^2 - 4*iota + 4
387 387 (-iota^2 - 4*iota - 1)*T - 2*iota^2 - 3*iota + 4
388 388 (3*iota^2 - 2*iota + 1)*T + 2*iota^2 + 5*iota + 1
389 389 (3*iota^2 - 3*iota + 2)*T + 6*iota^2 + 3*iota
390 390 -iota*T + 2*iota + 3
391 391 (-3*iota^2 + iota - 2)*T - 2*iota^2 + 2*iota
392 392 (-2*iota^2 - 4*iota)*T + 2*iota^2 + 3*iota - 1
393 393 (-4*iota^2 + 2*iota - 2)*T + 3*iota - 3
394 394 (-4*iota^2 - 1)*T + 3*iota^2 + 4*iota - 5
395 395 (-iota^2 - 4*iota + 4)*T - iota^2 + 3*iota + 4
396 396 (iota^2 - 4*iota - 2)*T + iota^2 + 6*iota
397 397 (3*iota^2 + 3)*T + iota^2 + 3*iota - 2
398 398 (2*iota^2 + 2*iota + 2)*T + 5*iota
############################################################
############################################################
##
## importing relations from example6b_37_3_3600.cube_rels
##
############################################################
############################################################
399 1 -iota*T + 1
# adjusting relation count offset to {offset}
400 2 (3*iota^2 - 6*iota - 1)*T - 3*iota
401 3 (iota^2 - 2*iota - 1)*T - iota - 4
402 4 (iota^2 - 3*iota - 1)*T - iota - 3
403 5 (iota^2 - 4*iota - 1)*T - iota - 2
404 6 -T - 6
405 7 (-2*iota^2 + iota - 1)*T + 2*iota - 7
406 8 -2*T - iota^2 + iota - 4
407 9 (3*iota^2 - 2*iota - 3)*T - 2*iota^2 - iota
408 10 (2*iota^2 - iota - 3)*T - 2*iota^2 - 1
409 11 (iota^2 - iota - 3)*T - 2*iota^2 + iota - 1
410 12 (-iota^2 - 3*iota - 3)*T - 2*iota^2 + 3*iota + 1
411 13 (-2*iota^2 - 3)*T - 2*iota^2 + 4*iota - 2
412 14 (-4*iota^2 - 3)*T - 2*iota^2 + 6*iota - 2
413 15 (iota^2 - iota - 4)*T - 3*iota^2 + 2*iota + 1
414 16 (-3*iota^2 + 3*iota + 3)*T + 2*iota^2 - 5*iota - 2
415 17 (-iota^2 - iota + 1)*T + iota^2 - 6*iota - 2
416 18 (-2*iota^2 + 2*iota - 4)*T - 3*iota^2 - iota - 3
417 19 (-iota^2 + iota - 5)*T - 4*iota^2 - iota
418 20 -2*T + 4*iota^2 - 3*iota + 3
419 21 (-2*iota^2 - 5*iota - 6)*T + 2*iota^2 + iota
420 22 (-6*iota^2 + 3*iota - 3)*T + 3*iota^2 - 2*iota + 1
421 23 (-iota^2 + iota - 6)*T + iota^2 - 5*iota + 1
422 24 -T - iota
423 25 (4*iota^2 + iota - 2)*T + 5*iota^2 - 5
424 26 (2*iota^2 + iota)*T + 3*iota^2 - 2*iota - 3
425 27 (2*iota^2 - 2)*T + 2*iota^2 - 4*iota - 3
426 28 (iota^2 - iota + 4)*T - 2
427 29 (iota^2 - iota + 1)*T - 3*iota - 2
428 30 (iota^2 - iota)*T - 4*iota - 2
429 31 6*T - 1
430 32 (-4*iota + 2)*T - 4*iota^2 - 4*iota - 1
431 33 (-2*iota^2 + 3*iota + 7)*T + iota^2 - 3*iota + 1
432 34 (2*iota^2 + iota + 6)*T + 3*iota^2 - 2*iota - 4
433 35 (-2*iota - 6)*T + 4*iota^2 + iota + 1
434 36 (-2*iota^2 + 2)*T + 4*iota^2 + 5*iota + 3
435 37 (-iota^2 - 5*iota + 5)*T + 4*iota + 1
436 38 (-2*iota^2 + 4)*T + 4*iota^2 + iota + 2
437 39 (iota^2 - 5*iota - 1)*T + 2*iota^2 - 4*iota - 2
438 40 (-iota^2 - 5*iota)*T + 6*iota^2 + 1
439 41 (-3*iota^2 + 2*iota - 1)*T - 6*iota^2 + 3*iota - 3
440 42 (-3*iota^2 - 2*iota - 2)*T - 4*iota^2 - 3*iota - 4
441 43 (-3*iota^2 - 4*iota - 2)*T + 4*iota - 3
442 44 iota*T - 2*iota - 2
443 45 -T + 2*iota^2 - 4*iota - 3
444 46 (iota^2 - 2*iota)*T + 4*iota^2 - 3*iota - 1
445 47 (-iota^2 + 3*iota + 2)*T - 2*iota^2 + 4*iota
446 48 (-2*iota^2 + 3*iota - 1)*T - iota - 4
447 49 (-3*iota^2 + iota - 4)*T + 2*iota^2 - 2*iota - 4
448 50 (iota^2 - iota + 2)*T + 6*iota^2 - 2*iota - 2
449 51 (-4*iota^2 + 5*iota - 1)*T - 2*iota^2 + 4*iota - 3
450 52 (-iota^2 + iota + 2)*T + 4*iota^2 + 3*iota - 1
451 53 (-3*iota^2 + iota - 2)*T + 4*iota^2 + iota - 3
452 54 (2*iota^2 - iota + 3)*T - 6*iota^2 + 4*iota + 2
453 55 (iota^2 - 4*iota - 1)*T - 2*iota^2 + iota + 1
454 56 (-2*iota^2 - iota - 4)*T - 2*iota^2 - iota - 4
455 57 (2*iota^2 + iota + 4)*T - 2*iota^2 - iota - 4
456 58 (2*iota^2 - 2*iota + 3)*T + iota - 1
457 59 (4*iota^2 + 3*iota + 4)*T + 3*iota^2 + 2*iota + 2
458 60 (-2*iota - 2)*T - iota
459 61 (-2*iota^2 + 4*iota)*T + iota^2 - 3*iota - 2
460 62 (iota - 2)*T + 2*iota^2 - 2*iota + 1
461 63 (6*iota^2 - 2*iota - 2)*T - iota^2 + iota - 2
462 64 (4*iota^2 + 3*iota - 1)*T + iota^2 - iota - 2
463 65 (4*iota^2 + iota - 3)*T + 3*iota^2 - iota + 2
464 66 (-2*iota^2 - 2*iota + 5)*T - 3*iota^2 - 2
465 67 (2*iota^2 - 4*iota + 2)*T + iota + 3
466 68 (-2*iota^2 + iota + 2)*T - 4*iota - 2
467 69 (-iota + 1)*T + 2*iota^2 - 2*iota + 3
468 70 2*iota^2*T - 4*iota - 3
469 71 (2*iota^2 - 3*iota - 3)*T + iota^2 - 5*iota - 1
470 72 (-2*iota^2 - 6*iota + 3)*T - 3*iota + 3
471 73 (-5*iota^2 + iota - 1)*T + 5*iota^2 - 3*iota + 1
472 74 (iota^2 - 4*iota - 3)*T + 4*iota^2 + 2
473 75 (5*iota^2 + iota + 1)*T + 4*iota^2 + 3*iota + 1
474 76 (2*iota^2 + 2*iota + 2)*T + 3*iota^2 + 5*iota - 5
475 77 (-iota^2 + iota + 1)*T + iota^2
476 78 3*iota*T - 3*iota + 4
477 79 (iota^2 + iota)*T - iota + 3
478 80 (3*iota^2 - iota - 3)*T + 2
479 81 (2*iota^2 - iota - 2)*T + 4*iota^2 + 3*iota
480 82 2*T + 5*iota^2 + 4*iota
481 83 (iota^2 - iota)*T + 6*iota^2 + 5*iota - 1
482 84 (5*iota^2 - 3*iota - 2)*T + iota^2 + 3*iota + 3
483 85 (-2*iota^2 + 6*iota + 2)*T + 3*iota^2 - 3*iota - 3
484 86 (2*iota^2 + 1)*T - iota^2 - 4
485 87 (4*iota^2 - iota + 3)*T - 5*iota^2 - iota
486 88 (3*iota^2 + 3*iota)*T + 4*iota^2
487 89 (-iota^2 - 4*iota - 1)*T + 5*iota^2 + iota - 3
488 90 (-iota^2 - iota + 4)*T + 4*iota^2 - iota + 4
489 91 (4*iota^2 + 2)*T + iota^2 - 4*iota - 3
490 92 (3*iota^2 + 3)*T + 5*iota^2 - iota - 5
491 93 (4*iota^2 + 3*iota + 1)*T + 3*iota^2 - 6*iota
492 94 -iota^2*T - iota^2 + iota + 1
493 95 (-iota^2 - iota - 2)*T + iota^2 + 1
494 96 (2*iota^2 + 2*iota - 4)*T + iota^2 + iota + 1
495 97 (-iota^2 + 2*iota - 4)*T - 2*iota^2 + 4*iota + 4
496 98 (-4*iota^2 + 2*iota - 2)*T + iota^2 + 3*iota - 5
497 99 (3*iota - 3)*T + 3*iota^2 + iota - 6
498 100 (-3*iota^2 + 3*iota + 3)*T - 2*iota^2 + 6*iota + 2
499 101 (5*iota^2 + 4*iota + 2)*T + 4*iota^2 - 3
500 102 (2*iota^2 + 5*iota + 1)*T - iota^2 + 5*iota + 3
501 103 (-iota^2 - 4*iota + 4)*T + 5*iota^2 - 3*iota
502 104 -4*iota^2*T + 3*iota^2 + 3*iota
503 105 (2*iota + 5)*T + 4*iota^2 + 3*iota + 1
504 106 (-iota + 1)*T - iota - 1
505 107 (4*iota^2 - iota + 1)*T + 7*iota^2 + iota - 2
506 108 (4*iota^2 - 1)*T + 5*iota^2 + 2*iota + 2
507 109 (2*iota + 1)*T + iota^2 - 4*iota
508 110 2*iota^2*T + iota^2 - 2*iota + 3
509 111 (2*iota^2 - 2*iota + 2)*T + iota^2 - 4*iota + 1
510 112 (iota^2 + iota)*T - 3*iota + 3
511 113 (iota^2 + 5*iota)*T + 3*iota^2 - 5*iota + 2
512 114 (-2*iota^2 + 2*iota - 4)*T + 2*iota^2 + 2*iota - 3
513 115 (-iota^2 - 3*iota)*T - 2*iota^2 - 7*iota
514 116 (iota^2 - 6*iota - 5)*T - 2*iota + 2
515 117 (-iota + 7)*T + 4*iota^2 - 1
516 118 (-2*iota + 7)*T + 2*iota^2 - iota + 1
517 119 (-6*iota^2 + 2*iota + 2)*T - iota^2 + iota - 2
518 120 -3*iota^2*T + 5*iota + 2
519 121 (-iota^2 + 3*iota + 2)*T + 6*iota^2
520 122 (-3*iota^2 + 3*iota - 3)*T + 2*iota^2 + 4
521 123 -iota*T + 4*iota^2 - 4*iota + 4
522 124 (-4*iota^2 - 2*iota - 4)*T - iota^2 - 3*iota + 4
523 125 (-4*iota^2 + 1)*T + 5*iota^2 + 3
524 126 (-iota - 1)*T + iota - 1
525 127 (-2*iota^2 + 4*iota + 2)*T - iota^2 + 4*iota + 1
526 128 (-6*iota^2 + 2)*T + 3*iota^2 + 1
527 129 (-iota^2 + 3*iota - 1)*T + 3*iota
528 130 (-2*iota^2 + 2*iota - 1)*T + iota^2 + 2*iota
529 131 (iota^2 + 5*iota - 2)*T + iota + 1
530 132 (iota^2 + 3*iota - 4)*T + 3*iota - 1
531 133 (3*iota - 3)*T + iota^2 + iota
532 134 (2*iota - 4)*T + iota^2 + 2*iota - 1
533 135 (-iota^2 + 2*iota - 3)*T + 2*iota^2
534 136 (iota^2 + 5*iota - 3)*T + 2*iota^2 - 3*iota + 2
535 137 (-2*iota^2 - 2*iota + 3)*T - 2*iota^2 + 2*iota - 4
536 138 (3*iota^2 + 5*iota - 4)*T - 3*iota - 2
537 139 (-4*iota^2 + 1)*T - iota + 7
538 140 (iota^2 - iota + 2)*T - 6*iota^2 + 2*iota + 2
539 141 (-3*iota^2 - 7*iota)*T - 2*iota^2
540 142 (2*iota^2 - 5*iota - 5)*T - 3*iota^2 - 1
541 143 -6*iota^2*T - iota^2 + 3*iota + 2
542 144 (-iota^2 + 6*iota + 1)*T - 4*iota^2 - iota + 2
543 145 (iota^2 + 3*iota - 5)*T - 4*iota^2 + 2*iota - 2
544 146 (-4*iota^2 + 4*iota - 4)*T - iota
545 147 (-iota - 1)*T + 2*iota
546 148 (-iota^2 - iota - 2)*T + iota - 1
547 149 (3*iota + 1)*T - 2*iota^2 - 5*iota - 1
548 150 (-2*iota^2 + 1)*T + iota^2 + 3*iota + 3
549 151 (-iota^2 + 3*iota + 1)*T - 3*iota^2 + 2
550 152 (-2*iota^2 + 3*iota - 2)*T - 5*iota^2
551 153 (-6*iota^2 + 3*iota - 1)*T - 2*iota^2 + 2
552 154 (-3*iota^2 + 3*iota)*T - 4*iota^2 + 4*iota + 4
553 155 (3*iota^2 + 1)*T + 3*iota^2 - 7*iota + 1
554 156 (-2*iota - 1)*T + 4*iota^2 - iota + 3
555 157 (2*iota^2 - 5)*T - 4*iota^2 + iota + 1
556 158 (-4*iota^2 + 2*iota - 2)*T + iota^2 - 6*iota + 2
557 159 (-3*iota^2 + 3*iota - 2)*T - iota^2 - 6*iota + 2
558 160 (iota^2 + 2*iota + 1)*T - iota^2 + 6
559 161 (-2*iota^2 - 2*iota - 2)*T - iota^2 - 7*iota
560 162 (-3*iota^2 - 5*iota + 5)*T - 2*iota^2 - 2*iota - 2
561 163 (-iota + 1)*T - iota^2 - iota - 2
562 164 -2*iota*T - iota - 1
563 165 (2*iota^2 + iota + 1)*T + iota - 1
564 166 (2*iota^2 - iota + 1)*T - 2
565 167 (-iota^2 + 3*iota - 1)*T - 4*iota^2 + 2*iota + 1
566 168 (3*iota^2 + 4*iota - 2)*T - iota^2 + 5*iota + 3
567 169 (4*iota^2 - 4*iota - 4)*T - 3*iota^2 + 3*iota
568 170 (-3*iota^2 - 3*iota + 3)*T + iota^2 - 3*iota + 2
569 171 (iota^2 - 6*iota + 2)*T + 4*iota^2 - 2*iota + 2
570 172 (2*iota^2 - 4*iota + 4)*T - 2*iota^2 - iota - 2
571 173 (3*iota^2 - 7*iota + 1)*T - 3*iota^2 - 1
572 174 (-iota^2 + 3*iota + 4)*T + 6*iota^2 + 2*iota - 1
573 175 (-6*iota^2 - 1)*T - 5*iota^2 + 2*iota - 1
574 176 (-4*iota^2 + iota - 1)*T + 2*iota^2 + 7*iota + 1
575 177 (-2*iota^2 - iota - 1)*T + 3*iota^2 + 7*iota
576 178 -2*iota^2*T - iota^2 + iota + 1
577 179 (2*iota^2 - 1)*T + 3*iota^2 - 3*iota
578 180 (3*iota^2 - 3)*T + 2*iota^2 - 5*iota + 2
579 181 (-2*iota + 1)*T - 3*iota^2 + 2*iota + 2
580 182 (4*iota^2 - 2*iota - 1)*T + 3*iota^2 - 4*iota + 2
581 183 (5*iota^2 - 4*iota + 1)*T + 4*iota^2 - 3*iota + 2
582 184 (iota^2 - 2*iota - 1)*T - 4*iota^2 + 4
583 185 -7*iota^2*T - 2*iota^2
584 186 (5*iota^2 - 4*iota + 2)*T - 2*iota^2 - 2*iota - 2
585 187 (-iota^2 - 1)*T - iota^2 - 6*iota - 5
586 188 (3*iota - 4)*T + 3*iota^2 + 3*iota
587 189 (4*iota^2 - iota - 2)*T - 5*iota^2 + 4*iota - 1
588 190 (-5*iota - 1)*T - 4*iota^2 + 2*iota + 2
589 191 (3*iota^2 - 5*iota - 3)*T - 4*iota^2 - iota + 3
590 192 (-iota^2 + iota + 1)*T + 2*iota^2
591 193 (iota^2 + iota)*T - iota^2 + 2*iota - 2
592 194 (2*iota^2 - 5*iota + 2)*T - 3*iota^2 + 3
593 195 (-2*iota^2 - iota + 3)*T + iota^2 + 2
594 196 (-4*iota^2 + 4)*T - iota^2 + 2*iota + 1
595 197 (-6*iota^2 + 2*iota)*T - 5*iota^2 + 2*iota - 1
596 198 (2*iota^2 + 5*iota - 2)*T + 4*iota^2 - 4*iota - 1
597 199 (6*iota^2 + 3*iota - 2)*T + iota^2 - 2*iota - 2
598 200 2*iota^2*T - 7*iota^2
599 201 (5*iota + 2)*T - 4*iota^2 - 2*iota
600 202 (5*iota^2 - 4*iota + 1)*T + 4*iota^2 - iota - 2
601 203 (-5*iota^2 + iota - 4)*T - 3*iota - 3
602 204 2*iota*T + iota^2 + 3*iota - 7
603 205 (-2*iota^2 + iota)*T - 2*iota^2 + 3*iota - 6
604 206 (4*iota^2 - 2*iota - 2)*T - 5*iota - 1
605 207 (-3*iota^2 + 2*iota + 1)*T - iota^2 - 7*iota + 1
606 208 (-3*iota^2 - 3*iota - 2)*T + 3*iota^2 - 4*iota - 4
607 209 (iota + 5)*T - 2*iota^2 - 6*iota - 2
608 210 (iota^2 + 4*iota + 3)*T - 3*iota^2
609 211 (-iota^2 + iota + 5)*T - 2*iota^2
610 212 (-iota^2 - 2*iota + 6)*T - iota^2 - iota
611 213 (2*iota^2 - 2)*T - iota - 5
612 214 -T - 5
613 215 (-2*iota + 2)*T - iota - 3
614 216 (2*iota + 2)*T - iota^2 + 5*iota + 2
615 217 (iota + 6)*T - 2*iota^2 + 4*iota + 1
616 218 (2*iota^2 + 2*iota + 6)*T - 3*iota^2 + 3*iota - 2
617 219 (iota^2 + 4*iota - 3)*T + 4*iota^2 - 3*iota + 3
618 220 (iota^2 + 7*iota)*T + 2*iota^2 + 2*iota + 2
619 221 (5*iota^2 + 3*iota + 2)*T + 2*iota^2 - 2*iota - 4
620 222 (3*iota^2 + 3*iota + 3)*T + 3*iota^2 + 4*iota + 4
621 223 (-iota + 1)*T - iota^2 + iota - 1
622 224 (-2*iota - 1)*T + 4*iota - 5
623 225 -5*T + 1
624 226 (-4*iota - 2)*T - 5*iota^2 + 3*iota - 1
625 227 (-iota^2 + iota - 3)*T + 2*iota^2 - iota - 2
626 228 (-iota^2 - 3)*T - iota - 1
627 229 (-iota^2 - iota - 2)*T - iota^2 - 2
628 230 -2*iota^2*T + iota^2 - iota - 5
629 231 (-3*iota^2 - 3)*T + iota^2 - 2*iota - 6
630 232 (6*iota + 1)*T + 3*iota^2 - 3
631 233 (-4*iota^2 - 2*iota - 6)*T - 2*iota^2 + 2*iota + 3
632 234 (-iota^2 - 2*iota + 1)*T + iota^2 + 1
633 235 (iota^2 + iota - 3)*T + iota^2
634 236 (3*iota^2 - 2*iota + 2)*T + 2*iota^2 - 2*iota - 5
635 237 (4*iota^2 - 4)*T + 3*iota^2 - 3
636 238 (-iota + 4)*T - 3*iota^2 + 4*iota
637 239 (2*iota^2 - 4)*T + iota^2 + 4*iota + 1
638 240 (-2*iota^2 + 2*iota + 4)*T + 3*iota^2 - iota + 4
639 241 (2*iota^2 - iota + 3)*T + iota^2 + 2*iota + 2
640 242 (4*iota^2 - 2*iota + 1)*T - 3*iota^2 + 6
641 243 (-iota^2 - 1)*T - iota^2 - 2*iota + 1
642 244 (iota^2 + 4*iota + 2)*T + 3*iota
643 245 (4*iota + 1)*T - iota^2 + iota + 1
644 246 (-2*iota^2 + 2*iota - 2)*T - iota^2 + iota - 4
645 247 (3*iota^2 - 3)*T - 4*iota^2 + 4
646 248 (-3*iota^2 - 7*iota - 3)*T - 2
647 249 (iota^2 - 3*iota + 1)*T + iota^2 + 6*iota - 1
648 250 (-3*iota^2 - 2*iota - 2)*T - 4*iota^2 + 3*iota + 4
649 251 (2*iota^2 - iota + 2)*T - iota^2 - 7*iota + 1
650 252 (iota^2 + 4)*T + iota^2 + 2*iota - 5
651 253 (2*iota^2 + iota + 4)*T - 3*iota^2 + 3*iota + 3
652 254 (-3*iota^2 + 6)*T - 4*iota^2 + 2*iota - 1
653 255 (-iota^2 - iota + 1)*T + iota^2 + iota + 1
654 256 (-2*iota^2 + 3)*T - 3*iota^2 + 3*iota
655 257 (-3*iota^2 - 2*iota + 4)*T + 3*iota - 1
656 258 (-iota^2 + iota + 1)*T - 2*iota^2 + 2*iota - 6
657 259 (-iota^2 - 3*iota + 4)*T - 2*iota + 1
658 260 (-3*iota^2 - 4*iota + 5)*T + 2*iota^2 + iota
659 261 (-2*iota^2 - iota + 2)*T + iota^2 + 2*iota - 7
660 262 (-4*iota + 4)*T + iota^2 - 5*iota + 1
661 263 (-2*iota^2 - 3*iota + 3)*T + 3*iota^2 - 6
662 264 (4*iota^2 + 5*iota - 3)*T + iota^2 - 2*iota + 3
663 265 (4*iota^2 + 4*iota + 1)*T - 3*iota^2 - 5*iota - 1
664 266 (-iota^2 + iota + 7)*T - 3*iota^2 + iota + 2
665 267 (2*iota^2 + 4*iota + 4)*T + 3*iota^2 - iota - 1
666 268 (-3*iota^2 + 3*iota - 3)*T + iota^2 + 2*iota + 6
667 269 (-6*iota^2 + iota + 1)*T + iota^2 - 4*iota + 4
668 270 (-iota^2 - iota - 1)*T - iota^2 - iota + 1
669 271 (3*iota^2 + 2*iota - 2)*T - iota + 3
670 272 (3*iota^2 + iota + 1)*T + 2
671 273 (-2*iota^2 + iota + 7)*T - iota^2 - 2*iota + 2
672 274 (-iota^2 - 2*iota - 5)*T + 4*iota^2 - 3
673 275 2*iota^2*T - 1
674 276 (2*iota^2 - 5*iota - 1)*T + iota^2 + 2*iota + 2
675 277 (-5*iota^2 + 4*iota - 2)*T - 2
676 278 (5*iota^2 - iota - 3)*T + iota^2 + 2*iota - 4
677 279 (3*iota^2 - 3*iota + 5)*T - iota^2 - iota - 1
678 280 (-3*iota^2 - 3*iota + 3)*T + 6*iota^2 - 2*iota - 2
679 281 (-6*iota^2 + iota)*T - 3*iota^2 - 4*iota + 1
680 282 (-4*iota - 3)*T + 5*iota^2 - 3*iota - 3
681 283 (-4*iota^2 + 3)*T - 5*iota^2 - 4*iota - 2
682 284 -T - 2*iota^2
683 285 (6*iota^2 - 3*iota - 3)*T - iota^2 - iota - 1
684 286 (iota^2 + 2*iota + 2)*T - 2*iota^2 + 5*iota + 1
685 287 (2*iota^2 + iota - 5)*T - 3*iota^2 - iota + 3
686 288 (iota^2 + 2*iota - 4)*T - 5*iota^2 + iota + 3
687 289 (3*iota - 2)*T - 5*iota^2 + 3*iota + 3
688 290 (-iota^2 + 4*iota + 1)*T - 3*iota^2 + 5*iota + 3
689 291 (-4*iota + 5)*T - 3*iota - 3
690 292 (-6*iota^2 + 2*iota + 2)*T - 3*iota^2 - 3*iota + 3
691 293 (-3*iota^2 + 2*iota - 2)*T - 4*iota - 5
692 294 (6*iota^2 + 1)*T - iota^2 - 5*iota
693 295 -3*T - 5*iota^2 - 3*iota + 2
694 296 (-2*iota - 3)*T - 3*iota^2 + iota + 2
695 297 (-3*iota - 3)*T - 2*iota^2 + 3*iota + 2
696 298 (-5*iota + 1)*T + 3*iota - 6
697 299 -2*iota^2*T + iota^2 - 2*iota - 6
698 300 (-2*iota^2 - 2*iota - 3)*T + 3*iota^2 + 5*iota
699 301 (-4*iota^2 + 2*iota - 2)*T + 5*iota^2 - 4
700 302 (-3*iota + 5)*T + 2*iota^2 - iota + 3
701 303 (-4*iota^2 + 2)*T + 6*iota^2 - 2*iota + 1
702 304 (2*iota^2 - 2*iota - 4)*T + 5*iota^2 + iota
703 305 (5*iota^2 + 3*iota - 2)*T - 3
704 306 (2*iota^2 - 3*iota - 2)*T - 3*iota - 3
705 307 (iota^2 + 1)*T - iota^2 - iota - 2
706 308 (-iota^2 + 2*iota + 6)*T - 2*iota^2
707 309 (4*iota^2 - 3*iota + 4)*T - iota^2 + 4*iota + 2
708 310 (-2*iota^2 - 1)*T - 2*iota
709 311 (iota^2 + 1)*T - iota^2 - 4*iota
710 312 (iota^2 - iota - 2)*T - iota^2 - 3*iota + 1
711 313 (-3*iota + 1)*T - 3*iota
712 314 (3*iota^2 - 4*iota)*T - iota^2 - 4*iota + 1
713 315 (-2*iota^2 + 2*iota - 2)*T + iota^2 + 5*iota + 3
714 316 (iota^2 + 2)*T - 3*iota^2 + 3*iota - 6
715 317 (-iota^2 - iota - 2)*T - 2*iota^2 + 2
716 318 (-iota^2 - 5*iota - 1)*T - iota^2 - iota - 4
717 319 (iota^2 + 5*iota + 3)*T + 2*iota^2 - 2*iota + 2
718 320 (-iota^2 + 3*iota + 5)*T - 4*iota^2 + 4
719 321 -2*iota^2*T - 4*iota^2 - 6*iota - 1
720 322 (-3*iota^2 + 3*iota - 6)*T - iota^2 - 2
721 323 (-4*iota^2 - 3*iota - 1)*T - 2*iota - 5
722 324 -iota*T - 2*iota^2 + iota - 1
723 325 (-2*iota^2 - 2*iota - 2)*T - iota^2 - 3*iota - 1
724 326 (-2*iota^2 - 3*iota - 3)*T - 2*iota^2 - 5*iota - 3
725 327 (2*iota^2 - iota + 5)*T - 2*iota
726 328 (-iota^2 - iota + 4)*T + 4*iota^2 + 2*iota + 3
727 329 (-iota^2 + iota + 5)*T + 6*iota^2 + iota - 3
728 330 (2*iota^2 - 1)*T + 3*iota^2 + 2*iota + 3
729 331 (-iota - 1)*T - 2*iota^2 + 1
730 332 (4*iota^2 + iota - 3)*T + 4
731 333 (iota^2 + iota + 2)*T - 2*iota^2 - iota + 3
732 334 (2*iota + 5)*T - iota^2 + 1
733 335 3*T - 5*iota^2 + 3
734 336 2*T - 4*iota^2 - 4*iota + 5
735 337 (-iota^2 + 4*iota + 2)*T + 4*iota^2 + 4*iota
736 338 (-5*iota^2 + iota + 2)*T - 4*iota^2 - 2*iota - 4
737 339 (iota^2 + 6*iota - 4)*T - 3*iota^2 + iota - 3
738 340 (iota^2 - 1)*T + 2*iota + 5
739 341 (3*iota - 5)*T + 3*iota^2 + iota - 2
740 342 -4*T + 4*iota^2 + iota - 3
741 343 (-iota^2 + 3*iota + 4)*T - iota + 3
742 344 (4*iota^2 + 4*iota)*T + iota^2 - 4*iota - 2
743 345 (5*iota^2 + iota)*T + 2*iota^2 - 2*iota + 2
744 346 (-4*iota^2 - iota - 2)*T + 2*iota^2 + 4
745 347 (-2*iota^2 - 7*iota - 1)*T + 4*iota^2 - iota + 1
746 348 (-iota^2 - iota - 2)*T - iota + 1
747 349 (-2*iota^2 - 3*iota - 5)*T + iota^2 + 4
748 350 (-2*iota^2 - iota)*T + 3*iota^2 - 2*iota - 3
749 351 (-2*iota^2 - 2*iota)*T + 5*iota^2 - 3*iota - 2
750 352 (-2*iota^2 - iota - 1)*T + 2*iota^2 + iota - 2
751 353 (-2*iota^2 - 2*iota - 2)*T + 3*iota^2 + 3*iota
752 354 (-3*iota^2 - 2*iota - 1)*T + 5*iota^2 + 5*iota - 3
753 355 (-4*iota^2 + 2*iota + 2)*T - 5*iota - 1
754 356 (2*iota^2 - iota + 1)*T + iota
755 357 (-iota + 1)*T + iota^2 + iota + 2
756 358 (3*iota^2 - 2*iota - 3)*T + 2*iota^2 + iota
757 359 (5*iota^2 - 3*iota - 2)*T + 2*iota^2 + 2*iota
758 360 (3*iota^2 + 3*iota)*T + 2*iota^2 + 2*iota + 2
759 361 (3*iota^2 - 6)*T + 4*iota^2 + iota + 1
760 362 (-5*iota - 1)*T + 4*iota^2 - 2*iota - 2
761 363 2*T + 4*iota^2 - iota
762 364 (-2*iota^2 + 2)*T + 5*iota^2 - iota + 2
763 365 (4*iota^2 - iota + 4)*T - iota^2 - iota + 4
764 366 (iota^2 - 3*iota + 3)*T - 2*iota^2 - iota + 1
765 367 2*T - 5*iota - 2
766 368 (5*iota^2 - 4)*T - 4*iota^2 + 2*iota - 2
767 369 (-5*iota^2 + 2*iota - 1)*T - 6*iota^2 - 1
768 370 (-5*iota^2 + 3*iota)*T + iota^2 + 4*iota - 4
769 371 -3*iota^2*T + 4*iota - 3
770 372 (-2*iota^2 + 2*iota)*T - 3*iota^2 + iota - 2
771 373 (-iota^2 - 1)*T - 3*iota^2 + 2*iota - 1
772 374 (-3*iota^2 + 6*iota - 2)*T - 4*iota^2 - 1
773 375 (-4*iota^2 - 3*iota - 1)*T + 4*iota^2 - 2*iota + 2
774 376 (3*iota^2 + 4*iota - 1)*T - 2*iota^2 + 3*iota - 1
775 377 (iota^2 + iota)*T - 2*iota^2 + 2*iota - 2
776 378 (-iota^2 - 5*iota - 1)*T - 6*iota^2 + 2*iota + 2
777 379 (iota^2 - iota + 4)*T + 2*iota^2 - 2*iota
778 380 (2*iota^2 - 2*iota)*T + 5*iota^2 - 3*iota + 2
779 381 (4*iota^2 - 3*iota - 1)*T - 3*iota^2 + 4*iota + 1
780 382 (-3*iota^2 - 3)*T - 3*iota^2 + iota - 4
781 383 (2*iota + 3)*T + iota
782 384 (-3*iota + 3)*T - 4*iota^2 + 2*iota - 2
783 385 (7*iota^2 + 3*iota - 1)*T - 2*iota^2 - 2*iota + 2
784 386 (iota^2 - 3*iota - 4)*T - iota^2 - 4*iota + 4
785 387 (-iota^2 - 4*iota - 1)*T - 2*iota^2 - 3*iota + 4
786 388 (3*iota^2 - 2*iota + 1)*T + 2*iota^2 + 5*iota + 1
787 389 (3*iota^2 - 3*iota + 2)*T + 6*iota^2 + 3*iota
788 390 -iota*T + 2*iota + 3
789 391 (-3*iota^2 + iota - 2)*T - 2*iota^2 + 2*iota
790 392 (-2*iota^2 - 4*iota)*T + 2*iota^2 + 3*iota - 1
791 393 (-4*iota^2 + 2*iota - 2)*T + 3*iota - 3
792 394 (-4*iota^2 - 1)*T + 3*iota^2 + 4*iota - 5
793 395 (-iota^2 - 4*iota + 4)*T - iota^2 + 3*iota + 4
794 396 (iota^2 - 4*iota - 2)*T + iota^2 + 6*iota
795 397 (3*iota^2 + 3)*T + iota^2 + 3*iota - 2
796 398 (2*iota^2 + 2*iota + 2)*T + 5*iota
797 399 -T
798 400 -iota*T - 1
799 401 iota^2*T - 1
800 402 -iota^2*T - 1
801 403 T - iota
802 404 T - iota^2
803 405 T + iota^2
804 406 T + iota - 1
805 407 iota*T + iota - 1
806 408 iota^2*T - iota - 1
807 409 -iota^2*T - iota - 1
808 410 -iota^2*T - iota^2 - 1
809 411 (iota + 1)*T - iota^2
810 412 (iota + 1)*T + iota^2
811 413 (iota^2 + 1)*T + iota^2
812 414 iota*T - iota^2 + iota - 1
813 415 (iota + 1)*T + iota - 1
814 416 (iota - 1)*T - iota - 1
815 417 (iota^2 - iota)*T - iota - 1
816 418 (-iota^2 + iota)*T - iota - 1
817 419 (iota^2 + 1)*T + iota^2 - 1
818 420 (iota^2 - 1)*T - iota^2 - 1
819 421 (-iota^2 + 1)*T - iota^2 - 1
820 422 (-iota^2 - 1)*T + iota^2 - 1
821 423 (iota + 1)*T - iota^2 + iota
822 424 (iota + 1)*T + iota^2 - iota
823 425 (iota^2 - iota + 1)*T - iota
824 426 (-iota^2 + 1)*T - iota^2 + iota - 1
825 427 (iota^2 - iota + 1)*T + iota^2 - 1
826 428 (iota^2 + iota + 1)*T + iota^2 - iota - 1
827 429 (iota^2 + iota - 1)*T - iota^2 + iota - 1
828 430 (iota^2 + iota - 1)*T + iota^2 - iota - 1
829 431 (iota^2 - iota + 1)*T + iota^2 - iota - 1
830 432 (iota^2 - iota - 1)*T - iota^2 - iota - 1
831 433 (-iota^2 + iota + 1)*T - iota^2 - iota - 1
832 434 (-iota^2 + iota + 1)*T + iota^2 + iota - 1
833 435 (-iota^2 - iota - 1)*T + iota^2 - iota - 1
834 436 T - 2
835 437 -T - 2
836 438 iota^2*T - 2
837 439 -iota^2*T - 2
838 440 (iota - 1)*T - 2
839 441 (-iota + 1)*T - 2
840 442 (iota^2 + iota)*T - 2
841 443 (-iota^2 - iota)*T - 2
842 444 (iota - 1)*T - iota^2 + iota - 2
843 445 (iota^2 - iota - 1)*T - iota - 2
844 446 (iota^2 - iota + 1)*T + iota^2 - 2
845 447 (iota^2 - iota - 1)*T - iota^2 - 2
846 448 (-iota^2 + iota + 1)*T - iota^2 - 2
847 449 (iota^2 + 1)*T + iota^2 - 2*iota
848 450 (-iota^2 + iota + 1)*T - 2*iota^2
849 451 (iota + 1)*T - 2*iota^2 - iota - 1
850 452 (-iota^2 + iota + 1)*T - 2*iota^2 - iota - 1
851 453 2*T - 1
852 454 2*T - iota^2
853 455 2*T + iota^2
854 456 2*T + iota - 1
855 457 2*T + iota^2 - 1
856 458 2*T - iota^2 - iota
857 459 2*T + iota^2 + iota
858 460 (iota^2 + 2)*T + iota^2 - iota - 1
859 461 -2*T - 1
860 462 (-iota^2 - 2)*T + iota^2 - iota - 1
861 463 (-iota^2 + iota - 2)*T + iota - 1
862 464 (-iota^2 + 2*iota)*T - iota^2 - 1
863 465 (2*iota^2 + iota + 1)*T - iota - 1
864 466 (2*iota^2 + iota + 1)*T + iota^2 - iota - 1
865 467 -2*iota^2*T + iota^2 - iota - 1
866 468 iota^2*T - 2*iota - 2
867 469 (iota^2 + iota - 1)*T - iota^2 + 2*iota - 2
868 470 (-iota^2 - iota + 1)*T - iota^2 + 2*iota - 2
869 471 (iota^2 - iota - 1)*T - 2*iota^2 - 2
870 472 (iota^2 - iota + 1)*T + 2*iota^2 + iota - 2
871 473 (-iota^2 - 2)*T - iota^2 - iota - 2
872 474 (iota^2 + 2*iota - 1)*T - iota - 2
873 475 -2*iota*T - iota^2 - 2
874 476 (-iota^2 - 1)*T - 2*iota^2 + 2*iota
875 477 (iota^2 + 2)*T + 2*iota
876 478 (-2*iota^2 + iota - 1)*T - iota^2 - 2*iota - 1
877 479 2*T - 2*iota^2 + iota - 1
878 480 -2*iota*T - 2*iota^2 - 1
879 481 (-iota^2 - 2*iota - 1)*T - 2*iota^2 + iota - 1
880 482 (2*iota^2 + iota)*T - 2*iota^2 - 1
881 483 (2*iota^2 + 1)*T - 2*iota^2 - iota
882 484 (2*iota^2 + iota - 1)*T - 2*iota^2 - 1
883 485 (2*iota^2 + 1)*T + 2*iota^2 - iota - 1
884 486 (2*iota^2 + 1)*T + 2*iota^2 + iota - 1
885 487 (-2*iota^2 + iota + 1)*T - 2*iota^2 - 1
886 488 (-2*iota^2 - iota + 1)*T - 2*iota^2 - 1
887 489 (-2*iota^2 - 1)*T + 2*iota^2 + iota - 1
888 490 (2*iota + 2)*T + iota^2
889 491 (-iota^2 + 2*iota - 2)*T + iota^2 + iota
890 492 (-iota^2 + 2*iota - 2)*T + iota^2 + iota - 1
891 493 (iota^2 - 2*iota + 2)*T + iota^2 + iota - 1
892 494 (2*iota^2 - iota + 2)*T + iota
893 495 (-2*iota^2 - 2)*T + iota^2 - iota - 1
894 496 (-2*iota^2 + 2*iota)*T - iota^2 - 1
895 497 (iota^2 + 1)*T - 2*iota^2 + 2*iota - 2
896 498 (-iota^2 - 2)*T - iota^2 + 2*iota - 2
897 499 (-2*iota^2 + iota - 1)*T + 2*iota - 2
898 500 (iota^2 - iota - 2)*T - 2*iota^2 - 2
899 501 (2*iota + 1)*T - 2*iota^2 - 2
900 502 (-iota^2 + 2*iota - 2)*T - iota^2 - 2
901 503 (-2*iota^2 - 2)*T + iota^2 - iota - 2
902 504 (-2*iota^2 + 2*iota)*T - iota^2 + iota - 2
903 505 (iota^2 + 2*iota)*T - 2*iota^2 + 2*iota - 1
904 506 (2*iota^2 + 2)*T - 2*iota - 1
905 507 (2*iota^2 - 2*iota + 2)*T - iota^2 - 1
906 508 (2*iota^2 - 2*iota + 2)*T - iota^2 - iota
907 509 (-iota + 2)*T - 2*iota^2 + 2*iota - 2
908 510 (-2*iota^2 - 2*iota)*T - 2*iota^2 - iota - 2
909 511 (2*iota^2 + iota + 2)*T + 2*iota^2 + 2*iota
910 512 (2*iota^2 + 2*iota)*T + 2*iota^2 - 2*iota - 1
911 513 (2*iota^2 - 2*iota - 1)*T - 2*iota^2 - 2*iota
912 514 (2*iota^2 - 2*iota - 1)*T + 2*iota^2 + 2*iota
913 515 (-2*iota^2 - 2*iota)*T + 2*iota^2 - 2*iota - 1
914 516 (-iota^2 - 2*iota + 2)*T - 2*iota^2 + 2*iota - 2
915 517 (-2*iota^2 + iota - 2)*T + 2*iota^2 + 2*iota - 2
916 518 (-2*iota^2 + 2*iota - 2)*T + 2*iota^2 - 2*iota - 1
917 519 T - 3
918 520 -T - 3
919 521 iota^2*T - 3
920 522 -iota^2*T - 3
921 523 (-iota^2 - iota)*T - 3
922 524 (-iota - 1)*T - iota^2 - 3
923 525 (-iota^2 - iota + 1)*T - 3
924 526 iota^2*T - 2*iota - 3
925 527 (-iota^2 + 1)*T - iota^2 - 2*iota - 3
926 528 (iota^2 + 1)*T + 2*iota - 3
927 529 (iota^2 + iota)*T - iota^2 + 2*iota - 3
928 530 2*T - 3
929 531 (iota + 2)*T + iota - 3
930 532 (iota^2 + 2)*T + iota - 3
931 533 -2*T - 3
932 534 (-iota - 2)*T + iota - 3
933 535 (iota - 2)*T - iota^2 + iota - 3
934 536 (iota^2 - iota - 2)*T - iota^2 + iota - 3
935 537 2*iota*T - 3
936 538 (2*iota - 1)*T - iota - 3
937 539 -2*iota*T - 3
938 540 (-2*iota + 1)*T - iota - 3
939 541 (-iota + 1)*T - 2*iota^2 + 2*iota - 3
940 542 (-iota^2 + 2*iota - 1)*T - 2*iota - 3
941 543 (iota^2 + 2*iota)*T - iota^2 + 2*iota - 3
942 544 -2*iota*T - iota^2 - 2*iota - 3
943 545 (2*iota^2 + 1)*T + iota^2 - 2*iota - 3
944 546 2*iota^2*T - iota^2 + 2*iota - 3
945 547 (2*iota^2 - iota + 1)*T - iota^2 + 2*iota - 3
946 548 (-2*iota^2 - 1)*T + iota^2 - 2*iota - 3
947 549 (-iota^2 - 2)*T + 2*iota^2 + iota - 3
948 550 (-2*iota^2 - 1)*T + 2*iota^2 - iota - 3
949 551 (iota^2 + 2*iota + 2)*T - iota^2 - 3
950 552 (2*iota^2 + 2)*T - 3
951 553 (2*iota^2 - iota - 2)*T - iota^2 + iota - 3
952 554 (-2*iota^2 - iota + 2)*T - 3
953 555 (-2*iota^2 - 2)*T - 3
954 556 (2*iota^2 + 2*iota + 1)*T - iota^2 - 3
955 557 (-iota^2 + iota - 2)*T + 2*iota^2 - 2*iota - 3
956 558 (2*iota - 2)*T - iota^2 - 2*iota - 3
957 559 (-2*iota^2 - 2)*T + iota^2 + 2*iota - 3
958 560 (-iota^2 - 2*iota - 2)*T - 2*iota^2 + iota - 3
959 561 (2*iota^2 - 2)*T - 2*iota^2 - 3
960 562 (-2*iota^2 + iota + 2)*T - 2*iota^2 + iota - 3
961 563 (-2*iota^2 + 2*iota - 2)*T - iota^2 + iota - 3
962 564 -iota^2*T - 2*iota^2 - 3*iota - 1
963 565 (iota^2 + 2)*T - iota^2 - 3*iota - 1
964 566 (iota^2 - 2*iota - 1)*T - 3*iota
965 567 (iota^2 - 2*iota)*T - iota^2 - 3*iota - 1
966 568 (2*iota - 1)*T - 2*iota^2 - 3*iota - 1
967 569 (-2*iota^2 - 2*iota - 1)*T - 3*iota
968 570 (-iota^2 - iota - 2)*T + 2*iota^2 - 3*iota - 2
969 571 (2*iota^2 - 2*iota - 1)*T - 3*iota - 2
970 572 (-2*iota^2 + 2*iota + 1)*T - 3*iota - 2
971 573 (2*iota^2 + 2*iota - 2)*T + iota^2 - 3*iota - 1
972 574 (2*iota + 1)*T + 3*iota - 1
973 575 (2*iota + 1)*T - iota^2 + 3*iota - 1
974 576 (-2*iota - 1)*T + 3*iota - 1
975 577 (2*iota^2 + 1)*T - 2*iota^2 + 3*iota - 1
976 578 (2*iota^2 + 1)*T - 2*iota^2 + 3*iota - 2
977 579 (-2*iota - 2)*T - iota^2 + 3*iota - 2
978 580 (-2*iota^2 - 2*iota - 2)*T + iota^2 + 3*iota - 1
979 581 (-iota^2 + iota + 1)*T - 3*iota^2
980 582 (-iota^2 - 2*iota)*T - 3*iota^2 + iota - 1
981 583 (-2*iota^2 - 1)*T - 3*iota^2 - iota
982 584 (-2*iota^2 + iota + 1)*T - 3*iota^2 - iota
983 585 -iota*T - 3*iota^2 + 2*iota - 2
984 586 (iota^2 + 2)*T - 3*iota^2 + 2*iota - 2
985 587 (2*iota^2 - iota - 2)*T - 3*iota^2 - iota - 2
986 588 (2*iota^2 + 2*iota)*T - 3*iota^2 + 2*iota - 1
987 589 (-2*iota^2 - 2*iota)*T - 3*iota^2 + 2*iota - 1
988 590 (2*iota^2 - 2*iota - 2)*T - 3*iota^2 - 1
989 591 (-2*iota^2 + iota - 1)*T + 3*iota^2 + 2*iota - 2
990 592 3*T - 1
991 593 3*T - iota^2
992 594 3*T + iota^2
993 595 3*T + iota^2 + iota
994 596 3*T + iota^2 + iota - 1
995 597 3*T - 2
996 598 (-iota + 3)*T - iota^2 - 2
997 599 3*T - 2*iota
998 600 3*T + 2*iota
999 601 (iota^2 + 3)*T - iota^2 - 2*iota - 2
1000 602 (iota + 3)*T + 2*iota - 2
1001 603 3*T - 2*iota^2 - 2
1002 604 (iota + 3)*T - 2*iota^2 - 2*iota
1003 605 (iota^2 + 3)*T - 2*iota^2 - 2*iota - 1
1004 606 (iota^2 - 2*iota + 3)*T + 2*iota^2
1005 607 (2*iota^2 - iota + 3)*T + 2*iota^2 - iota - 2
1006 608 -3*T - 1
1007 609 -3*T - iota^2 + iota - 1
1008 610 -3*T - 2
1009 611 (-iota^2 + iota - 3)*T + iota - 2
1010 612 (-iota^2 + iota - 3)*T + iota^2 - iota - 2
1011 613 -3*T - 2*iota^2 - 2
1012 614 -3*T + 2*iota^2 + iota - 2
1013 615 (-2*iota - 3)*T - iota^2 + 2*iota - 1
1014 616 (-2*iota^2 + 2*iota - 3)*T + iota - 1
1015 617 (-iota^2 + iota - 3)*T - 2*iota^2 + 2*iota - 2
1016 618 (-iota^2 + 2*iota - 3)*T + 2*iota - 2
1017 619 (-iota^2 - 2*iota - 3)*T + 2*iota - 2
1018 620 (iota^2 + 2*iota - 3)*T - 2*iota^2 - 2
1019 621 (-2*iota^2 - 3)*T + 2*iota^2 - 2
1020 622 (iota^2 + 3*iota + 1)*T - iota^2 - 2
1021 623 (iota^2 + 3*iota + 1)*T - iota^2 + 2*iota
1022 624 (-iota^2 + 3*iota - 1)*T - iota^2 - 2*iota - 2
1023 625 (iota^2 + 3*iota - 1)*T - 2*iota^2 - 2*iota - 2
1024 626 (-iota^2 + 3*iota - 2)*T - 2*iota - 2
1025 627 (-iota^2 - 3*iota)*T - 2*iota^2 + iota - 1
1026 628 -3*iota*T - 2*iota^2 - 2*iota - 1
1027 629 (iota^2 - 3*iota)*T - 2*iota^2 - 2*iota - 1
1028 630 (-2*iota^2 - 3*iota - 1)*T + 2*iota - 1
1029 631 (2*iota^2 - 3*iota - 2)*T - iota^2 - iota - 2
1030 632 (3*iota^2 - 2*iota + 2)*T - iota
1031 633 (3*iota^2 - 2*iota + 2)*T - iota^2 - 2
1032 634 (3*iota^2 - 2*iota + 1)*T - 2*iota^2 - 2*iota
1033 635 (3*iota^2 - 2*iota + 1)*T + 2*iota^2 + 2*iota
1034 636 -3*iota^2*T + iota^2 - iota - 1
1035 637 -3*iota^2*T - iota^2 - 2*iota - 1
1036 638 (-3*iota^2 - 1)*T + 2*iota^2 - 2*iota - 2
1037 639 (-3*iota^2 - iota - 2)*T + 2*iota^2 - iota - 2
1038 640 -2*T - iota^2 - 3*iota - 3
1039 641 (iota^2 - 2*iota + 1)*T - 3*iota - 3
1040 642 (iota^2 - 2*iota + 2)*T - 3*iota - 3
1041 643 (2*iota^2 + iota - 1)*T - iota^2 + 3*iota - 3
1042 644 (iota^2 + iota - 2)*T - 3*iota^2 - 2*iota - 3
1043 645 (iota^2 + 2*iota)*T + 3*iota^2 - 2*iota - 3
1044 646 (iota^2 - iota + 3)*T + 2*iota^2 - iota - 3
1045 647 (-2*iota^2 + iota + 3)*T - iota^2 + iota - 3
1046 648 (-iota^2 + iota - 3)*T + 2*iota - 3
1047 649 -3*T - 2*iota^2 - 2*iota - 3
1048 650 (-2*iota^2 - 2*iota - 3)*T - 3
1049 651 (-iota^2 - 3*iota + 1)*T - iota^2 - iota - 3
1050 652 3*iota^2*T - 2*iota - 3
1051 653 (-3*iota^2 + iota - 1)*T - 3
1052 654 (-3*iota^2 - iota + 1)*T - 3
1053 655 -3*iota^2*T - 2*iota - 3
1054 656 (-3*iota^2 + 2*iota - 2)*T - 2*iota^2 - iota - 3
1055 657 (iota^2 - 2*iota + 2)*T - 3*iota^2 - 3*iota
1056 658 (2*iota^2 + 2*iota)*T - 3*iota^2 + 3*iota - 2
1057 659 (-2*iota^2 - 2*iota)*T - 3*iota^2 + 3*iota - 2
1058 660 (iota^2 + iota + 3)*T + iota^2 + 3*iota - 1
1059 661 (2*iota^2 - 3*iota + 1)*T - iota^2 - 3*iota - 2
1060 662 (3*iota^2 - 2)*T + iota^2 - 3*iota - 1
1061 663 (3*iota^2 + iota + 1)*T - 2*iota^2 + 3*iota
1062 664 (3*iota^2 - 2*iota + 1)*T + iota^2 + 3*iota
1063 665 -3*iota^2*T - iota^2 - 3*iota - 2
1064 666 3*T - 3*iota^2 + 2*iota - 1
1065 667 (2*iota + 3)*T + 3*iota^2
1066 668 -3*T - 3*iota^2 + iota - 1
1067 669 (-2*iota^2 - iota - 3)*T - 3*iota^2 + 2*iota - 2
1068 670 (iota^2 + 3*iota + 2)*T + 3*iota^2
1069 671 (-iota^2 - 3*iota)*T - 3*iota^2 + 2*iota - 1
1070 672 (2*iota^2 - 3*iota)*T - 3*iota^2 - iota - 1
1071 673 (iota^2 + 3*iota + 3)*T - 2
1072 674 (3*iota + 3)*T - iota^2 + 2*iota - 2
1073 675 (-3*iota - 3)*T - iota^2 + 2*iota - 1
1074 676 (3*iota^2 + 2*iota + 3)*T + 2*iota^2 - 1
1075 677 (-3*iota^2 - 2*iota - 3)*T + iota^2 + iota - 2
1076 678 (3*iota^2 + 3*iota + 1)*T + 2*iota^2 + iota - 1
1077 679 (3*iota^2 - 3*iota + 1)*T + iota^2 - iota - 2
1078 680 (3*iota^2 - 3*iota + 2)*T - 2*iota^2 - 2*iota
1079 681 (3*iota^2 - 3*iota + 2)*T + 2*iota^2 + 2*iota
1080 682 (-iota^2 + 2*iota + 2)*T - 3*iota^2 - 3*iota - 3
1081 683 (-2*iota^2 - 2*iota + 1)*T + 3*iota^2 - 3*iota - 3
1082 684 (iota + 3)*T + 3*iota - 3
1083 685 (-2*iota^2 - iota - 3)*T - iota^2 + 3*iota - 3
1084 686 (-2*iota^2 + 3*iota + 1)*T - iota^2 - 3*iota - 3
1085 687 (-3*iota + 2)*T - iota^2 - 3*iota - 3
1086 688 (-iota^2 - 3*iota + 2)*T - iota^2 - 3*iota - 3
1087 689 (3*iota^2 - 2*iota + 2)*T + 3*iota - 3
1088 690 (-iota^2 + 3*iota - 3)*T - 2*iota^2 - iota - 3
1089 691 (-3*iota + 3)*T - iota - 3
1090 692 (3*iota^2 - 3*iota)*T - 2*iota^2 + 2*iota - 3
1091 693 (-3*iota^2 + 3*iota - 2)*T - iota^2 + iota - 3
1092 694 (-iota^2 + iota - 3)*T - 3*iota^2 + 3*iota - 2
1093 695 (iota^2 + 3*iota + 3)*T + 3*iota - 2
1094 696 (iota^2 + 3*iota + 3)*T + iota^2 + 3*iota - 2
1095 697 (-3*iota^2 + 3*iota + 2)*T + iota^2 + 3*iota - 1
1096 698 (3*iota^2 + 3*iota + 3)*T + iota^2 - 2*iota - 2
1097 699 (3*iota^2 - 3*iota - 3)*T + 2*iota^2 + 2*iota - 1
1098 700 (-2*iota^2 - 3)*T + 3*iota^2 - 3*iota - 3
1099 701 (-2*iota^2 + 2*iota - 3)*T + 3*iota^2 - 3*iota - 3
1100 702 (3*iota^2 - 3*iota - 3)*T - 2*iota^2 - 3
1101 703 (-3*iota^2 - 3*iota + 3)*T - 3*iota^2 + 2*iota - 2
Looking for smooth a,b pairs: done in 2.01
Decomposing primes in K1
# 1 primes (>= 1/128) at 0.03 (avg 31 ms each)
# 2 primes (>= 1/64) at 0.08 (avg 38 ms each)
# 3 primes (>= 1/32) at 0.11 (avg 38 ms each)
# 4 primes (>= 1/16) at 0.13 (avg 33 ms each)
# 6 primes (>= 1/8) at 0.22 (avg 36 ms each)
# 12 primes (>= 1/4) at 0.45 (avg 38 ms each)
# 23 primes (>= 1/2) at 0.92 (avg 40 ms each)
Decomposing primes in K2
# 1 primes (>= 1/128) at 0.01 (avg 9 ms each)
# 2 primes (>= 1/64) at 0.01 (avg 6 ms each)
# 3 primes (>= 1/32) at 0.01 (avg 5 ms each)
# 6 primes (>= 1/16) at 0.02 (avg 4 ms each)
# 11 primes (>= 1/8) at 0.05 (avg 5 ms each)
# 22 primes (>= 1/4) at 0.14 (avg 6 ms each)
# 44 primes (>= 1/2) at 0.32 (avg 7 ms each)
Decomposing primes (K1 and K2): done in 2.45 s
Factoring into ideals
0.01 1 -iota*T + 1
0.02 2 (3*iota^2 - 6*iota - 1)*T - 3*iota
0.04 3 (iota^2 - 2*iota - 1)*T - iota - 4
0.05 4 (iota^2 - 3*iota - 1)*T - iota - 3
0.06 5 (iota^2 - 4*iota - 1)*T - iota - 2
0.07 6 -T - 6
0.08 7 (-2*iota^2 + iota - 1)*T + 2*iota - 7
0.09 8 -2*T - iota^2 + iota - 4
0.11 9 (3*iota^2 - 2*iota - 3)*T - 2*iota^2 - iota
0.12 10 (2*iota^2 - iota - 3)*T - 2*iota^2 - 1
0.13 11 (iota^2 - iota - 3)*T - 2*iota^2 + iota - 1
0.15 12 (-iota^2 - 3*iota - 3)*T - 2*iota^2 + 3*iota + 1
0.16 13 (-2*iota^2 - 3)*T - 2*iota^2 + 4*iota - 2
0.18 14 (-4*iota^2 - 3)*T - 2*iota^2 + 6*iota - 2
0.19 15 (iota^2 - iota - 4)*T - 3*iota^2 + 2*iota + 1
0.21 16 (-3*iota^2 + 3*iota + 3)*T + 2*iota^2 - 5*iota - 2
0.22 17 (-iota^2 - iota + 1)*T + iota^2 - 6*iota - 2
0.24 18 (-2*iota^2 + 2*iota - 4)*T - 3*iota^2 - iota - 3
0.26 19 (-iota^2 + iota - 5)*T - 4*iota^2 - iota
0.27 20 -2*T + 4*iota^2 - 3*iota + 3
0.29 21 (-2*iota^2 - 5*iota - 6)*T + 2*iota^2 + iota
0.30 22 (-6*iota^2 + 3*iota - 3)*T + 3*iota^2 - 2*iota + 1
0.32 23 (-iota^2 + iota - 6)*T + iota^2 - 5*iota + 1
0.32 24 -T - iota
0.34 25 (4*iota^2 + iota - 2)*T + 5*iota^2 - 5
0.35 26 (2*iota^2 + iota)*T + 3*iota^2 - 2*iota - 3
0.36 27 (2*iota^2 - 2)*T + 2*iota^2 - 4*iota - 3
0.38 28 (iota^2 - iota + 4)*T - 2
0.39 29 (iota^2 - iota + 1)*T - 3*iota - 2
0.41 30 (iota^2 - iota)*T - 4*iota - 2
0.41 31 6*T - 1
0.43 32 (-4*iota + 2)*T - 4*iota^2 - 4*iota - 1
0.45 33 (-2*iota^2 + 3*iota + 7)*T + iota^2 - 3*iota + 1
0.47 34 (2*iota^2 + iota + 6)*T + 3*iota^2 - 2*iota - 4
0.48 35 (-2*iota - 6)*T + 4*iota^2 + iota + 1
0.50 36 (-2*iota^2 + 2)*T + 4*iota^2 + 5*iota + 3
0.52 37 (-iota^2 - 5*iota + 5)*T + 4*iota + 1
0.53 38 (-2*iota^2 + 4)*T + 4*iota^2 + iota + 2
0.55 39 (iota^2 - 5*iota - 1)*T + 2*iota^2 - 4*iota - 2
0.57 40 (-iota^2 - 5*iota)*T + 6*iota^2 + 1
0.58 41 (-3*iota^2 + 2*iota - 1)*T - 6*iota^2 + 3*iota - 3
0.60 42 (-3*iota^2 - 2*iota - 2)*T - 4*iota^2 - 3*iota - 4
0.62 43 (-3*iota^2 - 4*iota - 2)*T + 4*iota - 3
0.63 44 iota*T - 2*iota - 2
0.64 45 -T + 2*iota^2 - 4*iota - 3
0.65 46 (iota^2 - 2*iota)*T + 4*iota^2 - 3*iota - 1
0.67 47 (-iota^2 + 3*iota + 2)*T - 2*iota^2 + 4*iota
0.68 48 (-2*iota^2 + 3*iota - 1)*T - iota - 4
0.70 49 (-3*iota^2 + iota - 4)*T + 2*iota^2 - 2*iota - 4
0.72 50 (iota^2 - iota + 2)*T + 6*iota^2 - 2*iota - 2
0.73 51 (-4*iota^2 + 5*iota - 1)*T - 2*iota^2 + 4*iota - 3
0.74 52 (-iota^2 + iota + 2)*T + 4*iota^2 + 3*iota - 1
0.75 53 (-3*iota^2 + iota - 2)*T + 4*iota^2 + iota - 3
0.76 54 (2*iota^2 - iota + 3)*T - 6*iota^2 + 4*iota + 2
0.78 55 (iota^2 - 4*iota - 1)*T - 2*iota^2 + iota + 1
0.79 56 (-2*iota^2 - iota - 4)*T - 2*iota^2 - iota - 4
0.82 57 (2*iota^2 - 2*iota + 3)*T + iota - 1
0.84 58 (4*iota^2 + 3*iota + 4)*T + 3*iota^2 + 2*iota + 2
0.85 59 (-2*iota - 2)*T - iota
0.86 60 (-2*iota^2 + 4*iota)*T + iota^2 - 3*iota - 2
0.87 61 (iota - 2)*T + 2*iota^2 - 2*iota + 1
0.89 62 (6*iota^2 - 2*iota - 2)*T - iota^2 + iota - 2
0.90 63 (4*iota^2 + 3*iota - 1)*T + iota^2 - iota - 2
0.91 64 (4*iota^2 + iota - 3)*T + 3*iota^2 - iota + 2
0.93 65 (-2*iota^2 - 2*iota + 5)*T - 3*iota^2 - 2
0.94 66 (2*iota^2 - 4*iota + 2)*T + iota + 3
0.96 67 (-2*iota^2 + iota + 2)*T - 4*iota - 2
0.97 68 (-iota + 1)*T + 2*iota^2 - 2*iota + 3
0.99 69 2*iota^2*T - 4*iota - 3
1.00 70 (2*iota^2 - 3*iota - 3)*T + iota^2 - 5*iota - 1
1.02 71 (-2*iota^2 - 6*iota + 3)*T - 3*iota + 3
1.03 72 (-5*iota^2 + iota - 1)*T + 5*iota^2 - 3*iota + 1
1.06 73 (iota^2 - 4*iota - 3)*T + 4*iota^2 + 2
1.08 74 (5*iota^2 + iota + 1)*T + 4*iota^2 + 3*iota + 1
1.10 75 (2*iota^2 + 2*iota + 2)*T + 3*iota^2 + 5*iota - 5
1.11 76 (-iota^2 + iota + 1)*T + iota^2
1.12 77 3*iota*T - 3*iota + 4
1.13 78 (iota^2 + iota)*T - iota + 3
1.15 79 (3*iota^2 - iota - 3)*T + 2
1.16 80 (2*iota^2 - iota - 2)*T + 4*iota^2 + 3*iota
1.18 81 2*T + 5*iota^2 + 4*iota
1.20 82 (iota^2 - iota)*T + 6*iota^2 + 5*iota - 1
1.21 83 (5*iota^2 - 3*iota - 2)*T + iota^2 + 3*iota + 3
1.23 84 (-2*iota^2 + 6*iota + 2)*T + 3*iota^2 - 3*iota - 3
1.24 85 (2*iota^2 + 1)*T - iota^2 - 4
1.26 86 (4*iota^2 - iota + 3)*T - 5*iota^2 - iota
1.28 87 (3*iota^2 + 3*iota)*T + 4*iota^2
1.29 88 (-iota^2 - 4*iota - 1)*T + 5*iota^2 + iota - 3
1.31 89 (-iota^2 - iota + 4)*T + 4*iota^2 - iota + 4
1.33 90 (4*iota^2 + 2)*T + iota^2 - 4*iota - 3
1.34 91 (3*iota^2 + 3)*T + 5*iota^2 - iota - 5
1.36 92 (4*iota^2 + 3*iota + 1)*T + 3*iota^2 - 6*iota
1.37 93 -iota^2*T - iota^2 + iota + 1
1.38 94 (-iota^2 - iota - 2)*T + iota^2 + 1
1.39 95 (2*iota^2 + 2*iota - 4)*T + iota^2 + iota + 1
1.41 96 (-iota^2 + 2*iota - 4)*T - 2*iota^2 + 4*iota + 4
1.42 97 (-4*iota^2 + 2*iota - 2)*T + iota^2 + 3*iota - 5
1.44 98 (3*iota - 3)*T + 3*iota^2 + iota - 6
1.45 99 (-3*iota^2 + 3*iota + 3)*T - 2*iota^2 + 6*iota + 2
1.46 100 (5*iota^2 + 4*iota + 2)*T + 4*iota^2 - 3
1.48 101 (2*iota^2 + 5*iota + 1)*T - iota^2 + 5*iota + 3
1.50 102 (-iota^2 - 4*iota + 4)*T + 5*iota^2 - 3*iota
1.52 103 -4*iota^2*T + 3*iota^2 + 3*iota
1.54 104 (2*iota + 5)*T + 4*iota^2 + 3*iota + 1
1.55 105 (-iota + 1)*T - iota - 1
1.56 106 (4*iota^2 - iota + 1)*T + 7*iota^2 + iota - 2
1.58 107 (4*iota^2 - 1)*T + 5*iota^2 + 2*iota + 2
1.59 108 (2*iota + 1)*T + iota^2 - 4*iota
1.60 109 2*iota^2*T + iota^2 - 2*iota + 3
1.61 110 (2*iota^2 - 2*iota + 2)*T + iota^2 - 4*iota + 1
1.63 111 (iota^2 + iota)*T - 3*iota + 3
1.64 112 (iota^2 + 5*iota)*T + 3*iota^2 - 5*iota + 2
1.65 113 (-2*iota^2 + 2*iota - 4)*T + 2*iota^2 + 2*iota - 3
1.67 114 (-iota^2 - 3*iota)*T - 2*iota^2 - 7*iota
1.68 115 (iota^2 - 6*iota - 5)*T - 2*iota + 2
1.70 116 (-iota + 7)*T + 4*iota^2 - 1
1.71 117 (-2*iota + 7)*T + 2*iota^2 - iota + 1
1.73 118 (-6*iota^2 + 2*iota + 2)*T - iota^2 + iota - 2
1.74 119 -3*iota^2*T + 5*iota + 2
1.76 120 (-iota^2 + 3*iota + 2)*T + 6*iota^2
1.77 121 (-3*iota^2 + 3*iota - 3)*T + 2*iota^2 + 4
1.79 122 -iota*T + 4*iota^2 - 4*iota + 4
1.81 123 (-4*iota^2 - 2*iota - 4)*T - iota^2 - 3*iota + 4
1.83 124 (-4*iota^2 + 1)*T + 5*iota^2 + 3
1.85 125 (-iota - 1)*T + iota - 1
1.86 126 (-2*iota^2 + 4*iota + 2)*T - iota^2 + 4*iota + 1
1.87 127 (-6*iota^2 + 2)*T + 3*iota^2 + 1
1.89 128 (-iota^2 + 3*iota - 1)*T + 3*iota
1.91 129 (-2*iota^2 + 2*iota - 1)*T + iota^2 + 2*iota
1.92 130 (iota^2 + 5*iota - 2)*T + iota + 1
1.93 131 (iota^2 + 3*iota - 4)*T + 3*iota - 1
1.94 132 (3*iota - 3)*T + iota^2 + iota
1.95 133 (2*iota - 4)*T + iota^2 + 2*iota - 1
1.96 134 (-iota^2 + 2*iota - 3)*T + 2*iota^2
1.98 135 (iota^2 + 5*iota - 3)*T + 2*iota^2 - 3*iota + 2
1.99 136 (-2*iota^2 - 2*iota + 3)*T - 2*iota^2 + 2*iota - 4
2.01 137 (3*iota^2 + 5*iota - 4)*T - 3*iota - 2
2.03 138 (-4*iota^2 + 1)*T - iota + 7
2.04 139 (iota^2 - iota + 2)*T - 6*iota^2 + 2*iota + 2
2.06 140 (-3*iota^2 - 7*iota)*T - 2*iota^2
2.07 141 (2*iota^2 - 5*iota - 5)*T - 3*iota^2 - 1
2.09 142 -6*iota^2*T - iota^2 + 3*iota + 2
2.10 143 (-iota^2 + 6*iota + 1)*T - 4*iota^2 - iota + 2
2.12 144 (iota^2 + 3*iota - 5)*T - 4*iota^2 + 2*iota - 2
2.14 145 (-4*iota^2 + 4*iota - 4)*T - iota
2.14 146 (-iota - 1)*T + 2*iota
2.16 147 (-iota^2 - iota - 2)*T + iota - 1
2.17 148 (3*iota + 1)*T - 2*iota^2 - 5*iota - 1
2.18 149 (-2*iota^2 + 1)*T + iota^2 + 3*iota + 3
2.19 150 (-iota^2 + 3*iota + 1)*T - 3*iota^2 + 2
2.21 151 (-2*iota^2 + 3*iota - 2)*T - 5*iota^2
2.23 152 (-6*iota^2 + 3*iota - 1)*T - 2*iota^2 + 2
2.24 153 (-3*iota^2 + 3*iota)*T - 4*iota^2 + 4*iota + 4
2.27 154 (3*iota^2 + 1)*T + 3*iota^2 - 7*iota + 1
2.28 155 (-2*iota - 1)*T + 4*iota^2 - iota + 3
2.30 156 (2*iota^2 - 5)*T - 4*iota^2 + iota + 1
2.31 157 (-4*iota^2 + 2*iota - 2)*T + iota^2 - 6*iota + 2
2.33 158 (-3*iota^2 + 3*iota - 2)*T - iota^2 - 6*iota + 2
2.34 159 (iota^2 + 2*iota + 1)*T - iota^2 + 6
2.36 160 (-2*iota^2 - 2*iota - 2)*T - iota^2 - 7*iota
2.38 161 (-3*iota^2 - 5*iota + 5)*T - 2*iota^2 - 2*iota - 2
2.39 162 (-iota + 1)*T - iota^2 - iota - 2
2.40 163 -2*iota*T - iota - 1
2.41 164 (2*iota^2 + iota + 1)*T + iota - 1
2.43 165 (2*iota^2 - iota + 1)*T - 2
2.44 166 (-iota^2 + 3*iota - 1)*T - 4*iota^2 + 2*iota + 1
2.46 167 (3*iota^2 + 4*iota - 2)*T - iota^2 + 5*iota + 3
2.49 168 (4*iota^2 - 4*iota - 4)*T - 3*iota^2 + 3*iota
2.50 169 (-3*iota^2 - 3*iota + 3)*T + iota^2 - 3*iota + 2
2.52 170 (iota^2 - 6*iota + 2)*T + 4*iota^2 - 2*iota + 2
2.53 171 (2*iota^2 - 4*iota + 4)*T - 2*iota^2 - iota - 2
2.55 172 (3*iota^2 - 7*iota + 1)*T - 3*iota^2 - 1
2.57 173 (-iota^2 + 3*iota + 4)*T + 6*iota^2 + 2*iota - 1
2.59 174 (-6*iota^2 - 1)*T - 5*iota^2 + 2*iota - 1
2.60 175 (-4*iota^2 + iota - 1)*T + 2*iota^2 + 7*iota + 1
2.62 176 (-2*iota^2 - iota - 1)*T + 3*iota^2 + 7*iota
2.63 177 -2*iota^2*T - iota^2 + iota + 1
2.64 178 (2*iota^2 - 1)*T + 3*iota^2 - 3*iota
2.65 179 (3*iota^2 - 3)*T + 2*iota^2 - 5*iota + 2
2.66 180 (-2*iota + 1)*T - 3*iota^2 + 2*iota + 2
2.68 181 (4*iota^2 - 2*iota - 1)*T + 3*iota^2 - 4*iota + 2
2.69 182 (5*iota^2 - 4*iota + 1)*T + 4*iota^2 - 3*iota + 2
2.71 183 (iota^2 - 2*iota - 1)*T - 4*iota^2 + 4
2.72 184 -7*iota^2*T - 2*iota^2
2.74 185 (5*iota^2 - 4*iota + 2)*T - 2*iota^2 - 2*iota - 2
2.76 186 (-iota^2 - 1)*T - iota^2 - 6*iota - 5
2.77 187 (3*iota - 4)*T + 3*iota^2 + 3*iota
2.79 188 (4*iota^2 - iota - 2)*T - 5*iota^2 + 4*iota - 1
2.80 189 (-5*iota - 1)*T - 4*iota^2 + 2*iota + 2
2.82 190 (3*iota^2 - 5*iota - 3)*T - 4*iota^2 - iota + 3
2.83 191 (-iota^2 + iota + 1)*T + 2*iota^2
2.85 192 (iota^2 + iota)*T - iota^2 + 2*iota - 2
2.86 193 (2*iota^2 - 5*iota + 2)*T - 3*iota^2 + 3
2.87 194 (-2*iota^2 - iota + 3)*T + iota^2 + 2
2.88 195 (-4*iota^2 + 4)*T - iota^2 + 2*iota + 1
2.90 196 (-6*iota^2 + 2*iota)*T - 5*iota^2 + 2*iota - 1
2.91 197 (2*iota^2 + 5*iota - 2)*T + 4*iota^2 - 4*iota - 1
2.93 198 (6*iota^2 + 3*iota - 2)*T + iota^2 - 2*iota - 2
2.94 199 2*iota^2*T - 7*iota^2
2.96 200 (5*iota + 2)*T - 4*iota^2 - 2*iota
2.98 201 (5*iota^2 - 4*iota + 1)*T + 4*iota^2 - iota - 2
3.00 202 (-5*iota^2 + iota - 4)*T - 3*iota - 3
3.01 203 2*iota*T + iota^2 + 3*iota - 7
3.03 204 (-2*iota^2 + iota)*T - 2*iota^2 + 3*iota - 6
3.04 205 (4*iota^2 - 2*iota - 2)*T - 5*iota - 1
3.06 206 (-3*iota^2 + 2*iota + 1)*T - iota^2 - 7*iota + 1
3.09 207 (-3*iota^2 - 3*iota - 2)*T + 3*iota^2 - 4*iota - 4
3.10 208 (iota + 5)*T - 2*iota^2 - 6*iota - 2
3.12 209 (iota^2 + 4*iota + 3)*T - 3*iota^2
3.13 210 (-iota^2 + iota + 5)*T - 2*iota^2
3.15 211 (-iota^2 - 2*iota + 6)*T - iota^2 - iota
3.16 212 (2*iota^2 - 2)*T - iota - 5
3.17 213 -T - 5
3.18 214 (-2*iota + 2)*T - iota - 3
3.20 215 (2*iota + 2)*T - iota^2 + 5*iota + 2
3.22 216 (iota + 6)*T - 2*iota^2 + 4*iota + 1
3.23 217 (2*iota^2 + 2*iota + 6)*T - 3*iota^2 + 3*iota - 2
3.25 218 (iota^2 + 4*iota - 3)*T + 4*iota^2 - 3*iota + 3
3.27 219 (iota^2 + 7*iota)*T + 2*iota^2 + 2*iota + 2
3.28 220 (5*iota^2 + 3*iota + 2)*T + 2*iota^2 - 2*iota - 4
3.30 221 (3*iota^2 + 3*iota + 3)*T + 3*iota^2 + 4*iota + 4
3.31 222 (-iota + 1)*T - iota^2 + iota - 1
3.32 223 (-2*iota - 1)*T + 4*iota - 5
3.33 224 -5*T + 1
3.35 225 (-4*iota - 2)*T - 5*iota^2 + 3*iota - 1
3.36 226 (-iota^2 + iota - 3)*T + 2*iota^2 - iota - 2
3.37 227 (-iota^2 - 3)*T - iota - 1
3.38 228 (-iota^2 - iota - 2)*T - iota^2 - 2
3.40 229 -2*iota^2*T + iota^2 - iota - 5
3.41 230 (-3*iota^2 - 3)*T + iota^2 - 2*iota - 6
3.42 231 (6*iota + 1)*T + 3*iota^2 - 3
3.44 232 (-4*iota^2 - 2*iota - 6)*T - 2*iota^2 + 2*iota + 3
3.46 233 (-iota^2 - 2*iota + 1)*T + iota^2 + 1
3.47 234 (iota^2 + iota - 3)*T + iota^2
3.49 235 (3*iota^2 - 2*iota + 2)*T + 2*iota^2 - 2*iota - 5
3.51 236 (4*iota^2 - 4)*T + 3*iota^2 - 3
3.52 237 (-iota + 4)*T - 3*iota^2 + 4*iota
3.53 238 (2*iota^2 - 4)*T + iota^2 + 4*iota + 1
3.55 239 (-2*iota^2 + 2*iota + 4)*T + 3*iota^2 - iota + 4
3.57 240 (2*iota^2 - iota + 3)*T + iota^2 + 2*iota + 2
3.59 241 (4*iota^2 - 2*iota + 1)*T - 3*iota^2 + 6
3.60 242 (-iota^2 - 1)*T - iota^2 - 2*iota + 1
3.62 243 (iota^2 + 4*iota + 2)*T + 3*iota
3.63 244 (4*iota + 1)*T - iota^2 + iota + 1
3.65 245 (-2*iota^2 + 2*iota - 2)*T - iota^2 + iota - 4
3.66 246 (3*iota^2 - 3)*T - 4*iota^2 + 4
3.67 247 (-3*iota^2 - 7*iota - 3)*T - 2
3.69 248 (iota^2 - 3*iota + 1)*T + iota^2 + 6*iota - 1
3.71 249 (-3*iota^2 - 2*iota - 2)*T - 4*iota^2 + 3*iota + 4
3.72 250 (2*iota^2 - iota + 2)*T - iota^2 - 7*iota + 1
3.74 251 (iota^2 + 4)*T + iota^2 + 2*iota - 5
3.76 252 (2*iota^2 + iota + 4)*T - 3*iota^2 + 3*iota + 3
3.78 253 (-3*iota^2 + 6)*T - 4*iota^2 + 2*iota - 1
3.79 254 (-iota^2 - iota + 1)*T + iota^2 + iota + 1
3.80 255 (-2*iota^2 + 3)*T - 3*iota^2 + 3*iota
3.81 256 (-3*iota^2 - 2*iota + 4)*T + 3*iota - 1
3.83 257 (-iota^2 + iota + 1)*T - 2*iota^2 + 2*iota - 6
3.84 258 (-iota^2 - 3*iota + 4)*T - 2*iota + 1
3.86 259 (-3*iota^2 - 4*iota + 5)*T + 2*iota^2 + iota
3.88 260 (-2*iota^2 - iota + 2)*T + iota^2 + 2*iota - 7
3.89 261 (-4*iota + 4)*T + iota^2 - 5*iota + 1
3.91 262 (-2*iota^2 - 3*iota + 3)*T + 3*iota^2 - 6
3.93 263 (4*iota^2 + 5*iota - 3)*T + iota^2 - 2*iota + 3
3.94 264 (4*iota^2 + 4*iota + 1)*T - 3*iota^2 - 5*iota - 1
3.96 265 (-iota^2 + iota + 7)*T - 3*iota^2 + iota + 2
3.97 266 (2*iota^2 + 4*iota + 4)*T + 3*iota^2 - iota - 1
3.99 267 (-3*iota^2 + 3*iota - 3)*T + iota^2 + 2*iota + 6
4.01 268 (-6*iota^2 + iota + 1)*T + iota^2 - 4*iota + 4
4.02 269 (-iota^2 - iota - 1)*T - iota^2 - iota + 1
4.03 270 (3*iota^2 + 2*iota - 2)*T - iota + 3
4.04 271 (3*iota^2 + iota + 1)*T + 2
4.06 272 (-2*iota^2 + iota + 7)*T - iota^2 - 2*iota + 2
4.08 273 (-iota^2 - 2*iota - 5)*T + 4*iota^2 - 3
4.09 274 2*iota^2*T - 1
4.11 275 (2*iota^2 - 5*iota - 1)*T + iota^2 + 2*iota + 2
4.13 276 (-5*iota^2 + 4*iota - 2)*T - 2
4.14 277 (5*iota^2 - iota - 3)*T + iota^2 + 2*iota - 4
4.16 278 (3*iota^2 - 3*iota + 5)*T - iota^2 - iota - 1
4.17 279 (-3*iota^2 - 3*iota + 3)*T + 6*iota^2 - 2*iota - 2
4.19 280 (-6*iota^2 + iota)*T - 3*iota^2 - 4*iota + 1
4.20 281 (-4*iota - 3)*T + 5*iota^2 - 3*iota - 3
4.22 282 (-4*iota^2 + 3)*T - 5*iota^2 - 4*iota - 2
4.23 283 -T - 2*iota^2
4.25 284 (6*iota^2 - 3*iota - 3)*T - iota^2 - iota - 1
4.27 285 (iota^2 + 2*iota + 2)*T - 2*iota^2 + 5*iota + 1
4.28 286 (2*iota^2 + iota - 5)*T - 3*iota^2 - iota + 3
4.29 287 (iota^2 + 2*iota - 4)*T - 5*iota^2 + iota + 3
4.31 288 (3*iota - 2)*T - 5*iota^2 + 3*iota + 3
4.33 289 (-iota^2 + 4*iota + 1)*T - 3*iota^2 + 5*iota + 3
4.34 290 (-4*iota + 5)*T - 3*iota - 3
4.36 291 (-6*iota^2 + 2*iota + 2)*T - 3*iota^2 - 3*iota + 3
4.37 292 (-3*iota^2 + 2*iota - 2)*T - 4*iota - 5
4.39 293 (6*iota^2 + 1)*T - iota^2 - 5*iota
4.40 294 -3*T - 5*iota^2 - 3*iota + 2
4.41 295 (-2*iota - 3)*T - 3*iota^2 + iota + 2
4.42 296 (-3*iota - 3)*T - 2*iota^2 + 3*iota + 2
4.44 297 (-5*iota + 1)*T + 3*iota - 6
4.45 298 -2*iota^2*T + iota^2 - 2*iota - 6
4.47 299 (-2*iota^2 - 2*iota - 3)*T + 3*iota^2 + 5*iota
4.48 300 (-4*iota^2 + 2*iota - 2)*T + 5*iota^2 - 4
4.50 301 (-3*iota + 5)*T + 2*iota^2 - iota + 3
4.51 302 (-4*iota^2 + 2)*T + 6*iota^2 - 2*iota + 1
4.53 303 (2*iota^2 - 2*iota - 4)*T + 5*iota^2 + iota
4.54 304 (5*iota^2 + 3*iota - 2)*T - 3
4.55 305 (2*iota^2 - 3*iota - 2)*T - 3*iota - 3
4.56 306 (iota^2 + 1)*T - iota^2 - iota - 2
4.58 307 (-iota^2 + 2*iota + 6)*T - 2*iota^2
4.60 308 (4*iota^2 - 3*iota + 4)*T - iota^2 + 4*iota + 2
4.61 309 (-2*iota^2 - 1)*T - 2*iota
4.62 310 (iota^2 + 1)*T - iota^2 - 4*iota
4.64 311 (iota^2 - iota - 2)*T - iota^2 - 3*iota + 1
4.65 312 (-3*iota + 1)*T - 3*iota
4.66 313 (3*iota^2 - 4*iota)*T - iota^2 - 4*iota + 1
4.68 314 (-2*iota^2 + 2*iota - 2)*T + iota^2 + 5*iota + 3
4.69 315 (iota^2 + 2)*T - 3*iota^2 + 3*iota - 6
4.71 316 (-iota^2 - iota - 2)*T - 2*iota^2 + 2
4.72 317 (-iota^2 - 5*iota - 1)*T - iota^2 - iota - 4
4.74 318 (iota^2 + 5*iota + 3)*T + 2*iota^2 - 2*iota + 2
4.76 319 (-iota^2 + 3*iota + 5)*T - 4*iota^2 + 4
4.77 320 -2*iota^2*T - 4*iota^2 - 6*iota - 1
4.78 321 (-3*iota^2 + 3*iota - 6)*T - iota^2 - 2
4.80 322 (-4*iota^2 - 3*iota - 1)*T - 2*iota - 5
4.81 323 -iota*T - 2*iota^2 + iota - 1
4.82 324 (-2*iota^2 - 2*iota - 2)*T - iota^2 - 3*iota - 1
4.84 325 (-2*iota^2 - 3*iota - 3)*T - 2*iota^2 - 5*iota - 3
4.86 326 (2*iota^2 - iota + 5)*T - 2*iota
4.88 327 (-iota^2 - iota + 4)*T + 4*iota^2 + 2*iota + 3
4.89 328 (-iota^2 + iota + 5)*T + 6*iota^2 + iota - 3
4.91 329 (2*iota^2 - 1)*T + 3*iota^2 + 2*iota + 3
4.92 330 (-iota - 1)*T - 2*iota^2 + 1
4.93 331 (4*iota^2 + iota - 3)*T + 4
4.95 332 (iota^2 + iota + 2)*T - 2*iota^2 - iota + 3
4.97 333 (2*iota + 5)*T - iota^2 + 1
4.98 334 3*T - 5*iota^2 + 3
4.99 335 2*T - 4*iota^2 - 4*iota + 5
5.01 336 (-iota^2 + 4*iota + 2)*T + 4*iota^2 + 4*iota
5.03 337 (-5*iota^2 + iota + 2)*T - 4*iota^2 - 2*iota - 4
5.04 338 (iota^2 + 6*iota - 4)*T - 3*iota^2 + iota - 3
5.06 339 (iota^2 - 1)*T + 2*iota + 5
5.07 340 (3*iota - 5)*T + 3*iota^2 + iota - 2
5.08 341 -4*T + 4*iota^2 + iota - 3
5.10 342 (-iota^2 + 3*iota + 4)*T - iota + 3
5.12 343 (4*iota^2 + 4*iota)*T + iota^2 - 4*iota - 2
5.13 344 (5*iota^2 + iota)*T + 2*iota^2 - 2*iota + 2
5.15 345 (-4*iota^2 - iota - 2)*T + 2*iota^2 + 4
5.16 346 (-2*iota^2 - 7*iota - 1)*T + 4*iota^2 - iota + 1
5.18 347 (-iota^2 - iota - 2)*T - iota + 1
5.20 348 (-2*iota^2 - 3*iota - 5)*T + iota^2 + 4
5.21 349 (-2*iota^2 - iota)*T + 3*iota^2 - 2*iota - 3
5.23 350 (-2*iota^2 - 2*iota)*T + 5*iota^2 - 3*iota - 2
5.24 351 (-2*iota^2 - iota - 1)*T + 2*iota^2 + iota - 2
5.25 352 (-2*iota^2 - 2*iota - 2)*T + 3*iota^2 + 3*iota
5.27 353 (-3*iota^2 - 2*iota - 1)*T + 5*iota^2 + 5*iota - 3
5.28 354 (-4*iota^2 + 2*iota + 2)*T - 5*iota - 1
5.29 355 (2*iota^2 - iota + 1)*T + iota
5.30 356 (-iota + 1)*T + iota^2 + iota + 2
5.32 357 (3*iota^2 - 2*iota - 3)*T + 2*iota^2 + iota
5.33 358 (5*iota^2 - 3*iota - 2)*T + 2*iota^2 + 2*iota
5.35 359 (3*iota^2 + 3*iota)*T + 2*iota^2 + 2*iota + 2
5.36 360 (3*iota^2 - 6)*T + 4*iota^2 + iota + 1
5.38 361 (-5*iota - 1)*T + 4*iota^2 - 2*iota - 2
5.39 362 2*T + 4*iota^2 - iota
5.40 363 (-2*iota^2 + 2)*T + 5*iota^2 - iota + 2
5.42 364 (4*iota^2 - iota + 4)*T - iota^2 - iota + 4
5.44 365 (iota^2 - 3*iota + 3)*T - 2*iota^2 - iota + 1
5.45 366 2*T - 5*iota - 2
5.47 367 (5*iota^2 - 4)*T - 4*iota^2 + 2*iota - 2
5.49 368 (-5*iota^2 + 2*iota - 1)*T - 6*iota^2 - 1
5.51 369 (-5*iota^2 + 3*iota)*T + iota^2 + 4*iota - 4
5.52 370 -3*iota^2*T + 4*iota - 3
5.53 371 (-2*iota^2 + 2*iota)*T - 3*iota^2 + iota - 2
5.54 372 (-iota^2 - 1)*T - 3*iota^2 + 2*iota - 1
5.56 373 (-3*iota^2 + 6*iota - 2)*T - 4*iota^2 - 1
5.58 374 (-4*iota^2 - 3*iota - 1)*T + 4*iota^2 - 2*iota + 2
5.60 375 (3*iota^2 + 4*iota - 1)*T - 2*iota^2 + 3*iota - 1
5.61 376 (iota^2 + iota)*T - 2*iota^2 + 2*iota - 2
5.63 377 (-iota^2 - 5*iota - 1)*T - 6*iota^2 + 2*iota + 2
5.64 378 (iota^2 - iota + 4)*T + 2*iota^2 - 2*iota
5.66 379 (2*iota^2 - 2*iota)*T + 5*iota^2 - 3*iota + 2
5.67 380 (4*iota^2 - 3*iota - 1)*T - 3*iota^2 + 4*iota + 1
5.69 381 (-3*iota^2 - 3)*T - 3*iota^2 + iota - 4
5.70 382 (2*iota + 3)*T + iota
5.71 383 (-3*iota + 3)*T - 4*iota^2 + 2*iota - 2
5.73 384 (7*iota^2 + 3*iota - 1)*T - 2*iota^2 - 2*iota + 2
5.75 385 (iota^2 - 3*iota - 4)*T - iota^2 - 4*iota + 4
5.77 386 (-iota^2 - 4*iota - 1)*T - 2*iota^2 - 3*iota + 4
5.78 387 (3*iota^2 - 2*iota + 1)*T + 2*iota^2 + 5*iota + 1
5.80 388 (3*iota^2 - 3*iota + 2)*T + 6*iota^2 + 3*iota
5.81 389 -iota*T + 2*iota + 3
5.82 390 (-3*iota^2 + iota - 2)*T - 2*iota^2 + 2*iota
5.83 391 (-2*iota^2 - 4*iota)*T + 2*iota^2 + 3*iota - 1
5.85 392 (-4*iota^2 + 2*iota - 2)*T + 3*iota - 3
5.86 393 (-4*iota^2 - 1)*T + 3*iota^2 + 4*iota - 5
5.88 394 (-iota^2 - 4*iota + 4)*T - iota^2 + 3*iota + 4
5.90 395 (iota^2 - 4*iota - 2)*T + iota^2 + 6*iota
5.92 396 (3*iota^2 + 3)*T + iota^2 + 3*iota - 2
5.93 397 (2*iota^2 + 2*iota + 2)*T + 5*iota
11.25 398 -iota*T - 1
11.26 399 iota^2*T - 1
11.27 400 -iota^2*T - 1
11.27 401 T - iota
11.28 402 T - iota^2
11.29 403 T + iota^2
11.29 404 T + iota - 1
11.30 405 iota*T + iota - 1
11.31 406 iota^2*T - iota - 1
11.33 407 -iota^2*T - iota - 1
11.34 408 -iota^2*T - iota^2 - 1
11.35 409 (iota + 1)*T - iota^2
11.36 410 (iota + 1)*T + iota^2
11.38 411 (iota^2 + 1)*T + iota^2
11.39 412 iota*T - iota^2 + iota - 1
11.41 413 (iota + 1)*T + iota - 1
11.42 414 (iota - 1)*T - iota - 1
11.43 415 (iota^2 - iota)*T - iota - 1
11.44 416 (-iota^2 + iota)*T - iota - 1
11.45 417 (iota^2 + 1)*T + iota^2 - 1
11.46 418 (iota^2 - 1)*T - iota^2 - 1
11.48 419 (-iota^2 + 1)*T - iota^2 - 1
11.49 420 (-iota^2 - 1)*T + iota^2 - 1
11.50 421 (iota + 1)*T - iota^2 + iota
11.51 422 (iota + 1)*T + iota^2 - iota
11.53 423 (iota^2 - iota + 1)*T - iota
11.54 424 (-iota^2 + 1)*T - iota^2 + iota - 1
11.55 425 (iota^2 - iota + 1)*T + iota^2 - 1
11.57 426 (iota^2 + iota + 1)*T + iota^2 - iota - 1
11.58 427 (iota^2 + iota - 1)*T - iota^2 + iota - 1
11.59 428 (iota^2 + iota - 1)*T + iota^2 - iota - 1
11.60 429 (iota^2 - iota + 1)*T + iota^2 - iota - 1
11.62 430 (iota^2 - iota - 1)*T - iota^2 - iota - 1
11.63 431 (-iota^2 + iota + 1)*T - iota^2 - iota - 1
11.64 432 (-iota^2 + iota + 1)*T + iota^2 + iota - 1
11.66 433 (-iota^2 - iota - 1)*T + iota^2 - iota - 1
11.67 434 T - 2
11.68 435 -T - 2
11.69 436 iota^2*T - 2
11.70 437 -iota^2*T - 2
11.71 438 (iota - 1)*T - 2
11.72 439 (-iota + 1)*T - 2
11.73 440 (iota^2 + iota)*T - 2
11.74 441 (-iota^2 - iota)*T - 2
11.75 442 (iota - 1)*T - iota^2 + iota - 2
11.76 443 (iota^2 - iota - 1)*T - iota - 2
11.77 444 (iota^2 - iota + 1)*T + iota^2 - 2
11.78 445 (iota^2 - iota - 1)*T - iota^2 - 2
11.79 446 (-iota^2 + iota + 1)*T - iota^2 - 2
11.80 447 (iota^2 + 1)*T + iota^2 - 2*iota
11.81 448 (-iota^2 + iota + 1)*T - 2*iota^2
11.82 449 (iota + 1)*T - 2*iota^2 - iota - 1
11.83 450 (-iota^2 + iota + 1)*T - 2*iota^2 - iota - 1
11.84 451 2*T - 1
11.85 452 2*T - iota^2
11.86 453 2*T + iota^2
11.87 454 2*T + iota - 1
11.88 455 2*T + iota^2 - 1
11.89 456 2*T - iota^2 - iota
11.90 457 2*T + iota^2 + iota
11.91 458 (iota^2 + 2)*T + iota^2 - iota - 1
11.92 459 -2*T - 1
11.93 460 (-iota^2 - 2)*T + iota^2 - iota - 1
11.94 461 (-iota^2 + iota - 2)*T + iota - 1
11.95 462 (-iota^2 + 2*iota)*T - iota^2 - 1
11.96 463 (2*iota^2 + iota + 1)*T - iota - 1
11.97 464 (2*iota^2 + iota + 1)*T + iota^2 - iota - 1
11.98 465 -2*iota^2*T + iota^2 - iota - 1
11.99 466 iota^2*T - 2*iota - 2
12.01 467 (iota^2 + iota - 1)*T - iota^2 + 2*iota - 2
12.02 468 (-iota^2 - iota + 1)*T - iota^2 + 2*iota - 2
12.04 469 (iota^2 - iota - 1)*T - 2*iota^2 - 2
12.05 470 (iota^2 - iota + 1)*T + 2*iota^2 + iota - 2
12.06 471 (-iota^2 - 2)*T - iota^2 - iota - 2
12.07 472 (iota^2 + 2*iota - 1)*T - iota - 2
12.09 473 -2*iota*T - iota^2 - 2
12.10 474 (-iota^2 - 1)*T - 2*iota^2 + 2*iota
12.12 475 (iota^2 + 2)*T + 2*iota
12.13 476 (-2*iota^2 + iota - 1)*T - iota^2 - 2*iota - 1
12.14 477 2*T - 2*iota^2 + iota - 1
12.15 478 -2*iota*T - 2*iota^2 - 1
12.16 479 (-iota^2 - 2*iota - 1)*T - 2*iota^2 + iota - 1
12.17 480 (2*iota^2 + iota)*T - 2*iota^2 - 1
12.18 481 (2*iota^2 + 1)*T - 2*iota^2 - iota
12.20 482 (2*iota^2 + iota - 1)*T - 2*iota^2 - 1
12.22 483 (2*iota^2 + 1)*T + 2*iota^2 - iota - 1
12.24 484 (2*iota^2 + 1)*T + 2*iota^2 + iota - 1
12.25 485 (-2*iota^2 + iota + 1)*T - 2*iota^2 - 1
12.27 486 (-2*iota^2 - iota + 1)*T - 2*iota^2 - 1
12.28 487 (-2*iota^2 - 1)*T + 2*iota^2 + iota - 1
12.29 488 (2*iota + 2)*T + iota^2
12.30 489 (-iota^2 + 2*iota - 2)*T + iota^2 + iota
12.31 490 (-iota^2 + 2*iota - 2)*T + iota^2 + iota - 1
12.32 491 (iota^2 - 2*iota + 2)*T + iota^2 + iota - 1
12.34 492 (2*iota^2 - iota + 2)*T + iota
12.35 493 (-2*iota^2 - 2)*T + iota^2 - iota - 1
12.37 494 (-2*iota^2 + 2*iota)*T - iota^2 - 1
12.38 495 (iota^2 + 1)*T - 2*iota^2 + 2*iota - 2
12.39 496 (-iota^2 - 2)*T - iota^2 + 2*iota - 2
12.41 497 (-2*iota^2 + iota - 1)*T + 2*iota - 2
12.43 498 (iota^2 - iota - 2)*T - 2*iota^2 - 2
12.44 499 (2*iota + 1)*T - 2*iota^2 - 2
12.45 500 (-iota^2 + 2*iota - 2)*T - iota^2 - 2
12.47 501 (-2*iota^2 - 2)*T + iota^2 - iota - 2
12.48 502 (-2*iota^2 + 2*iota)*T - iota^2 + iota - 2
12.50 503 (iota^2 + 2*iota)*T - 2*iota^2 + 2*iota - 1
12.51 504 (2*iota^2 + 2)*T - 2*iota - 1
12.52 505 (2*iota^2 - 2*iota + 2)*T - iota^2 - 1
12.54 506 (2*iota^2 - 2*iota + 2)*T - iota^2 - iota
12.55 507 (-iota + 2)*T - 2*iota^2 + 2*iota - 2
12.56 508 (-2*iota^2 - 2*iota)*T - 2*iota^2 - iota - 2
12.58 509 (2*iota^2 + iota + 2)*T + 2*iota^2 + 2*iota
12.59 510 (2*iota^2 + 2*iota)*T + 2*iota^2 - 2*iota - 1
12.61 511 (2*iota^2 - 2*iota - 1)*T - 2*iota^2 - 2*iota
12.63 512 (2*iota^2 - 2*iota - 1)*T + 2*iota^2 + 2*iota
12.64 513 (-2*iota^2 - 2*iota)*T + 2*iota^2 - 2*iota - 1
12.66 514 (-iota^2 - 2*iota + 2)*T - 2*iota^2 + 2*iota - 2
12.67 515 (-2*iota^2 + iota - 2)*T + 2*iota^2 + 2*iota - 2
12.68 516 (-2*iota^2 + 2*iota - 2)*T + 2*iota^2 - 2*iota - 1
12.71 517 iota^2*T - 3
12.72 518 -iota^2*T - 3
12.73 519 (-iota^2 - iota)*T - 3
12.75 520 (-iota - 1)*T - iota^2 - 3
12.76 521 (-iota^2 - iota + 1)*T - 3
12.77 522 iota^2*T - 2*iota - 3
12.79 523 (-iota^2 + 1)*T - iota^2 - 2*iota - 3
12.80 524 (iota^2 + 1)*T + 2*iota - 3
12.82 525 (iota^2 + iota)*T - iota^2 + 2*iota - 3
12.83 526 2*T - 3
12.84 527 (iota + 2)*T + iota - 3
12.86 528 (iota^2 + 2)*T + iota - 3
12.87 529 -2*T - 3
12.88 530 (-iota - 2)*T + iota - 3
12.90 531 (iota - 2)*T - iota^2 + iota - 3
12.91 532 (iota^2 - iota - 2)*T - iota^2 + iota - 3
12.93 533 2*iota*T - 3
12.94 534 (2*iota - 1)*T - iota - 3
12.95 535 -2*iota*T - 3
12.96 536 (-2*iota + 1)*T - iota - 3
12.98 537 (-iota + 1)*T - 2*iota^2 + 2*iota - 3
12.99 538 (-iota^2 + 2*iota - 1)*T - 2*iota - 3
13.00 539 (iota^2 + 2*iota)*T - iota^2 + 2*iota - 3
13.02 540 -2*iota*T - iota^2 - 2*iota - 3
13.04 541 (2*iota^2 + 1)*T + iota^2 - 2*iota - 3
13.05 542 2*iota^2*T - iota^2 + 2*iota - 3
13.07 543 (2*iota^2 - iota + 1)*T - iota^2 + 2*iota - 3
13.08 544 (-2*iota^2 - 1)*T + iota^2 - 2*iota - 3
13.10 545 (-iota^2 - 2)*T + 2*iota^2 + iota - 3
13.11 546 (-2*iota^2 - 1)*T + 2*iota^2 - iota - 3
13.13 547 (iota^2 + 2*iota + 2)*T - iota^2 - 3
13.14 548 (2*iota^2 + 2)*T - 3
13.15 549 (2*iota^2 - iota - 2)*T - iota^2 + iota - 3
13.17 550 (-2*iota^2 - iota + 2)*T - 3
13.18 551 (-2*iota^2 - 2)*T - 3
13.20 552 (2*iota^2 + 2*iota + 1)*T - iota^2 - 3
13.21 553 (-iota^2 + iota - 2)*T + 2*iota^2 - 2*iota - 3
13.22 554 (2*iota - 2)*T - iota^2 - 2*iota - 3
13.24 555 (-2*iota^2 - 2)*T + iota^2 + 2*iota - 3
13.26 556 (-iota^2 - 2*iota - 2)*T - 2*iota^2 + iota - 3
13.28 557 (2*iota^2 - 2)*T - 2*iota^2 - 3
13.29 558 (-2*iota^2 + iota + 2)*T - 2*iota^2 + iota - 3
13.31 559 (-2*iota^2 + 2*iota - 2)*T - iota^2 + iota - 3
13.32 560 -iota^2*T - 2*iota^2 - 3*iota - 1
13.34 561 (iota^2 + 2)*T - iota^2 - 3*iota - 1
13.36 562 (iota^2 - 2*iota - 1)*T - 3*iota
13.37 563 (iota^2 - 2*iota)*T - iota^2 - 3*iota - 1
13.39 564 (2*iota - 1)*T - 2*iota^2 - 3*iota - 1
13.40 565 (-2*iota^2 - 2*iota - 1)*T - 3*iota
13.42 566 (-iota^2 - iota - 2)*T + 2*iota^2 - 3*iota - 2
13.43 567 (2*iota^2 - 2*iota - 1)*T - 3*iota - 2
13.45 568 (-2*iota^2 + 2*iota + 1)*T - 3*iota - 2
13.46 569 (2*iota^2 + 2*iota - 2)*T + iota^2 - 3*iota - 1
13.47 570 (2*iota + 1)*T + 3*iota - 1
13.49 571 (2*iota + 1)*T - iota^2 + 3*iota - 1
13.50 572 (-2*iota - 1)*T + 3*iota - 1
13.51 573 (2*iota^2 + 1)*T - 2*iota^2 + 3*iota - 1
13.53 574 (2*iota^2 + 1)*T - 2*iota^2 + 3*iota - 2
13.54 575 (-2*iota - 2)*T - iota^2 + 3*iota - 2
13.56 576 (-2*iota^2 - 2*iota - 2)*T + iota^2 + 3*iota - 1
13.57 577 (-iota^2 + iota + 1)*T - 3*iota^2
13.58 578 (-iota^2 - 2*iota)*T - 3*iota^2 + iota - 1
13.60 579 (-2*iota^2 - 1)*T - 3*iota^2 - iota
13.61 580 (-2*iota^2 + iota + 1)*T - 3*iota^2 - iota
13.62 581 -iota*T - 3*iota^2 + 2*iota - 2
13.64 582 (iota^2 + 2)*T - 3*iota^2 + 2*iota - 2
13.66 583 (2*iota^2 - iota - 2)*T - 3*iota^2 - iota - 2
13.67 584 (2*iota^2 + 2*iota)*T - 3*iota^2 + 2*iota - 1
13.68 585 (-2*iota^2 - 2*iota)*T - 3*iota^2 + 2*iota - 1
13.70 586 (2*iota^2 - 2*iota - 2)*T - 3*iota^2 - 1
13.71 587 (-2*iota^2 + iota - 1)*T + 3*iota^2 + 2*iota - 2
13.73 588 3*T - iota^2
13.74 589 3*T + iota^2
13.75 590 3*T + iota^2 + iota
13.76 591 3*T + iota^2 + iota - 1
13.77 592 3*T - 2
13.78 593 (-iota + 3)*T - iota^2 - 2
13.79 594 3*T - 2*iota
13.81 595 3*T + 2*iota
13.82 596 (iota^2 + 3)*T - iota^2 - 2*iota - 2
13.83 597 (iota + 3)*T + 2*iota - 2
13.85 598 3*T - 2*iota^2 - 2
13.86 599 (iota + 3)*T - 2*iota^2 - 2*iota
13.87 600 (iota^2 + 3)*T - 2*iota^2 - 2*iota - 1
13.89 601 (iota^2 - 2*iota + 3)*T + 2*iota^2
13.90 602 (2*iota^2 - iota + 3)*T + 2*iota^2 - iota - 2
13.92 603 -3*T - iota^2 + iota - 1
13.93 604 -3*T - 2
13.95 605 (-iota^2 + iota - 3)*T + iota - 2
13.96 606 (-iota^2 + iota - 3)*T + iota^2 - iota - 2
13.98 607 -3*T - 2*iota^2 - 2
13.99 608 -3*T + 2*iota^2 + iota - 2
14.01 609 (-2*iota - 3)*T - iota^2 + 2*iota - 1
14.02 610 (-2*iota^2 + 2*iota - 3)*T + iota - 1
14.04 611 (-iota^2 + iota - 3)*T - 2*iota^2 + 2*iota - 2
14.05 612 (-iota^2 + 2*iota - 3)*T + 2*iota - 2
14.07 613 (-iota^2 - 2*iota - 3)*T + 2*iota - 2
14.09 614 (iota^2 + 2*iota - 3)*T - 2*iota^2 - 2
14.10 615 (-2*iota^2 - 3)*T + 2*iota^2 - 2
14.12 616 (iota^2 + 3*iota + 1)*T - iota^2 - 2
14.13 617 (iota^2 + 3*iota + 1)*T - iota^2 + 2*iota
14.15 618 (-iota^2 + 3*iota - 1)*T - iota^2 - 2*iota - 2
14.16 619 (iota^2 + 3*iota - 1)*T - 2*iota^2 - 2*iota - 2
14.17 620 (-iota^2 + 3*iota - 2)*T - 2*iota - 2
14.19 621 (-iota^2 - 3*iota)*T - 2*iota^2 + iota - 1
14.20 622 -3*iota*T - 2*iota^2 - 2*iota - 1
14.21 623 (iota^2 - 3*iota)*T - 2*iota^2 - 2*iota - 1
14.22 624 (-2*iota^2 - 3*iota - 1)*T + 2*iota - 1
14.24 625 (2*iota^2 - 3*iota - 2)*T - iota^2 - iota - 2
14.25 626 (3*iota^2 - 2*iota + 2)*T - iota
14.27 627 (3*iota^2 - 2*iota + 2)*T - iota^2 - 2
14.28 628 (3*iota^2 - 2*iota + 1)*T - 2*iota^2 - 2*iota
14.30 629 (3*iota^2 - 2*iota + 1)*T + 2*iota^2 + 2*iota
14.31 630 -3*iota^2*T + iota^2 - iota - 1
14.32 631 -3*iota^2*T - iota^2 - 2*iota - 1
14.34 632 (-3*iota^2 - 1)*T + 2*iota^2 - 2*iota - 2
14.36 633 (-3*iota^2 - iota - 2)*T + 2*iota^2 - iota - 2
14.37 634 -2*T - iota^2 - 3*iota - 3
14.38 635 (iota^2 - 2*iota + 1)*T - 3*iota - 3
14.40 636 (iota^2 - 2*iota + 2)*T - 3*iota - 3
14.41 637 (2*iota^2 + iota - 1)*T - iota^2 + 3*iota - 3
14.43 638 (iota^2 + iota - 2)*T - 3*iota^2 - 2*iota - 3
14.44 639 (iota^2 + 2*iota)*T + 3*iota^2 - 2*iota - 3
14.45 640 (iota^2 - iota + 3)*T + 2*iota^2 - iota - 3
14.46 641 (-2*iota^2 + iota + 3)*T - iota^2 + iota - 3
14.48 642 (-iota^2 + iota - 3)*T + 2*iota - 3
14.49 643 -3*T - 2*iota^2 - 2*iota - 3
14.51 644 (-2*iota^2 - 2*iota - 3)*T - 3
14.52 645 (-iota^2 - 3*iota + 1)*T - iota^2 - iota - 3
14.53 646 3*iota^2*T - 2*iota - 3
14.55 647 (-3*iota^2 + iota - 1)*T - 3
14.56 648 (-3*iota^2 - iota + 1)*T - 3
14.57 649 -3*iota^2*T - 2*iota - 3
14.59 650 (-3*iota^2 + 2*iota - 2)*T - 2*iota^2 - iota - 3
14.61 651 (iota^2 - 2*iota + 2)*T - 3*iota^2 - 3*iota
14.62 652 (2*iota^2 + 2*iota)*T - 3*iota^2 + 3*iota - 2
14.63 653 (-2*iota^2 - 2*iota)*T - 3*iota^2 + 3*iota - 2
14.65 654 (iota^2 + iota + 3)*T + iota^2 + 3*iota - 1
14.67 655 (2*iota^2 - 3*iota + 1)*T - iota^2 - 3*iota - 2
14.68 656 (3*iota^2 - 2)*T + iota^2 - 3*iota - 1
14.69 657 (3*iota^2 + iota + 1)*T - 2*iota^2 + 3*iota
14.70 658 (3*iota^2 - 2*iota + 1)*T + iota^2 + 3*iota
14.72 659 -3*iota^2*T - iota^2 - 3*iota - 2
14.73 660 3*T - 3*iota^2 + 2*iota - 1
14.74 661 (2*iota + 3)*T + 3*iota^2
14.75 662 -3*T - 3*iota^2 + iota - 1
14.77 663 (-2*iota^2 - iota - 3)*T - 3*iota^2 + 2*iota - 2
14.79 664 (iota^2 + 3*iota + 2)*T + 3*iota^2
14.80 665 (-iota^2 - 3*iota)*T - 3*iota^2 + 2*iota - 1
14.82 666 (2*iota^2 - 3*iota)*T - 3*iota^2 - iota - 1
14.83 667 (iota^2 + 3*iota + 3)*T - 2
14.84 668 (3*iota + 3)*T - iota^2 + 2*iota - 2
14.85 669 (-3*iota - 3)*T - iota^2 + 2*iota - 1
14.87 670 (3*iota^2 + 2*iota + 3)*T + 2*iota^2 - 1
14.89 671 (-3*iota^2 - 2*iota - 3)*T + iota^2 + iota - 2
14.91 672 (3*iota^2 + 3*iota + 1)*T + 2*iota^2 + iota - 1
14.92 673 (3*iota^2 - 3*iota + 1)*T + iota^2 - iota - 2
14.93 674 (3*iota^2 - 3*iota + 2)*T - 2*iota^2 - 2*iota
14.95 675 (3*iota^2 - 3*iota + 2)*T + 2*iota^2 + 2*iota
14.97 676 (-iota^2 + 2*iota + 2)*T - 3*iota^2 - 3*iota - 3
14.98 677 (-2*iota^2 - 2*iota + 1)*T + 3*iota^2 - 3*iota - 3
14.99 678 (iota + 3)*T + 3*iota - 3
15.01 679 (-2*iota^2 - iota - 3)*T - iota^2 + 3*iota - 3
15.02 680 (-2*iota^2 + 3*iota + 1)*T - iota^2 - 3*iota - 3
15.04 681 (-3*iota + 2)*T - iota^2 - 3*iota - 3
15.05 682 (-iota^2 - 3*iota + 2)*T - iota^2 - 3*iota - 3
15.07 683 (3*iota^2 - 2*iota + 2)*T + 3*iota - 3
15.08 684 (-iota^2 + 3*iota - 3)*T - 2*iota^2 - iota - 3
15.09 685 (-3*iota + 3)*T - iota - 3
15.11 686 (3*iota^2 - 3*iota)*T - 2*iota^2 + 2*iota - 3
15.12 687 (-3*iota^2 + 3*iota - 2)*T - iota^2 + iota - 3
15.14 688 (-iota^2 + iota - 3)*T - 3*iota^2 + 3*iota - 2
15.15 689 (iota^2 + 3*iota + 3)*T + 3*iota - 2
15.17 690 (iota^2 + 3*iota + 3)*T + iota^2 + 3*iota - 2
15.18 691 (-3*iota^2 + 3*iota + 2)*T + iota^2 + 3*iota - 1
15.20 692 (3*iota^2 + 3*iota + 3)*T + iota^2 - 2*iota - 2
15.21 693 (3*iota^2 - 3*iota - 3)*T + 2*iota^2 + 2*iota - 1
15.22 694 (-2*iota^2 - 3)*T + 3*iota^2 - 3*iota - 3
15.24 695 (-2*iota^2 + 2*iota - 3)*T + 3*iota^2 - 3*iota - 3
15.25 696 (3*iota^2 - 3*iota - 3)*T - 2*iota^2 - 3
15.27 697 (-3*iota^2 - 3*iota + 3)*T - 3*iota^2 + 2*iota - 2
Factoring into ideals: done in 15.27
Computing Schirokauer maps
# 1 rows (>= 1/1024) at 0.04 (avg 38 ms each) (memory 0.32 GB)
# 2 rows (>= 1/512) at 0.07 (avg 34 ms each) (memory 0.32 GB)
# 3 rows (>= 1/256) at 0.10 (avg 33 ms each) (memory 0.32 GB)
# 6 rows (>= 1/128) at 0.19 (avg 32 ms each) (memory 0.32 GB)
# 11 rows (>= 1/64) at 0.34 (avg 31 ms each) (memory 0.32 GB)
# 22 rows (>= 1/32) at 0.65 (avg 29 ms each) (memory 0.32 GB)
# 44 rows (>= 1/16) at 1.24 (avg 28 ms each) (memory 0.33 GB)
# 88 rows (>= 1/8) at 2.46 (avg 28 ms each) (memory 0.34 GB)
# 175 rows (>= 1/4) at 4.88 (avg 28 ms each) (memory 0.35 GB)
# 349 rows (>= 1/2) at 9.83 (avg 28 ms each) (memory 0.39 GB)
# done at 19.64
Full matrix: 697 rows 1008 cols rank 697
starting modified_linear_algebra
######################### Right power #################################
1
Compressed matrix: 697 rows 168 cols rank 164
Compression yields 17 zero rows: [5, 30, 55, 183, 198, 212, 223, 235, 245, 433, 434, 450, 458, 525, 528, 591, 603]
Compressed kernel: Vector space of degree 168 and dimension 4 over Finite Field of size 43
Basis matrix:
4 x 168 dense matrix over Finite Field of size 43
Compressed kernel vector: 162/168 non-zero logs
Log vector: 972/1008 non-zero logs
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
character ratio =  16
ratio =  16
Computing unit groups
Minimum polynomial (in number fields) of units
[x^4 + 3*x^2 + 1, x^6 + 5*x^4 + 6*x^2 + 1, x^3 + x^2 - 2*x - 1, x^12 + 17*x^10 + 92*x^8 + 179*x^6 + 137*x^4 + 34*x^2 + 1, x^12 + 17*x^10 + 92*x^8 + 179*x^6 + 137*x^4 + 34*x^2 + 1]
[x^3 - x^2 - 2*x + 1, x^3 - x^2 - 2*x + 1]
Minimum polynomial (in GF(p^n)) of images of units
[x^2 + 6*x + 1, x^3 + 31*x^2 + 2*x + 31, x^3 + x^2 + 35*x + 36, x^6 + 6*x^5 + 8*x^4 + 30*x^3 + 9*x^2 + 24*x + 1, x^6 + 31*x^5 + 8*x^4 + 7*x^3 + 9*x^2 + 13*x + 1]
[x^3 + 36*x^2 + 35*x + 1, x^3 + 36*x^2 + 35*x + 1]
Vlog of units_orbits
[0, 0, 0, 41, 14]
[0, 0]
Schirokauer maps on units
[(0, 0), (0, 0), (0, 0), (32, 15), (34, 24)]
[(0), (0)]

Checking result: computing individual logs of 10 random elements
logarithm basis is  z6 

Getting image of vlog2 on lift of generator z6
# found decomposition after 12 attempts
Getting image of vlog2 on lift of generator z6: 15
# found decomposition after 7 attempts
-------
target in subgroup is y = 16*z6^5 + 16*z6^4 + 36*z6^3 + 26*z6^2 + 16*z6
log(y) is x = 8
Check g^x = 16*z6^5 + 16*z6^4 + 36*z6^3 + 26*z6^2 + 16*z6
Check passed! (we do have g^x == y)
# found decomposition after 6 attempts
-------
target in subgroup is y = 7*z6^5 + 10*z6^4 + 19*z6^3 + 15*z6^2 + 2*z6 + 21
log(y) is x = 12
Check g^x = 7*z6^5 + 10*z6^4 + 19*z6^3 + 15*z6^2 + 2*z6 + 21
Check passed! (we do have g^x == y)
# found decomposition after 3 attempts
-------
target in subgroup is y = 11*z6^5 + 22*z6^4 + 8*z6^3 + 21*z6^2 + 9*z6 + 30
log(y) is x = 35
Check g^x = 11*z6^5 + 22*z6^4 + 8*z6^3 + 21*z6^2 + 9*z6 + 30
Check passed! (we do have g^x == y)
# found decomposition after 22 attempts
-------
target in subgroup is y = 8*z6^5 + 15*z6^4 + 18*z6^3 + 21*z6^2 + 22*z6 + 29
log(y) is x = 10
Check g^x = 8*z6^5 + 15*z6^4 + 18*z6^3 + 21*z6^2 + 22*z6 + 29
Check passed! (we do have g^x == y)
# found decomposition after 11 attempts
-------
target in subgroup is y = 20*z6^5 + 23*z6^4 + 35*z6^3 + 31*z6^2 + 27*z6 + 11
log(y) is x = 37
Check g^x = 20*z6^5 + 23*z6^4 + 35*z6^3 + 31*z6^2 + 27*z6 + 11
Check passed! (we do have g^x == y)
# found decomposition after 33 attempts
-------
target in subgroup is y = 29*z6^5 + 14*z6^4 + 30*z6^3 + 22*z6^2 + 33*z6 + 2
log(y) is x = 3
Check g^x = 29*z6^5 + 14*z6^4 + 30*z6^3 + 22*z6^2 + 33*z6 + 2
Check passed! (we do have g^x == y)
# found decomposition after 21 attempts
-------
target in subgroup is y = 21*z6^5 + 24*z6^4 + 24*z6^3 + 24*z6^2 + 14*z6 + 9
log(y) is x = 11
Check g^x = 21*z6^5 + 24*z6^4 + 24*z6^3 + 24*z6^2 + 14*z6 + 9
Check passed! (we do have g^x == y)
# found decomposition after 25 attempts
-------
target in subgroup is y = 31*z6^4 + 4*z6^3 + 20*z6^2 + 31*z6 + 5
log(y) is x = 5
Check g^x = 31*z6^4 + 4*z6^3 + 20*z6^2 + 31*z6 + 5
Check passed! (we do have g^x == y)
# found decomposition after 3 attempts
-------
target in subgroup is y = 12*z6^5 + 22*z6^4 + 20*z6^3 + 14*z6^2 + 15*z6 + 33
log(y) is x = 7
Check g^x = 12*z6^5 + 22*z6^4 + 20*z6^3 + 14*z6^2 + 15*z6 + 33
Check passed! (we do have g^x == y)
# found decomposition after 4 attempts
-------
target in subgroup is y = 12*z6^5 + 35*z6^4 + 26*z6^3 + 33*z6^2 + 30*z6 + 21
log(y) is x = 34
Check g^x = 12*z6^5 + 35*z6^4 + 26*z6^3 + 33*z6^2 + 30*z6 + 21
Check passed! (we do have g^x == y)

