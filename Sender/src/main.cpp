#include <Functions.h>
#include <Var.h>
#include <stdlib.h>
#include <BluetoothSerial.h>

BluetoothSerial SerialBT;

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif


void setup(){
	Serial.begin(115200);
	SerialBT.begin("ESP32test"); // Name
	Serial.println("Started");
}

void loop(){
	for(int i = 0;i<4;i++){
		SerialBT.print(toggle[i]BTBT
		SerialBT.print(',');
	for(int i = 0;i<12;i++){
		SerialBT.print(encval[i/6][i%6]);
		if (i != 11) SerialBT.print(',');
	}
	SerialBT.println();
}
// void setup() {
// 	pinMode(buttonpin[0],INPUT_PULLUP);
// 	pinMode(buttonpin[1],INPUT_PULLUP);
// 	pinMode(buttonpin[2],INPUT_PULLUP);
// 	pinMode(buttonpin[3],INPUT_PULLUP);

// 	Serial.begin(115200);
// 	Serial.println("Hello");
// 	CheckI2CM(I2CMux);
// 	delay(1000);
// 	Serial.println("Start");
// }

// void loop() {

// 	// ===== Read Button with Debounce
// 	for (int i = 0; i<4;i++){
// 		button[i] = digitalRead(buttonpin[i]);
// 		if (button[i] != lastbutton[i])	lastdebouncetime[i] = millis();
// 		if ((millis() - lastdebouncetime[i]) > DebounceDelay){
// 			if (button[i] != state[i]){
// 				state[i] = button[i];
// 				if (state[i] == LOW) toggle[i] = !toggle[i];
// 				}
// 			}
// 		lastbutton[i] = button[i];
// 	}

// 	// ===== Read from MUX All
// 	// for(int i = 0;i<7;i++){
// 	// 	raw[i/4][i%4 + 2] = ReadMux(i,I2CMux,"");
// 	// 	delay(10);
// 	// }

// 	// ===== Read from MUX individual

// 	// raw[0][2] = ReadMux(0,I2CMux,"");
// 	raw[0][3] = ReadMux(1,I2CMux,"");
// 	raw[0][4] = ReadMux(2,I2CMux,"");
// 	raw[0][5] = ReadMux(3,I2CMux,"");
// 	// raw[1][2] = ReadMux(4,I2CMux,"");
// 	raw[1][3] = ReadMux(5,I2CMux,"");
// 	raw[1][4] = ReadMux(6,I2CMux,"");
// 	raw[1][5] = ReadMux(7,I2CMux,"");

// 	// ===== Read Quadrature Encoder
// 	// raw[0][0] = ReadQuadEnc(LJ1A,LJ1B);
// 	// raw[0][1] = map(ReadQuadEnc(LJ2A,LJ2B),0,2048,0,4096);
// 	// raw[1][0] = ReadQuadEnc(RJ1A,RJ1B);
// 	// raw[1][1] = map(ReadQuadEnc(RJ2A,RJ2B),0,2048,0,4096);

// 	// ===== Zero Configuration, First Button
// 	if (toggle[0] == 1){
// 		for(int i = 0;i<12;i++) zero[i/6][i%6] = raw[i/6][i%6];
// 	}

// 	// ===== Write to EncVal

// 	for(int i = 0;i<12;i++){
// 		static float a;
// 		a = (raw[i/6][i%6] - zero[i/6][i%6]);
// 		encval[i/6][i%6] = (a > 0) ? a : (a+4096);
// 		encval[i/6][i%6] = (encsign[i/6][i%6] == 1) ? encval[i/6][i%6] : (4096-encval[i/6][i%6]);
// 	}

// 	// ===== Communicate over Serial
// 	for(int i = 0;i<4;i++){
// 		Serial.print(toggle[i]);
// 		Serial.print(',');
// 	}
// 	for(int i = 0;i<12;i++){
// 		Serial.print(encval[i/6][i%6]);
// 		if (i != 11) Serial.print(',');
// 	}
// 	Serial.println();
// }