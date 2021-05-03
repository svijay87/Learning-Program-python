from observer import Publisher, Subscriber

p = Publisher()

ram = Subscriber('Ram')
shyam = Subscriber('Shyam')
mohan = Subscriber('Mohan')

p.register(ram)
p.register(shyam)
p.register(mohan)

p.dispatch("Hello! How are you doing?")
p.dispatch("Stay safe and take care of your health")