# Components

This page covers all the components currently supported by ALOC. Components represent a phrase in the target language. There are currently three components supported by ALOC.


## Simple Components
A simple component is a component used to represent simple phrases that are made up of attributes that the user can modify. A simple component may look like this:

```
[0] BABA is waiting for FOOD
```

## Chain Components
Chain components are similar to simple components but can be chained together like the name suggests. A chained component could look something like this:

```
[0] ONE IS ODD AND
[1] TWO IS EVEN AND
[2] THREE IS ODD
```
Each statement is ended with a `linking attribute`, except the last. The `linking attribute` does not need to be the same for every (or any) element in the chain.

## Conditional Components

Conditional Components are a type of composite component - they themselves contain other componenst. Conditional components consist of two Chain components, one `condition` and one `result`. A conditional component could look something like this:

```
IF
[0] BABA IS YOU
THEN
[1] FLAG IS WIN
```

Unlike the other two components, the conditional component does not have any attribute, but instead has two Chain components (which each have their own attributes that can be modified).

