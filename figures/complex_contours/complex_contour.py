from nhqm.bases.gen_contour import triangle_contour
import scipy as sp
import os

order = 50
peak_x = 0.5
peak_y = 0.5
k_max = 1.8

contour = triangle_contour(peak_x, peak_y, k_max, order/3)

points, _ = contour
contourdata = sp.array([sp.real(points), sp.imag(points)])
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "contour.data", contourdata.T)