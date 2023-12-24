package questao4;

import java.io.Reader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

// 
// Decompiled by Procyon v0.5.36
// 

public class Keyboard
{
    private static boolean printErrors;
    private static int errorCount;
    private static String current_token;
    private static StringTokenizer reader;
    private static BufferedReader in;
    
    static {
        Keyboard.printErrors = true;
        Keyboard.errorCount = 0;
        Keyboard.current_token = null;
        Keyboard.in = new BufferedReader(new InputStreamReader(System.in));
    }
    
    public static int getErrorCount() {
        return Keyboard.errorCount;
    }
    
    public static void resetErrorCount(final int count) {
        Keyboard.errorCount = 0;
    }
    
    public static boolean getPrintErrors() {
        return Keyboard.printErrors;
    }
    
    public static void setPrintErrors(final boolean flag) {
        Keyboard.printErrors = flag;
    }
    
    private static void error(final String str) {
        ++Keyboard.errorCount;
        if (Keyboard.printErrors) {
            System.out.println(str);
        }
    }
    
    private static String getNextToken() {
        return getNextToken(true);
    }
    
    private static String getNextToken(final boolean skip) {
        String token;
        if (Keyboard.current_token == null) {
            token = getNextInputToken(skip);
        }
        else {
            token = Keyboard.current_token;
            Keyboard.current_token = null;
        }
        return token;
    }
    
    private static String getNextInputToken(final boolean skip) {
        final String delimiters = " \t\n\r\f";
        String token = null;
        try {
            if (Keyboard.reader == null) {
                Keyboard.reader = new StringTokenizer(Keyboard.in.readLine(), " \t\n\r\f", true);
            }
            while (true) {
                if (token != null) {
                    if (" \t\n\r\f".indexOf(token) < 0) {
                        break;
                    }
                    if (!skip) {
                        break;
                    }
                }
                while (!Keyboard.reader.hasMoreTokens()) {
                    Keyboard.reader = new StringTokenizer(Keyboard.in.readLine(), " \t\n\r\f", true);
                }
                token = Keyboard.reader.nextToken();
            }
        }
        catch (Exception exception) {
            token = null;
        }
        return token;
    }
    
    public static boolean endOfLine() {
        return !Keyboard.reader.hasMoreTokens();
    }
    
    public static String readString() {
        String str;
        try {
            str = getNextToken(false);
            while (!endOfLine()) {
                str = String.valueOf(str) + getNextToken(false);
            }
        }
        catch (Exception exception) {
            error("Error reading String data, null value returned.");
            str = null;
        }
        return str;
    }
    
    public static String readWord() {
        String token;
        try {
            token = getNextToken();
        }
        catch (Exception exception) {
            error("Error reading String data, null value returned.");
            token = null;
        }
        return token;
    }
    
    public static boolean readBoolean() {
        final String token = getNextToken();
        boolean bool;
        try {
            if (token.toLowerCase().equals("true")) {
                bool = true;
            }
            else if (token.toLowerCase().equals("false")) {
                bool = false;
            }
            else {
                error("Error reading boolean data, false value returned.");
                bool = false;
            }
        }
        catch (Exception exception) {
            error("Error reading boolean data, false value returned.");
            bool = false;
        }
        return bool;
    }
    
    public static char readChar() {
        final String token = getNextToken(false);
        char value;
        try {
            if (token.length() > 1) {
                Keyboard.current_token = token.substring(1, token.length());
            }
            else {
                Keyboard.current_token = null;
            }
            value = token.charAt(0);
        }
        catch (Exception exception) {
            error("Error reading char data, MIN_VALUE value returned.");
            value = '\0';
        }
        return value;
    }
    
    public static int readInt() {
        final String token = getNextToken();
        int value;
        try {
            value = Integer.parseInt(token);
        }
        catch (Exception exception) {
            error("Error reading int data, MIN_VALUE value returned.");
            value = Integer.MIN_VALUE;
        }
        return value;
    }
    
    public static long readLong() {
        final String token = getNextToken();
        long value;
        try {
            value = Long.parseLong(token);
        }
        catch (Exception exception) {
            error("Error reading long data, MIN_VALUE value returned.");
            value = Long.MIN_VALUE;
        }
        return value;
    }
    
    public static float readFloat() {
        final String token = getNextToken();
        float value;
        try {
            value = new Float(token);
        }
        catch (Exception exception) {
            error("Error reading float data, NaN value returned.");
            value = Float.NaN;
        }
        return value;
    }
    
    public static double readDouble() {
        final String token = getNextToken();
        double value;
        try {
            value = new Double(token);
        }
        catch (Exception exception) {
            error("Error reading double data, NaN value returned.");
            value = Double.NaN;
        }
        return value;
    }
}
