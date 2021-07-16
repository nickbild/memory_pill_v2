#include <WiFi.h>
#include "secrets.h"

const int LID = 4;

WiFiClient client;

const char* host = "aws.amazon.com";
const char* url = "/record_open?key=";

String state = "closed";

void setup() {
  Serial.begin(115200);
  delay(10);
    
  pinMode(LID, INPUT);

  esp_sleep_enable_ext0_wakeup(GPIO_NUM_4, HIGH);

  // Connect to WiFi.
  WiFi.begin(SSID, PASSWORD);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Trigger this if an 'open' signal is received, and the
  // lid was not previously opened.
  if (digitalRead(LID) == HIGH && state != "open") {
    state = "open";

    Serial.println("Lid open.");
//    // Send signal to remote server.
//    if (!client.connect(host, 80)) {
//      Serial.println("Connection failed.");
//      return;
//    }
//
//    client.print(String("GET ") + url + BOTTLE_ID + " HTTP/1.1\r\n" +
//      "Host: " + host + "\r\n" +
//      "Connection: close\r\n\r\n");
//
//     while(client.available()) {}
//
//     client.stop();
  }
  // Lid is in place, so track that state.
  else if (digitalRead(LID) == LOW) {
    state = "closed";

    // Sleep.
    Serial.println("Lid on. Going to sleep.");
    WiFi.mode(WIFI_OFF);
    esp_deep_sleep_start();
    WiFi.mode(WIFI_STA);
    Serial.println("Awake.");
  }

  delay(250);
}
