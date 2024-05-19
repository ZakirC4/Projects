import javax.swing.*;
import java.awt.*;

public class Main {


    public Main() {
        this.setTitle("");
        this.setPreferredSize(new Dimension(500, 400));
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);

        this.setVisible(true);
    }

    public static void main(String[] args) {
        Main window = new Main();
    }
}