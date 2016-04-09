import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.io.*;
public class Solver {
	
	enum States{W,Z,O,I};
	
	public static void main(String[] args) throws IOException {
		
		Path filePath = Paths.get("input1.txt");
		Scanner reader = new Scanner(filePath);
		String message = "";
		String message2 = "";
		States state;
		state = States.W;
		int test = 0;

		while(reader.hasNext()) {
			test++;
			if(reader.hasNextInt()) {
				String value = String.valueOf(reader.nextInt());
				value = value.substring(value.length()-1);
				
				switch(state) {
				case W:	if(value.startsWith("0")) {
						state = States.Z;
						message = message + value;
					}
					break;
					
				case Z:	if(value.startsWith("1")) {
						state = States.O;
						message = message + value;
					}
					else {state = States.W;
							message = "";}
					break;
					
				case O:	if(value.startsWith("1") || value.startsWith("0")) {
						message = message + value;
						state = States.I;
					}
					else {state = States.W;
							message = "";}
					break;
					
				case I:	if(!(value.startsWith("1")|| value.startsWith("0"))) {
						state = States.W;
						
					}
					else {
						message = message + value;
						if(message.length()== 8) {
							message2 += (char)Integer.parseInt(message,2);
							message = "";
						}
					}
					break;
					
				}
				
			}
			else {reader.next();}
		}
		System.out.println(message2);
		System.out.println(test);
		
		

	}

}
