# Unix terminal commands

- __wc file.txt -w__ - counts words in a file.  
- __cat file.txt | wc -w__ - does the same but with _pipe_ syntax.  
- __\<__ - standart input  
- __\>__ - standart output  
- __cat \> input.txt__ -- writing to file (ctrl + d to stop writing).  
- __cat \< input.txt__ -- printing content of the file.  
- __ls -l /bin/abd/dgh 2\> error.txt__ -- writing error to a file. (0 - standart input, 1 - standart output, 2 - standart error).  
- __ls -l /bin/abd/dgh \> output.txt 2>&1__ -- errors and output to a file.  
- __grep Sam names.txt__ -- standart grep query.
- __grep -w Sam names.txt__ -- returns only exact matches.  
- __ls -la | grep word__ -- an example of the grep command with pipe.  


