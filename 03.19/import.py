import funcs

funcs.func1()
funcs.func2()

del funcs

from funcs import func1

func1()
func2()
