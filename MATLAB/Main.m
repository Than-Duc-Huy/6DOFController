A = serialport("COM15",115200);
configureTerminator(A,"CR/LF");
flush(A);

% Variables
button = zeros(1,4); % Button Values
encval = zeros(1,12); % Encoder Values



% Main Loop
while(true)
    data = readline(A);
    if (data == "Start") 
        break 
    end
end


disp("Running")
f = figure('Name',"TR");

linkdata on

while(true)
    data = readline(A);
    newdata = split(data,',');
    receive = zeros(1,16);
    for i = 1:16
        receive(i) = double(newdata(i));
    end
    for i = 1:16
        if (i<5)
            button(i) = receive(i);
        else 
            encval(i-4) = AngleConvert(receive(i),"degree");
        end
    end
    disp(button)
    % Connecting the link

    plotvol([-3 3 -3 3 -3 3]);
    view([131.01 21.85])
    TrW4 = DHLink(-2,0,2,-90);
    Tr45 = TrW4*DHLink(2,180+encval(4),0,-90);
    Tr56 = Tr45*DHLink(0,-90+encval(5),0,90);
    Tr66 = Tr56*trotz(encval(6));
    trplot(eye(4),'framelabel','World','color','r');
    trplot(TrW4,'framelabel', 'W4', 'color', 'b');
    trplot(Tr45,'framelabel', '45', 'color', 'y');
    trplot(Tr56,'framelabel', '56', 'color', 'g');
    trplot(Tr66,'framelabel', 'Tip','color', 'r');
    pause(0.100);
    clf(f)
end



