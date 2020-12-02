# Command Line Help Tool Api

Currently only supports Unix (Mac & Linux)

## Endpoints

### .../
GET req:
- displays all navigation paths/endpoints

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
