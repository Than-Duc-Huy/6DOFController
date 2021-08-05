A = serialport("COM9",115200);
configureTerminator(A,"CR/LF");
flush(A);
%Define data structure
A.UserData = struct("Joints",[],"Button",[]);