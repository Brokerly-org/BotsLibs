import org.json.simple.JSONObject;

interface VoidFunction {
    void handler(Bot bot, JSONObject message);
}

public class EchoBot {

    public static void main(String[] args) {
        VoidFunction handler = (bot, message) -> {
            String chat_id = (String)message.get("chat_id");
            String text = (String)message.get("content");
            System.out.println("New message from chat " + chat_id + ". The Message: " + text);
            bot.sendMessage(chat_id, text);
        };
       Bot bot = new Bot("nblNTu1zMWTQrte0p5KJ", "127.0.0.1", 6700, handler);
       bot.start(1);

    }
}