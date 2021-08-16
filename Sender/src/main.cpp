#include <Functions.h>
#include <Var.h>
#include <stdlib.h>
#include <BluetoothSerial.h>
#include <ESP32Encoder.h>


ESP32Encoder CL0;
ESP32Encoder CR0;

BluetoothSerial SerialBT;
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif


// void setup(){
// 	Serial.begin(115200);

// }

// void loop(){
	
// 	for(int i = 0;i<4;i++){
// 		SerialBT.print(toggle[i]);
// 		SerialBT.print(',');
// 		toggle[i] = !toggle[i];
// 	}
// 	for(int i = 0;i<12;i++){
// 		SerialBT.print(encval[i/6][i%6]);
// 		if (i != 11) SerialBT.print(',');
// 		if (encval[0][5] > 360) encval[0][5] = 0;
// 		else if (encval[0][5] < 0) encval[0][5] = 0;
// 		else encval[0][5] = encval[0][5] + 1;
// 	}
// 	SerialBT.println();
// 	delay(10);
// }






void setup() {

	SerialBT.begin("ESP32test"); // Name
	Serial.println("Started");



	pinMode(buttonpin[0],INPUT_PULLUP);
	pinMode(buttonpin[1],INPUT_PULLUP);
	pinMode(buttonpin[2],INPUT_PULLUP);
	pinMode(buttonpin[3],INPUT_PULLUP);

	Serial.begin(115200);
	CheckI2CM(I2CMuxR);
	//CheckI2CM(I2CMuxL);
	
	ESP32Encoder::useInternalWeakPullResistors=UP;
	CL0.attachHalfQuad(32,33);
	CL0.clearCount();
	CR0.attachHalfQuad(34,35);
	CR0.clearCount();
}

void loop() {
	// ===== Read Button with Debounce
	for (int i = 0; i<4;i++){
		button[i] = digitalRead(buttonpin[i]);
		if (button[i] != lastbutton[i])	lastdebouncetime[i] = millis();
		if ((millis() - lastdebouncetime[i]) > DebounceDelay){
			if (button[i] != state[i]){
				state[i] = button[i];
				if (state[i] == LOW) toggle[i] = !toggle[i];
				}
			}
		lastbutton[i] = button[i];
	}

	// ===== Read from MUX All
	// for(int i = 0;i<7;i++){
	// 	raw[i/4][i%4 + 2] = ReadMux(i,I2CMux,"");
	// 	delay(10);
	// }

	// ===== Read from MUX individual

	// raw[0][5] = ReadMux(2,I2CMuxL,"");
	// raw[0][4] = ReadMux(3,I2CMuxL,"");
	// raw[0][3] = ReadMux(4,I2CMuxL,"");
	// raw[0][2] = ReadMux(5,I2CMuxL,"");
	// raw[0][1] = ReadMux(6,I2CMuxL,"");

	raw[1][5] = ReadMux(2,I2CMuxR,"");
	raw[1][4] = ReadMux(3,I2CMuxR,"");
	raw[1][3] = ReadMux(4,I2CMuxR,"");
	raw[1][2] = ReadMux(5,I2CMuxR,"");
	raw[1][1] = ReadMux(6,I2CMuxR,"");


	// ===== Read Quadrature Encoder
	raw[0][0] = CL0.getCount();
	raw[1][0] = CR0.getCount();

	// ===== Zero Configuration, First Button
	if (toggle[2] == 1){
		for(int i = 0;i<12;i++) zero[i/6][i%6] = raw[i/6][i%6];
	}

	// ===== Write to EncVal

	for(int i = 0;i<12;i++){
		static float a;
		a = (raw[i/6][i%6] - zero[i/6][i%6]);
		encval[i/6][i%6] = (a > 0) ? a : (a+4096);
		encval[i/6][i%6] = ((encsign[i/6][i%6] == 1) ? encval[i/6][i%6] : (4096-encval[i/6][i%6]));
	}

	// ===== Communicate over Serial
	for(int i = 0;i<4;i++){
		Serial.print(toggle[i]);
		SerialBT.print(toggle[i]);
		SerialBT.print(',');
		Serial.print('\t');
	}
	for(int i = 0;i<12;i++){
		Serial.print(encval[i/6][i%6]);
		SerialBT.print(encval[i/6][i%6]);
		if (i != 11) {
			Serial.print('\t');
			SerialBT.print(',');
		}
	}
	Serial.println();
	SerialBT.println();
}

