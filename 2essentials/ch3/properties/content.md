>### Instance variables
>A property exists when and only when it is explicitly created and added to an object. This can be done during the object's initialization, performed by the constructor.
>Moreover, it can be done in any moment of the object's life. Furthermore, any existing property can be removed at any time.

>Such an approach has some important consequences:
> 1. different objects of the same class may possess different sets of properties;
> 2. there must be a way to safely check if a specific object owns the property you want to utilize (unless you want to provoke an exception - it's always worth considering)
> 3. each object carries its own set of properties - they don't interfere with one another in any way.
Such variables (properties) are called instance variables.

>### Class variables
>A class variable is a property which exists in just one copy and is stored outside any object.
> <br> **Note**: no instance variable exists if there is no object in the class; a class variable exists in one copy even if there are no objects in the class.