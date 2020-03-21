const int LED =13;                      //  set Led indicator  (pin nbr)
const int BTPWR=12;                     //  set  Power          (pin nbr)
String nameBt="Group 8 KTJ";            //  set Char " new Name & numbers of caracters of this new name [13] "
String pin="1234";                      // enter password for Bluetooth Device

void setup(){
  pinMode(LED, OUTPUT);                             // set LED Output                  
  pinMode(BTPWR, OUTPUT);                             // set LED Power Output 
  
  digitalWrite(LED, LOW);
  digitalWrite(BTPWR, HIGH);
  
  Serial.begin(9600);                             //  SET Baud Rate Speed 
  Serial.print("AT");                              //  SET Module to " Program Mode "
  delay(1000);
  Serial.print("AT+NAME");                          //  SET Module to " Program New Name "
  Serial.print(nameBt);                       //  SET "  New Name "
  Serial.print("\r\n");
  delay(1000);                     
  
  Serial.print("AT+BAUD:");                           //  SET Baud SPEED  "to Comm with Module "
  Serial.print("9600");                                //  SET Baud SPEED   (default at 9600)
  Serial.print("\r\n");
  delay(1000);

  Serial.print("AT+PIN");                                //  SET Module to " new Password "
  Serial.print("0007");                                   //  SET " Password "      default = ( 1234 )
  Serial.print("\r\n");
  delay(1000);
  digitalWrite(LED, HIGH);                                 
}
void loop(){
}
