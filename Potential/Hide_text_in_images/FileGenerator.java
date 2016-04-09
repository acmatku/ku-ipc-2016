import java.io.*;
import java.util.*;

public class FileGenerator {

	public static void main(String[] args) throws IOException {
		
		//FileWriter writer = new FileWriter("input1.txt");
		String text = "01010100011010000110100101110011001000000110100101110011001000000110000100100000011101000110010101110011011101000010000001100110011010010110110001100101";
		String txt =  "01010100011001010111001101110100";
		Random generator = new Random();
		
		
		for(int i = 0; i < 45; i++) {
			if(i== 44) {
				System.out.printf("%02d%01d ", generator.nextInt(25), generator.nextInt(8)+1);
			}
			else {
			System.out.printf("%03d ", generator.nextInt(255));
			}
		}
		
		for(int i = 0; i < text.length(); i++) {
			System.out.printf("%02d%c ", generator.nextInt(25), text.charAt(i));
		}
	
		for(int i = 0; i < text.length()%3-1; i++) {
			System.out.printf("%03d ", generator.nextInt(255));
		}
		
		
		
	}

}
