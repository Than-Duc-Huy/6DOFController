function T = DHLink(d,theta,r,alpha)
    Tz = transl(0,0,d);
    Rz = trotz(theta);
    Tx = transl(r,0,0);
    Rx = trotx(alpha);
    T  = Tz*Rz*Tx*Rx;
end