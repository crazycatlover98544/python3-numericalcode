# python3-numericalcode
This is a simple (and not practical) project that takes a string and encodes it into a number.
## Warnings
THIS PROGRAM HAS NOT BEEN FULLY TESTED WITH MANY STRINGS. AS THUS, SOME CODES MAY NOT WORK. IF YOU FIND SOMETHING THAT DOES NOT WORK, YOU MAY REPORT IT IN THE ISSUES PAGE OF THIS REPOSITORY.
THE GENERATED STRINGS MAY NOT BE FULLY SECURE. I DO NOT KNOW; I AM NOT AN ENCRYPTION EXPERT.
## How to use
To encode a string, run `code_generator.py --encode`, then enter the string.
To decode a string, run `code_generator.py --decode`, then enter the encoded number.

Here are all the arguments and what they do:
|Argument|Function|
|---|---|
|-e,--encode|Encode a string|
|-d,--decode|Decode a string|
|-h,--help|Show the help menu and exit|

Sometimes, due to the string's length, it will fail, as the number generated is too large and causes an `OverflowError`.
## How this works
### Encoding
This program starts out by doing a Caesar cipher by -7. After that, it converts the text from the Caesar cipher to ASCII, and formats it as a number, but binary (eg. instead of being what 0b10101010 is, it is 10101010). After this, it puts all the binary numbers together, adding other numbers as formatting markers (eg. if 10101010 was the first character, and 01010101 the second, then it would be formatted as 241010101040101010143). Finally, it multiplies it by a value (it chooses different values if one does not work; there is a list stored in the program), and prints it to the output.
### Decoding
This program does the same thing as encoding, but in reverse, so it divides by a value (choosing different ones like the encoder to get the one the code uses), then splits the binary, then converts it to a string, then Caesar ciphers it by 7 (7 to cancel out the -7 from before).
## Using this as a Python module
If you do want to use this as a Python module, there are two main functions:
### encode(string)
Encode the number provided using the same method as what running `code_generator.py -e` does.
Returns a list, with the following format:
`[status,numb]`
_status_ is whether it succeeded or not. If it is `True`, then it successfully worked, and _numb_ should be the output number, as an integer. If it is `False`, then it did not work, and _numb_ will be 0.
### decode(number)
Encode the string provided using the same method as what running `code_generator.py -d` does.
Returns a list, with the following format:
`[status,string]`
_status_ is whether it succeeded or not. If it is `True`, then it successfully worked, and _string_ should be the output string. If it is `False`, then it did not work, and _string_ will be `''`.
## Extra information
`ascii_json.py` is a helper module. Inside the python file, there are two python dictionaries: `translation` and `numbertext` (Yes, I know, better names exist). `translation` lets you take a character, and get it's ASCII equivalent, as a Python integer (yes, in the code, it is hexadecimal, but Python converts it to a decimal automatically). For instance, `translation.get('a')` would get 97, as that is the ASCII equivalent. `numbertext` lets you provide a base-10 number as a string, and get the character corresponding to the number provided. For instance, `numbertext.get('97')` would get "a", as that is what 97 corresponds to. Without `ascii_json.py`, `code_generator.py` will error out, as it is a required dependency. `ascii_json.py` helps to make `code_generator.py`'s code neater, as I do not have to include two large Python dictonaries in it.
