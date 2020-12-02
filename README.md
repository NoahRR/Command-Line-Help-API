# Command Line Help Tool REST API

This API is built to ease beginners' transition to the unix terminal. It is built with all get-requests (except for the /dev branch) for ease of access in the termal (via curl/wget).

- USAGE: When you find yourself not remembering a terminal command, or simply completely lost, just type:
```
curl http://http://127.0.0.1:8001
```
The output will show you how to use the api. For example, if you forget the command to change directory, simply search for it like so: curl http://127.0.0.1:8001/search/changedirectory. That output would look something like this:
```
{
    "5": {
        "name": "cd",
        "description": "Change directory. Directory = Folder. This is how you navigate through your files in the terminal.",
        "tags": "changedir, changedirectory, changelocation, movelocation"
    }
}
```

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
