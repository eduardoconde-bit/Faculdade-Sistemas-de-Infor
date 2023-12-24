package idiomasistema;

import java.util.Locale;

/**
 *
 * @author luise
 */
public class IdiomaSistema {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Locale local = Locale.getDefault();
        System.out.println("Seu sistema está em " + local.getDisplayLanguage());
    }
    
}
