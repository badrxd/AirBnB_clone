
# AirBnB clone - ( The console ) 

The Airbnb clone's command interpreter is a Python project that offers a command-line interface. Through this interface, users can interact with the data models that form the foundation of the Airbnb clone application. The command interpreter enables users to execute a range of actions and operations on these data models, all from the convenience of the command line.

## Project Description:

first To start the Airbnb clone's console, follow these steps:

- Clone the project repository: git clone `https://github.com/****/AirBnB_clone` 
- got to the project directory: `cd AirBnB_clone`
- start the console: `./console`

## How To Use:

Within the command interpreter, you'll find an assortment of commands designed to facilitate data model manipulation, execute operations, and engage with the functionalities of the Airbnb clone. Below are a few illustrative commands and their respective applications:

### Creating a New Object:

you have the option to create one of the available objects by using the command create

```
(hbnb) create Amenity
9475dfb8-b0f3-4d9a-a5a5-cadb2aa2d0db
(hbnb) create City
a597d4cf-2734-4ba2-bf1c-2ac6e98f3b25
```
### To see the objects

```
(hbnb) all BaseModel
["[BaseModel] (85d4f494-8c7f-430e-916d-5cc6db5a45a8) {'id': '85d4f494-8c7f-430e-916d-5cc6db5a45a8', 'created_at': datetime.datetime(2023, 8, 14, 3, 47, 9, 29787), 'updated_at': datetime.datetime(2023, 8, 14, 3, 47, 9, 29791)}", 
"[BaseModel] (735d9503-60d9-4e78-904e-9b53ecb25b56) {'id': '735d9503-60d9-4e78-904e-9b53ecb25b56', 'created_at': datetime.datetime(2023, 8, 14, 3, 47, 10, 103035), 'updated_at': datetime.datetime(2023, 8, 14, 3, 47, 10, 103039)}", 
"[BaseModel] (00c47961-c58d-4e1e-b5c9-190a04a78257) {'id': '00c47961-c58d-4e1e-b5c9-190a04a78257', 'created_at': datetime.datetime(2023, 8, 14, 3, 47, 10, 533672), 'updated_at': datetime.datetime(2023, 8, 14, 3, 47, 10, 533676)}", "
[BaseModel] (34d98662-b102-4d01-92aa-f4b44865f9bd) {'id': '34d98662-b102-4d01-92aa-f4b44865f9bd', 'created_at': datetime.datetime(2023, 8, 14, 3, 47, 11, 239988), 'updated_at': datetime.datetime(2023, 8, 14, 3, 47, 11, 239992)}"]
```
you can see any object using this command too : `<class name>.all()`

### To Updating an Object

You have the capability to modify individual attributes of an object using the update command. Simply input the class name, object ID, attribute name, and desired attribute value to perform the update. This approach allows for precise and targeted changes to your objects' characteristics.

```
(hbnb) update City a597d4cf-2734-4ba2-bf1c-2ac6e98f3b25 name "El ksiba"
```
you can use other commands : `<class name>.update(<id>, <attribute name>, <attribute value>)` or `<class name>.update(<id>, <dictionary>)`

### To display Objects Details:

With the show command, quickly view an object's attributes by specifying its class name and ID.

```
(hbnb) show Place 9475dfb8-b0f3-4d9a-a5a5-cadb2aa2d0db
[Place] (9475dfb8-b0f3-4d9a-a5a5-cadb2aa2d0db) {'id': '9475dfb8-b0f3-4d9a-a5a5-cadb2aa2d0db', 'created_at': datetime.datetime(2023, 8, 14, 3, 45, 38, 716423), 'updated_at': datetime.datetime(2023, 8, 14, 3, 45, 38, 716431)}
```
you can use other commands : `<class name>.show(<id>):`

### To Delete an Object:

Easily remove an object by using the destroy command with the class name and object ID.

```
(hbnb) destroy Place 9475dfb8-b0f3-4d9a-a5a5-cadb2aa2d0db
```

you can use other commands : `<class name>.destroy(<id>)`

### To Counte instances of Class:

You can know the number of instances of a class by this command `<class name>.count()`

