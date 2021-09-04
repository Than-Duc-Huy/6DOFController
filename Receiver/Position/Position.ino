#include <DynamixelShield.h>

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

void setup() {
  DEBUG_SERIAL.begin(115200);
  dxl.begin(1000000);
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);

  // Turn off torque when configuring items in EEPROM area
  for (int i = 1;i<=6;i++){
    dxl.torqueOff(DXL_ID[i]);
    dxl.setOperatingMode(DXL_ID[i],OP_POSITION);
    dxl.torqueOn(DXL_ID[i]);
  }
}

void loop() {
  for(int i = 1; i <=6; i++){
    dxl.setGoalPosition(DXL_ID[i], 512);
  }
}
