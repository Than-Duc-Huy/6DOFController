function val = AngleConvert(x,y)
    if (y == 'd' || y == "deg" || y == "degree")
        val = x*(360/4096);
    elseif (y == 'r' || y == "rad" || y == "radian")
        val = x*(2*pi/4096);
    else 
        val = x;
    end
end