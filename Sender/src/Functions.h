#include <Arduino.h>
#include <Wire.h>

//========= Communications
void CheckI2CM(uint8_t muxaddr);
void CheckI2C();
void Tcaselect(uint8_t i, uint8_t muxaddr);



//========= Encoders
double AngleConvert(double input, String a);
double ReadMagEnc();
double ReadMux(uint8_t select, uint8_t muxaddr, String mode);
double ReadQuadEnc(int A, int B);