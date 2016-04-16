Steganography is the science of hiding information in plain sight.  As it applies
to cryptography, it is often used to describe information encoded into images,
network traffics, or video.  A less-than-clever internet celebrity encoded a
secret message in his screenfetch portrait. Your task is to recover the message
using the original and the modified image information.

The message hidden in the image will be ASCII characters, to which a simple
cipher has been applied.  You will also need to figure out what this cipher
offset is to uncover the actual message. (You'll know it when you see it)

Hint: begin by printing each file to the console to see what you're working
with. We have included a simple c file with which to do so.

Compile it by typing:
gcc dogePrint.c -o dogePrint

Use it by typing:
./dogePrint <filename>

Input:
Two text files, asciiDoge89x89.txt and secretDoge.txt

Output:
a simple text message with only lowercase alphabetic characters