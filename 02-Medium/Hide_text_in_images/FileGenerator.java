import java.io.*;
import java.util.*;

public class FileGenerator {

	public static void main(String[] args) throws IOException {

		//FileWriter writer = new FileWriter("input1.txt");

		//Stores the message string in binary
		String text = "01010100011010000110100101110011001000000110100101110011001000000110000100100000011101000110010101110011011101000010000001100110011010010110110001100101";
		Random generator = new Random();

		//Prints the padding of RGB values before those with the encoded message. Could be set to create any random number of values, even 0
		//The number of values should be divisible by 3 to maintain the illusion of RGB values.
		//Currently prints a value with a non-0 last digit before the message starts.
		for(int i = 0; i < 45; i++) {
			if(i== 44) {
				System.out.printf("%02d%01d ", generator.nextInt(25), generator.nextInt(8)+1);
			}
			else {
			System.out.printf("%03d ", generator.nextInt(255));
			}
		}

		//Prints values with the last digit being a digit from the binary message
		for(int i = 0; i < text.length(); i++) {
			System.out.printf("%02d%c ", generator.nextInt(25), text.charAt(i));
		}

		//Pads out the end values to make sure the total number of values is divisible by 3.
		//Can be changed to a random value, as long as it makes the total number f
		for(int i = 0; i < text.length()%3-1; i++) {
			System.out.printf("%03d ", generator.nextInt(255));
		}



	}

}
