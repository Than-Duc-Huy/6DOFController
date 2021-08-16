disp("Running");
A = serialport("COM15",921600);
configureTerminator(A,"CR/LF");
flush(A);

% Variables
button = zeros(1,4); % Button Values
encval = zeros(1,12); % Encoder Values
receive = zeros(1,16);
% Main Loop
% while(true)
%     if (readline(A) == "Start")
%         disp("Looping");
%         break
%     end
% end
pause(1)
f = figure('Name',"TR");

while(true)
    data = readline(A);
    newdata = split(data,',');
    disp(data)
    if (size(newdata,1) == 16)
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
        flush(A)
        % Connecting the link
        plotvol([-3 3 -1 7 -3 3]);
        view([80 30])
        
%       LEFT ARM
        LTrW4 = DHLink(-2,0,2,-90);
        LTr45 = LTrW4*DHLink(2,180+encval(4),0,-90);
        LTr56 = LTr45*DHLink(0,-90+encval(5),0,90);
        LTr66 = LTr56*trotz(encval(6));
        
        trplot(eye(4),'framelabel','World','color','r');
        trplot(LTrW4,'framelabel', 'W4', 'color', 'b');
        trplot(LTr45,'framelabel', '45', 'color', 'y');
        trplot(LTr56,'framelabel', '56', 'color', 'g');
        trplot(LTr66,'framelabel', 'Tip','color', 'r');
        
%       RIGHT ARM
        RWorld= transl(0,6,0);
        RTrW4 = RWorld*DHLink(-2,0,2,90);
        RTr45 = RTrW4*DHLink(2,180+encval(10),0,90);
        RTr56 = RTr45*DHLink(0,-90+encval(11),0,90);
        RTr66 = RTr56*trotz(encval(12));
        
        trplot(RWorld,'framelabel','World','color','r');
        trplot(RTrW4,'framelabel', 'W4', 'color', 'b');
        trplot(RTr45,'framelabel', '45', 'color', 'y');
        trplot(RTr56,'framelabel', '56', 'color', 'g');
        trplot(RTr66,'framelabel', 'Tip','color', 'r');
        
        pause(0.0001);
        clf(f)
    end
end



