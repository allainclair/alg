# Problem

Create a function that determines whether each seat can "see" the front-stage.
A number can "see" the front-stage if it is strictly greater than the number
before it. Let's go the the examples. 

# Examples

## # 1


```
FRONT STAGE
1 2 3 2 1 1
2 4 4 3 2 2
5 5 5 5 4 4
6 6 7 6 5 5
```

If we analyse bottom up (starting from left), 6 > 5 > 2 > 1,
6 > 5 > 4 > 2, ..., so all numbers can "see".

## # 2

Not everyone can see the front-stage in the example below:

```
FRONT STAGE
1 2 3 2 1 1
2 4 4 3 2 2
5 5 5 9 4 4
6 6 7 6 5 5
```

The `9 (i=2, j=3)` is directly in front of the `6 (i=3, j=3)` and blocking its view.

The function should return `True` if every number can see the front-stage, and `False` if even a single number cannot.

# Design

Unfinished

# Draft 


# More examples

```
FRONT STAGE
   1 2 3
   4 5 6
   7 8 9
   True
```


```
FRONT STAGE
   0 0 0
   1 1 1
   2 2 2
   True
```

```
FRONT STAGE
   2 0 0
   1 1 1
   2 2 2
   False
```

```
FRONT STAGE
  1 0 0
  1 1 1
  2 2 2
  False
```

Number must be strictly smaller than the number directly behind it.

# Rerefences

Problem source: https://edabit.com/challenge/xbjDMxzpFcsAWKp97
