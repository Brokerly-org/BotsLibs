#include <ArduinoWebsockets.h>
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <ArduinoJson.h>
#include <ESP8266HTTPClient.h>


const char* ssid = "ssid"; //Enter SSID
const char* password = "pass"; //Enter Password
const char* websockets_server = "wss://yakov.gq/bot_connect?token=3c7-5fn9izWUgXvyMLJO"; //server adress and port
const char* TOKEN = "3c7-5fn9izWUgXvyMLJO";
const char* host = "yakov.gq";
const int httpsPort = 443;

//WiFiClientSecure wifiClientSecure; // use WiFiClient for non https

//SHA1 finger print of certificate use web browser to view and copy
// Steps to get SHA finger print ehttps://circuits4you.com/2019/02/08/esp8266-nodemcu-https-secured-post-request/ 
//const char fingerprint[] PROGMEM = "10:7C:39:11:1A:D8:8D:E7:54:E5:9D:72:C1:54:38:84:4A:4F:99:24";
using namespace websockets;

WebsocketsClient client;


void onMessageCallback(WebsocketsMessage message) {
    Serial.print("Got Message: ");
    Serial.println(message.data());
    DynamicJsonDocument doc(1024);
    deserializeJson(doc, message.data());
    JsonArray jsonUpdate = doc.as<JsonArray>();
    for(JsonVariant u : jsonUpdate) {
      JsonObject newUpdate = u.as<JsonObject>();
      JsonArray messages = newUpdate["messages"].as<JsonArray>();
      for(JsonVariant m : messages) {
        Serial.println();
        Serial.print("New message from chatId: ");
        Serial.print(u["chat"].as<String>());
        Serial.print(" Message: ");
        Serial.println(m["content"].as<String>());
        String msg = "{\"message\":{\"text\":\"" + m["content"].as<String>() + "\"},\"chat_id\":\"" + u["chat"].as<String>() + "\"}";
        client.send(msg);
      }
    }
}




void onEventsCallback(WebsocketsEvent event, String data) {
    if(event == WebsocketsEvent::ConnectionOpened) {
        Serial.println("Connnection Opened");
    } else if(event == WebsocketsEvent::ConnectionClosed) {
        Serial.println("Connnection Closed");
    } else if(event == WebsocketsEvent::GotPing) {
        Serial.println("Got a Ping!");
    } else if(event == WebsocketsEvent::GotPong) {
        Serial.println("Got a Pong!");
    }
}


void setupWebsocket() {
    client = {}; // as advised in issue #75 
//    client = WebsocketsClient();
    client.onMessage(onMessageCallback);
    client.onEvent(onEventsCallback);
//    client.setInsecure(); // yes, lame
    Serial.println("Connecting to ws");
    client.connect(websockets_server);
}

void setup() {
    Serial.begin(115200);
    // Connect to wifi
    Serial.print("Connecting");
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("Connected to wifi!");

    // Wait some time to connect to wifi
    for(int i = 0; i < 10 && WiFi.status() != WL_CONNECTED; i++) {
        Serial.print(".");
        delay(1000);
    }
    setupWebsocket();
}

void loop() {
    if (client.available()) {
      client.poll();
    } else {
      Serial.println("not available...");
      delay(5000);
      setupWebsocket();
    }
}