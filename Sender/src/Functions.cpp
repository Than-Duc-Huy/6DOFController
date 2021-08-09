#include <Wire.h>
#include <Arduino.h>
#include <AS5600.h>
// #include <Encoder.h>
//==================== I2C Multiplexor ========================
//===== Select the pathway
void Tcaselect(uint8_t i, uint8_t muxaddr) { // Select a path way
  if (i > 7) return;
  Wire.beginTransmission(muxaddr); // Start transmit to TCAADDR
  Wire.write(1 << i); // Left shift 1 based on the variable i to select a path way
  Wire.endTransmission();  // End transmit
}

//===== Multiplexor I2C Scan
void CheckI2CM(uint8_t muxaddr){
	while (!Serial);
	delay(1000);
	Wire.begin();
	Serial.begin(115200);
	Serial.println("\nTCAScanner ready!");
	
	for (uint8_t t=0; t<8; t++) { // run through 8 way
		Tcaselect(t,muxaddr); // Select each
		Serial.print("TCA Port #"); Serial.println(t); // Port number
	for (uint8_t addr = 0; addr<=127; addr++) { // run through 128 addresses
		if (addr == muxaddr) continue;  // Ignore the TCA Address

		Wire.beginTransmission(addr); // begin transmission to each address
		if (!Wire.endTransmission()) { // If there isn't any endTransmission, it means that there is an address
		Serial.print("Found I2C 0x");  Serial.println(addr,HEX); // Print out the address
		}
	}
	}
	Serial.println("\ndone");
}

//========================= NORMAL I2C
//===== Check I2C
void CheckI2C(){
	while (!Serial); // Waiting for Serial Monitor
	Serial.println("\nI2C Scanner");

	byte error, address; //variable for error and I2C address
	int nDevices;
	nDevices = 0;

	Serial.println("Scanning...");
	for (address = 1; address < 127; address++ )
	{
	// The i2c_scanner uses the return value of
	// the Write.endTransmisstion to see if
	// a device did acknowledge to the address.
	Wire.beginTransmission(address);
	error = Wire.endTransmission();
	if (error == 0)
	{
		Serial.print("I2C device found at address 0x");
		if (address < 16)
		Serial.print("0");
		Serial.print(address, HEX);
		Serial.println("  !");
		nDevices++;
	}
	else if (error == 4)
	{
		Serial.print("Unknown error at address 0x");
		if (address < 16)
		Serial.print("0");
		Serial.println(address, HEX);
	}
	}
	if (nDevices == 0)
	Serial.println("No I2C devices found\n");
	else
	Serial.println("done\n");
}

// ================== Encoder
//===== 4096 to Degree or Rad
double AngleConvert(double input, String a){
	if (a == "degree" || a == "deg" || a == "d"){
		return input*(360.0/4096.0); // Convert to degree
	}
	else if (a == "radian" || a == "rad" || a == "r"){
		return input*(2*PI/4096.0); // Convert to radian
	}
	else return input;
}

//===== Magnetic Encoder
double ReadMagEnc(){
	AS5600 encoder; // Construct Encoder Object
	return encoder.getPosition();
}

//===== Individual Encoder
double ReadMux(uint8_t select, uint8_t muxaddr, String mode){
	Tcaselect(select, muxaddr);
	return  AngleConvert(ReadMagEnc(), mode);
}


//===== Quadrature Encoder
double ReadQuadEnc(int A, int B){
	// Encoder Enc(A,B);
	// return Enc.read();
	return 0;
}
