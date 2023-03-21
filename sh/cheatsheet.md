# Command Line Cheatsheet

## (Arguably) The most useful command

```sh
# Display manual page for a given command
man {command}
```

## Quitting programs

If you're running a program that running longer than you need it to, you can send it a signal to exit using **CTRL-C**.

Sometimes this doesn't work and you have to go with the nuclear option, you can look for the process ID (all running processes on a Unix-based OS have a process ID number), and run `kill -9 {PID}`. This should be pretty rare though.

## Directories

```sh
# List files in directory
ls

# Useful flags
-l | Show "long format," which displays more details about each file
-a | Show "hidden" files that start with a "."
-G | Colors!
-h | With the -l flag, this shows more human-readable file sizes

# You can string all of the flags together like:
la -laGh

# Change directory
cd {directory}

# You can go up a directory by using "..":
cd ..

# Create a directory
mkdir {directoryName}

# Useful flags
-p | Create intermediate directories within a path if they don't already exist

# This can also be a path to a directory like:
mkdir outer/inner

# You can also use ".." to reference above directories. For example, if you need to create a directory two levels up:
mkdir ../../{directory}
```

## Files

```sh
# Create a file if it doesn't exist and update its last updated time. This doesn't sound useful but it can come in handy.
touch {file}

# Read a file
cat {file}

# Technically cat is used to conCATenate multiple files together, so you can use this to combine files. In Unix-style shell scripting, you can do handy things like direct the output of one command into a file, or even pipe them into other commands. For example, this copies the contents of two files into one:
cat {file1} {file2} > {newFile}

# You can also use `less` and `more` to read files interactively page-by-page. You can check the `man` page or check online for key controls. Just in case you use it and get stuck, press "q" to quit.
```

