const int row[8] = {9, 4, A4, 6, 10, A3, 11, A1};
const int col[8] = {5, 12, 13, 8, A2, 7, 3, 2};

unsigned long time = 0;
unsigned int dt;
unsigned int frametimer = 0;
int frame = 0;

void setup() {
  // put your setup code here, to run once:
  for (int i=0; i <= 7; i++) {
    pinMode(row[i], OUTPUT);
    pinMode(col[i], OUTPUT);
  }
}

void loop() {
  dt = millis() - time;
  time = millis();

  frametimer += dt;

  if (frametimer >= ms_per_frame) {
    frametimer -= ms_per_frame;
    frame += 1;

    if (frame >= frames) {
      frame = 0;
    }
  }

  drawScreen(frame);


}

void drawPoint(int x, int y) {
  digitalWrite(row[x], HIGH);
  digitalWrite(col[y], LOW);
  delay(3);
  digitalWrite(row[x], LOW);
  digitalWrite(col[y], HIGH);
}

void drawRow(int rownum, byte b) {
  for (int i=0; i <= 7; i++) {
    digitalWrite(col[i], (~b >> i) & 0x01);
  }

  digitalWrite(row[rownum], HIGH);
  delay(3);
  digitalWrite(row[rownum], LOW);
}

void drawScreen(int frame) {
  for (int i=0; i <= 7; i++) { 
    byte rowbyte = pgm_read_byte( &(videodata[frame][i]) );

    drawRow(i, rowbyte);
  }
}
