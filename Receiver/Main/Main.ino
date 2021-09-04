#include <DynamixelShield.h>
#include <string.h>
#include <Servo.h>
#include <SimpleKalmanFilter.h>

SimpleKalmanFilter OL1(2,1,0.01);
SimpleKalmanFilter OL2(2,1,0.01);
SimpleKalmanFilter OL3(1,1,0.01);
SimpleKalmanFilter OL4(1,1,0.01);
SimpleKalmanFilter OL5(1,1,0.01);
SimpleKalmanFilter OL6(1,1,0.01);

SimpleKalmanFilter OR1(2,2,0.01);
SimpleKalmanFilter OR2(2,2,0.01);
SimpleKalmanFilter OR3(2,2,0.01);
SimpleKalmanFilter OR4(2,2,0.01);
SimpleKalmanFilter OR5(2,2,0.01);
SimpleKalmanFilter OR6(2,2,0.01);


//Servo L;
//Servo R;
//#define ServoL
//#define ServoR
//int claw;
//==================================================================CHARACTER PARSING
char *b ; // Turn String to Char array
float data[16];  // Store Number
float prev[16];
float joint[13];
char *token; // Place to store token
int count = 0;
String a;

int clocktime=0;

//====================================================================DYNAMIXEL SETUP
#if defined(ARDUINO_AVR_UNO) || defined(ARDUINO_AVR_MEGA2560)
  #include <SoftwareSerial.h>
  SoftwareSerial soft_serial(7, 8); // DYNAMIXELShield UART RX/TX
  #define DEBUG_SERIAL soft_serial
#elif defined(ARDUINO_SAM_DUE) || defined(ARDUINO_SAM_ZERO)
  #define DEBUG_SERIAL SerialUSB    
#else
  #define DEBUG_SERIAL Serial
#endif

const uint8_t DXL_ID[7] = {0,1,2,3,4,5,6};
const float DXL_PROTOCOL_VERSION = 2.0;

DynamixelShield dxl;

//This namespace is required to use Control table item names
using namespace ControlTableItem;
//=============================================================================================
void setup() {
  DEBUG_SERIAL.begin(115200);

  dxl.begin(1000000);

  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);

  dxl.writeControlTableItem(TORQUE_LIMIT, DXL_ID, 50);
  dxl.writeControlTableItem(MAX_POSITION_LIMIT, DXL_ID, 873);
  dxl.writeControlTableItem(MIN_POSITION_LIMIT, DXL_ID, 150);
  
  for (int i = 1;i<=6;i++){
    dxl.torqueOff(DXL_ID[i]);
    dxl.setOperatingMode(DXL_ID[i],OP_POSITION);
    dxl.torqueOn(DXL_ID[i]);
    dxl.ledOn(DXL_ID[i]);
  }

  for(int i = 1; i <=6; i++){
    dxl.setGoalPosition(DXL_ID[i], 512);
  }
  delay(3000);
  Serial3.begin(115200);

  pinMode(6,INPUT_PULLUP);
  pinMode(LED_BUILTIN,OUTPUT);

  for(int i = 1; i <=6; i++){
    dxl.setGoalPosition(DXL_ID[i], 512);
  }

  //============================Servo
//  pinMode(ServoL, OUTPUT);
//  pinMode(SerovR, OUTPUT);
//  L.attach(ServoL);
//  R.attach(ServoR);
} 

void loop() {
  //=============================READ
  if(Serial3.available() !=0){
    a = Serial3.readStringUntil('\n');
    b = &a[0];
    token = strtok(b,",");
    count = 0;
    while (token != NULL){
      data[count] = atof(token)+150; // atof is char->float. Store token into Number
      token = strtok(NULL,","); // Move through the token
//      DEBUG_SERIAL.print(data[count]);
//      DEBUG_SERIAL.print("\t");
      count++;
    }
//    DEBUG_SERIAL.println();
  }


    for(int i = 4; i<16;i++){
      if (data[i] >= 0 && data[i] <=300) continue;
      else data[i] = prev[i];
    }
    

    joint[7] = OR1.updateEstimate(data[10]);
    joint[8] = OR2.updateEstimate(data[11]);
    joint[9] = OR3.updateEstimate(data[12]);
    joint[10] = OR4.updateEstimate(data[13]);
    joint[11] = OR5.updateEstimate(data[14]);
    joint[12] = OR6.updateEstimate(data[15]);

//  //=======================CLAW
////  claw = (joint[0] == 1)? 180 : 0;
////  L.write(claw);
////  claw = (joint[2] ==1)? 180 : 0;
////  R.write(claw);
//  //========================JOINT

  for(int i = 7 ; i<=12 ; i++){
    DEBUG_SERIAL.print(joint[i]);
    DEBUG_SERIAL.print("\t");
  }
  DEBUG_SERIAL.println();
  



  if(digitalRead(6) == 1){  // BUTTON ON
    digitalWrite(LED_BUILTIN,1);
    if(clocktime % 50 == 0){
      dxl.setGoalPosition(DXL_ID[1], joint[7],UNIT_DEGREE);
      dxl.setGoalPosition(DXL_ID[2], joint[8],UNIT_DEGREE);
      dxl.setGoalPosition(DXL_ID[3], joint[9],UNIT_DEGREE);
//      dxl.setGoalPosition(DXL_ID[4], joint[10],UNIT_DEGREE);
//      dxl.setGoalPosition(DXL_ID[5], joint[11],UNIT_DEGREE);
//      dxl.setGoalPosition(DXL_ID[6], joint[12],UNIT_DEGREE);

    }
  }
  else digitalWrite(LED_BUILTIN,0); // BUTTON OFF
  for(int i = 0;i<16;i++){
    prev[i] = data[i];
  }
  clocktime++;
}
