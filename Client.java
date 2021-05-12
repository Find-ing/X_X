package Server_Client;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class Client{
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("127.0.0.1", 8388);
        OutputStream oup = socket.getOutputStream();
        oup.write("HELLO SERVER!".getBytes(StandardCharsets.UTF_8));
        InputStream inp = socket.getInputStream();
        System.out.println(inp.read());
        socket.close();
    }
}
