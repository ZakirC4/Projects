import javax.swing.*;
import java.awt.*;

public class MainWindow {

    public MainWindow() {
        this.setTitle("Text Editor");
        this.setPreferredSize(new Dimension(500, 400));
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);

        this.setVisible(true);
    }

    public static void main(String[] args) {
        MainWindow window = new MainWindow();
    }
}