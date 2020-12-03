# Command Line Help Tool REST API

This API is built to ease beginners' transition to the unix terminal. It is built with all get-requests (except for the /dev branch) for ease of access in the termal (via curl/wget).

This project is not live, but if it were, just replace http://127.0.0.1:8001 with the hosted url!

- USAGE: When you find yourself not remembering a terminal command, or simply completely lost, just type:
```
curl http://127.0.0.1:8001
```
The output will show you how to use the api:
```json
{
    "NAVIGATION PATHS:": {
        ".../all": "display all hints",
        ".../search/<query>": "search for what you need to know",
        ".../dev": "modify the database"
    }
}
```

For example, if you want to know how to work with folders, simply search for it like so: curl http://127.0.0.1:8001/search/folder. That output would look something like this:
```json
{
    "4": {
        "name": "cd <directory name>",
        "description": "Type 'cd ~/Downloads' to change location to the Downloads folder. Alternatively, if you are already in the '~' folder, type 'cd Downloads' to achieve the same result. Type 'man cd' to view more options with this command.",
        "tags": "changedirectory, changedir, directory, changelocation, cd, relocate, location, changefolder"
    },
    "6": {
        "name": "mkdir <directory name>",
        "description": "Creates new directory/folder. Type 'mkdir projects' to create a new folder named projects. Type 'man mkdir' to view more options with this command.",
        "tags": "mkdir, makefolder, makedirectory, newfolder, newdirectory, createfolder, createdirectory"
    },
    "7": {
        "name": "rm <input>",
        "description": "Deletes a file. With the '-r' option, it will also delete a folder/directory like so: 'rm -r foldername'. Type 'man rm' to view more options with this command.",
        "tags": "mkdir, makefolder, makedirectory, newfolder, newdirectory, createfolder, createdirectory"
    },
    "8": {
        "name": "cp <input1> <input2>",
        "description": "Copies input1 to input2, if input2 does not exist, it will be created. The inputs can be files or directories (with the -r option). Type 'man cp' to view more options with this command.",
        "tags": "cp, copy, copyfile, copydirectory, copyfolder, duplicate"
    },
    "9": {
        "name": "mv <input1> <input2>",
        "description": "Renames or moves a file or directory. Type 'mv file1 file2' to rename file1 to file2. Type 'mv file1 ~/Downloads/file1' to change it's location to the Downloads folder. Type 'man mv' to view more options with this command.",
        "tags": "cp, copy, copyfile, copydirectory, copyfolder, duplicate"
    },
}
```
Note: queries should not contain spaces. To search for "more help", use "curl http://http://127.0.0.1:8001/search/morehelp". For better results, input shorter keywords, or search for individual words. For example, searching for "more help" won't return anything, however, "more" and "help" individually searched will.

Currently only supports Unix (Mac & Linux)

## Endpoints

### .../
GET req:
- displays all navigation paths/endpoints

### .../all
GET req:
- displays all hints with all information

### .../search/<query>
GET req:
- takes string <query> input and displays hints with maching names or tags

### .../search-tag/<query>
GET req:
- takes string <query> input and displays hints with matching tag

### .../search-hint/<query>
GET req:
- takes string <query> input and displays hints with matching name

### .../dev
GET req:
- displays all hints with all information

POST req:
- takes 'name', 'description', and optional 'tags' (in csv format) parameters
- creates a new hint

PUT req:
- takes 'id', optional 'name', optional 'description', and optional 'tags' (in csv format) parameters
- updates an existing hint

DELETE req:
- takes 'id' parameter
- deletes an existing hint

## Notes
- I am aware this is not the typical use case for APIs, however, I value creating something actually useful with my projects, regardless of size, and this was an idea that fit exactly that!
