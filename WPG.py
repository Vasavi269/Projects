import math
import numpy as np
from numpy import array
from numpy.linalg import norm
import matplotlib.pyplot as plt

points=[[0 ,0],[50, 300],[120, 450],[350, 440],[800, 200],[300, 150],[100, 10],[50,-150],[250,-300]]

for i in (range(len(points)-2)):
		
    a= points[i];
    b= points[i+1];
    c = points[i+2];
    raw = 25; # radius of circle about each waypoint

    #calculate point of intersection of circle and vectors
    v1 = np.array(a)-np.array(b);
    norm = np.linalg.norm(v1)
    u1 = v1/norm
    poi1 = b + raw*u1
    
    # calculating second point of intersection
    v2 = np.array(c)-np.array(b);
    norm = np.linalg.norm(v2)
    u2 = v2/norm
    poi2 = b + raw*u2
    print(poi1)
    print(poi2)
    
    #calculating angle between two unit vectors u1 and u2
    dot_product = np.dot(u1,u2)
    alpha = np.arccos(dot_product)
    print(alpha)# alpha is in radians
    
    # calculating radius of inscribed circle
    r = raw*math.tan(alpha/2);
    print(r)
    
    #calculating center of circle
    m1 = -((b[0]-a[0])/(b[1]-a[1]));
    b1 = -(m1*poi1[0])+poi1[1];
    m2 = -((c[0]-b[0])/(c[1]-b[1]));
    b2 = -(m2*poi2[0])+poi2[1];
    
    centerx = (b2-b1)/(m1-m2);
    centery = m1*centerx+b1;
    print(m2)
    print(b2)
    print(centerx)
    print(centery)
    
    plt.plot([a[0],b[0],c[0]],[a[1],b[1],c[1]],'-o')
    plt.plot([poi1[0],poi2[0]],[poi1[1], poi2[1]],'*')
    theta = np.linspace(0, 2*np.pi, 100)
    x1 = centerx + r*np.cos(theta)
    x2 = centery + r*np.sin(theta)
    plt.plot(x1, x2)
    
plt.savefig("result.png")
plt.show()
    


