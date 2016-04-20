Read from stdin a integer n followed by n+1 additional lines of input. The following n lines is a collection of key value pairs for the dictionary, the word to replace and the word to replace with. The last, n+1 line, is the text to do replacing in. This text will have no punctuation. 

Write to stdout the text with the words replaced by their dictionary counterparts.

Example input:
```
3
building complex
problem complex
obtuse complex
I told my psychologist I have a deep fear of complicated structures and they told me I had a obtuse building problem
```

Example output:
```
I told my psychologist I have a deep fear of complicated structures and they told me I had a complex complex complex
```
