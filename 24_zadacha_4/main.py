from child import Child
from parent import Parent

dad = Parent('Андрюха', 50, [Child(name='Коля', age=15), Child('Петя', 19), Child('Валера', 49)])

dad.have_grown()
print(dad.info())
print(dad.tell_about(1))
dad.feed_up(1)
print(dad.tell_about(1))
dad.calm_down(1)
print(dad.tell_about(1))
print(dad.tell_about(5))
