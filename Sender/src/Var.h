//========================== CONSTANTS

#define I2CMux 0x70
#define DebounceDelay 50
// Pins

// #define LJ1A 
// #define LJ1B
// #define LJ2A
// #define LJ2B 
// #define RJ1A
// #define RJ1B
// #define RJ2A
// #define RJ2B


//========================== VARIABLES
double encval[2][6] = {{0,0,0,0,0,0},{0,0,0,0,0,0}}; // 0 is left, 1 is right; 0->5 Starting from the Base
double encsign[2][6] = {{0,0,0,0,1,0},{0,0,0,0,0,0}}; // 1 is correct direction
double raw[2][6] = {{0,0,0,0,0,0},{0,0,0,0,0,0}};
double zero[2][6] = {{0,0,0,0,0,0},{0,0,0,0,0,0}};
const int buttonpin[4] = {4,5,18,19}; // LL LR RL RR
int button[4] = {0,0,0,0}; 
int lastbutton[4] = {0,0,0,0};
int state[4] = {0,0,0,0};
int toggle[4] = {0,0,0,0};
unsigned long lastdebouncetime[4] = {0,0,0,0};

