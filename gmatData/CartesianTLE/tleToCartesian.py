from sgp4.api import Satrec
from sgp4.api import jday

s = '1 20580U 90037B   23280.62575685  .00008489  00000-0  44103-3 0  9997'
t = '2 20580  28.4687 239.3163 0002600 156.6472  11.0844 15.14323645638513'
satellite = Satrec.twoline2rv(s, t)

jd, fr = jday(1990, 4, 24, 12, 33, 50) # I pick an epoch (close to the TLE's)
e, r, v = satellite.sgp4(jd, fr) # e = error, r = position vector, v = speed vector
print (f'coordenadas {r}')
print (f'vector de salida {v}')
