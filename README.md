# Airbnb :hotel:
An AirBnB Clone

## Description :memo:
This is a command interpreter which will be used to manage your Airbnb objects
## Using the console
To run the console in interactive mode, run the file `console.py`
```
$./console
```
The console will prompt for input:
```
$ ./console.py
(hbnb)
```
To quit the console, enter the command quit, an EOF signal(`ctrl-D`)
```
$ ./console.py
(hbnb) quit
$
```
```
$ ./console.py
(hbnb) EOF
$
```
## Console Commands
1. **create**
    - Usage: `create <class>`
Creates a new instance of `<class>`. saves it to `file.json` and prints the `id`.
```
$./console.py
$(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) quit
```
2. **show**
  - Usage: `show <class> id`
Prints the string representation of an instance based on the class name and id.
```
$./console.py
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```
3. **destroy**
  - Usage: `destroy <class> id`
Deletes an instance based on the class name and id and save the change into the `file.json`
```
$./console
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```
4. **update**
  Usage: `update <class> id`
Updates an instance based on the class name and id by adding or updating attribute saving the changes into `file.json`
```
./console
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```
5. **all**
  -Usage: `all`
Prints all string representation of all instances based or not on the class name.
```
$./console
(hbnb) all
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
```
## Authors :black_nib:
- Joseph Mariga
- Pius Mionki
