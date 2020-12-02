# Command Line Help Tool Api

This api is built to ease beginners' transition to the unix terminal. It is built with all get-requests (except for the /dev branch) for ease of access in the termal (via curl/wget).

- USAGE: curl http://url
- OUTPUT:
```
    'NAVIGATION PATHS:': {
        '.../all': 'display all hints',
        '.../search/<query>': 'search for hint or tag',
        '.../search-tag/<query>': 'search for tag',
        '.../search-hint/<query>': 'search for hint',
        '.../dev': 'modify the database',
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
