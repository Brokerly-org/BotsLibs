import org.json.simple.JSONObject;

public class EchoBot {

    void handler(JSONObject update) {
        String chat_id = (String)update.get("chat_id");
    }

    public static void main(String[] args) {
       Bot bot = new Bot("nblNTu1zMWTQrte0p5KJ", "127.0.0.1", 6700, 4);
       bot.start(1);

    }
}