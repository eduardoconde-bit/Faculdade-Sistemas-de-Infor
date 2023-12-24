package resolucaotela;

import java.awt.Dimension;
import java.awt.Toolkit;

/**
 *
 * @author luise
 */
public class ResolucaoTela {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Toolkit resolution = Toolkit.getDefaultToolkit();
        Dimension dimensao = resolution.getScreenSize();
    System.out.println("A resolução da tela é " + dimensao.width + " + " + dimensao.height);
    }
    
}
