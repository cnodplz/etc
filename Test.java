import java.io.*;

public class Test {

    public static void main(String args[]) {
    // Interate SKY-JDEC-0000 to 9999
    String Str = new String("SKY-JDEC-");
	int x = 0000;

	while (x<10000) {
		if (x >= 0 && x < 10) {
			String Str2 = new String(Str + "000" + x);
    		if (Str2.hashCode() == 1954501578) {
				System.out.println("uhoh: " + Str2.hashCode() + " " + Str2);
			}
		}
		else if (x >= 10 && x < 100) {
			String Str2 = new String(Str + "00" + x);
    		if (Str2.hashCode() == 1954501578) {
				System.out.println("uhoh: " + Str2.hashCode() + " " + Str2);
			}
		}
		else if (x >= 100 && x < 1000) {
			String Str2 = new String(Str + "0" + x);
    		if (Str2.hashCode() == 1954501578) {
				System.out.println("uhoh: " + Str2.hashCode() + " " + Str2);
			}
		}
		else { 
			String Str2 = new String(Str + x);
    		if (Str2.hashCode() == 1954501578) {
				System.out.println("uhoh: " + Str2.hashCode() + " " + Str2);
			}
		}
		x++;
		}
	} 
}
