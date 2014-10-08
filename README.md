##Censor
*Missing, high-performance **censor** for Python & Humans*

Use this component if you want to censor **any** text in a **fast & intuitive** ( **very** ) way.

It supports both **keywords** and **patterns** (regex)

###Overview

Imagine you have this text:
	
	hello you little shit    
	
And all you want to do is just censor it.

###You can do it now!!

all you have to do is:

```python
	from censor import Censor

    censor = Censor()
    censor.add_keyword('shit')
    
    print censor.censor('hello you little shit')

    'hello you little ****'
```

#### Isn't that trolololowesome ?!


##### Please feel free to improve it if you like :)
