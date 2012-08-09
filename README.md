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

	from censor import Censor

    censor = Censor()
    censor.add_keyword('shit')
    text = 'hello you little shit'
    censored_text = censor.censor(text)
    
print censored_text

    'hello you little ****'

#### Isn't that trolololowesome ?!


### Please feel free to improve it if you like :)

![image](http://img193.imageshack.us/img193/5605/tumblrlznr805hcb1r3zat8.png)
