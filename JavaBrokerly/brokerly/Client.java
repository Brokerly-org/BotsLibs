import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.function.Function;

class Message {
    JSONObject data;
    public Message(JSONObject jsonObject) {
        this.data = jsonObject;
    }

    public String getAttribute (String name) {
        return (String)this.data.get(name);
    }

    public void setItem(String key, String value) {
        this.data.put(key, value);
    }

    public String getItem(String key) {
        return  (String)this.data.get(key);
    }
}

class Bot {
    String token;
    String server_url;
    int handler;

    public Bot(String token,String host,  int port, int handler) {
        this.token = token;
        this.server_url = "http://" + host + ":" + String.valueOf(port);
        this.handler = handler;
    }

    private void getChatsMessages(JSONObject jsonObject) {
        JSONArray chats = (JSONArray) jsonObject.get("chats");
        for (Object chat : chats) {
            JSONObject chatObject = (JSONObject) chat;
            JSONArray messages = (JSONArray) chatObject.get("messages");
            for(Object message : messages) {
                System.out.println(message);
                Message newMessage = new Message((JSONObject)message);
                sendMessage(newMessage);
            }

        }

    }

    private void getUpdates() {
        try {
            String request_url = server_url + "/bot/pull?token=" + this.token;
            URL url = new URL(request_url);
            HttpURLConnection conn = (HttpURLConnection)url.openConnection();
            conn.setRequestMethod("GET");
            conn.connect();
            //int responsecode = conn.getResponseCode();
            String inline = "";
            Scanner sc = new Scanner(url.openStream());
            while(sc.hasNext())
            {
                inline += sc.nextLine();
            }
            sc.close();

            JSONParser parse = new JSONParser();
            JSONObject update = (JSONObject)parse.parse(inline);
            getChatsMessages(update);
        } catch (Exception e) {
            System.out.println("Error: Cannot connect to the server");
        }

    }

    public void sendMessage(Message message) {
        try {
            String request_url = server_url + "/bot/push";
            URL url = new URL(request_url);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Accept", "application/json");
            connection.setRequestMethod("POST");

            OutputStreamWriter wr = new OutputStreamWriter(connection.getOutputStream());
            JSONObject jsonObject = new JSONObject();
            jsonObject.put("chat_id", message.data.get("chat_id"));
            jsonObject.put("message", "hello");
            wr.write(jsonObject.toString());
            wr.flush();
            System.out.println(connection.getResponseCode());

        } catch (Exception e) {
            System.out.println("Error: Cannot connect to the server");
        }
    }

    public void start(int interval) {
        while (true) {
            getUpdates();
            try {
                Thread.sleep((long)interval * 1000);
            } catch(Exception exception) {
                System.out.println("Error: Sleep Error");
            }
        }
    }
}
