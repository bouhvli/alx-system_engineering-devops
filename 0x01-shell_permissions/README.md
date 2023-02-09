the command is 'su betty': allow us to change to the user betty
the command is 'whoami': allow us to print the effective name of the current user 
the command is 'groups': allow us to print the names of the groups the current user in.
the command is 'sudo chown betty hello': allow us to change the ownership from currant user to the user betty.
the command is 'touch hello': allow us to create a new empty file.
the command is 'chmod u+x hello': allow us to add to the hello file the right to be executed by the disired user.
the command is 'chmod ug+x,o+r': allow us to change the permessions to de desired ones
the command is 'chmod a+x hello':allow us to change the permission for all the users at once.
the command is 'chmod 007 hello': allow us to take over the user and group permissios and give everyone all permissions.
the command is 'chmod 753 hello': allow us to change the mode to look like this -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello. 
the command is 'chmod --reference=olleh hello': allow us to copy the permissions but not the file. 
the command is 'chmod -R a+X .': allow us to adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
the command is 'mkdir -m 751 my_dir': allow us to create a directory called my_dir with permissions 751 in the working directory.
the command is 'chgrp school hello': allow us to change ownership to school. 
