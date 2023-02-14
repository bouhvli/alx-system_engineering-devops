this is the README file for the 0x03. Shell, init files, variables and expansions project
0. <o> -> alias ls='rm *' a script that creates an alias that has a name of 'ls' and a value of 'rm *'.
1. Hello you -> echo "hello $USER" a script that prints hello user, where user is the current Linux user.
2. The path to success is to take massive, determined action -> export PATH="$PATH:/action" this let /action be the last directory the shell looks into when looking for a program.
3. If the path be beautiful, let us not ask where it leads -> echo $PATH | tr -s ':' '\n' | wc -l a script that will print the number of directories in the path variable after translating all the ':' in the path into '\n' to make it accessable.
4. Global variables -> printenv a script that lists environment variables.
5. Local variables -> set  a script that lists all local variables and environment variables, and functions.
6. Local variable -> BEST="School" a script that creates a new local variable.
7. Global variable -> export BEST="School" a script that creates a new global variable.
8. Every addition to true knowledge is an addition to human power -> echo -e "$((128+$TRUEKNOWLEDGE))\n" a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
9. Divide and rule -> echo -e "$(($POWER/$DIVIDE))\n" a script that prints the result of POWER divided by DIVIDE, followed by a new line.
10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath -> echo -e "$(($BREATH**LOVE))\n" a script that displays the result of BREATH to the power LOVE.
11. There are 10 types of people in the world -- Those who understand binary, and those who don't -> echo $(( 2#$BINARY ))a script that converts a number from base 2 to base 10.
12. Combination -> echo {a..z}{a..z} |tr ' ' '\n' | grep -v "oo"  a script that prints all possible combinations of two letters, except oo.
13. Floats -> printf "%.2f \n" $NUM a script that prints a number with two decimal places, followed by a new line.
