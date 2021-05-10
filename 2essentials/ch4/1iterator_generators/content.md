>## Generator
>>A Python generator is a piece of specialized code able to produce a series of values, and to control the iteration process. <br>
>>A generator returns a series of values

>## Iterator
>>The iterator protocol is a way in which an object should behave to conform to the rules imposed by the context of the for and in statements. An object conforming to the iterator protocol is called an iterator.
>>An iterator must provide two methods:
>> 1. ```__iter__()``` which should return the object itself and which is invoked once (it's needed for Python to successfully start the iteration) <br>
>> 2. ```__next__()``` which is intended to return the next value (first, second, and so on) of the desired series - it will be invoked by the for/in statements in order to pass through the next iteration; if there are no more values to provide, the method should raise the StopIteration exception.

> ## yield statement

>>The main discomfort in iterator protocol is the need to save the state of the iteration between subsequent ```__iter__``` invocations.

>> ```yeild``` makes it easier. it provides the value of the expression specified after the yield keyword, just like return, but doesn't lose the state of the function.

>>All the variables' values are frozen, and wait for the next invocation, when the execution is resumed (not taken from scratch, like after return).

>>There is one important limitation: such a function should not be invoked explicitly as - in fact - it isn't a function anymore; it's a generator object.

>>The invocation will return the object's identifier, not the series we expect from the generator.