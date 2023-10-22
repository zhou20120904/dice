This is a simulator to simulate dice.

First,import my model.

```apache
from dicesim import Dice
```

To roll dice,using code here.

```apache
die=Dice(6)
die.roll()#returns a random number between 1 and 6
```

To show what number could you get,use `allSide()`.

```apache
die.allSide()#returns [1,2,3,4,5,6]
```

To count how many times each side is thrown when throwing the dice,use `count(times)`.

```apache
die.count(100)#returns example [11, 15, 10, 22, 14, 7]
```
