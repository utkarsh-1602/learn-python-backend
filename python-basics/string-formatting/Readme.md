# String Formatting in python

- Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

- Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string.

### Basic Argument Specifiers
    %s - String (or any object with a string representation, like numbers)

    %d - Integers

    %f - Floating point numbers

    %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

    %x/%X - Integers in hex representation (lowercase/uppercase)

