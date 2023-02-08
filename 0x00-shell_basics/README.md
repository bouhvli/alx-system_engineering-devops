pwd command prints the absolute path name of the current working directory.
ls command Display the contents list of your current directory
cd ../../home by typing .. we are saying you have to go back to the parent directory
ls -l will list current directory contents in a long format because we used a wildcard '-l' .
ls -la Display current directory contents, including hidden files (starting with .). Use the long format.
ls -la -n cammand does the tric '-la' -> display the hidden files (starting with .). the '-n' -> will make the user and group IDs displayed numerically.
mkdir ~/../tmp/my_first_directory -> command Create a script that creates a directory named my_first_directory in the /tmp/ directory.
the command 'mv ~/../tmp/betty ~/../tmp/my_first_directory/' moves the betty file from directory tmp to tmp/my_first_directory.
 the 'rm' command is used to delete files.
rm -r ~/../tmp/my_first_directory -> Delete the directory my_first_directory that is in the /tmp directory.
 cd - command ->  changes the working directory to the previous one. 
  ls -la ~/../boot .. ../0x00-shell_basics/ command -> lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
type ~/../tmp/iamafile command -> prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
 ln -s ~/../bin/ls __ls__ -> Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
