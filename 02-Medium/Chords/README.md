Chord Problem

Many popular songs follow a set chord progression, composed of chords with their root notes 1-5 steps removed from the Key chord.  Each step is assigned a letter, which provides a simple way to play a song in a different key, and still retain the structure of the original.  For example, in the key of C, the notes and their steps are as follows:

Chord      I     II     III     IV     V     VI
Root Note  C     Dm     Em      F      G     Am

Jazz and blues musicians don't like to be fenced in, and often switch keys on a whim.  Typically, such a transistion is called a "blue note" (or chord).  You're playing a show with your sweet future-funk band, and your sax player lays down a solo so smooth that you lose track of the key.  All you can remember is what key you were in, the last chord you played, and the two chords he just played, which are apparently in a different key.

Your task is to take in a key, a chord progression, and the last three chords played, and output the root notes  of the progression in the new key.  The first chord represents the last chord played of the current key, and the second and third are the next two steps of the progression, but in the new key.

You will only be given the Major keys A-G.
The progressions will include only I,II,III,IV,and V chords.
For Python-friendly programming, all sharps will be represented as flats (F# becomes Gb)

Example Input:
C
I IV V IV
G C G

Example Output
G C D C
