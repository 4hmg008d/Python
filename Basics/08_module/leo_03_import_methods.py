import leo_01_test_module_1
import leo_02_test_module_2 as Test2
from leo_01_test_module_1 import Dog
from leo_02_test_module_2 import *
from leo_02_test_module_2 import say_hello as hello2

hello2()
say_hello()
leo_01_test_module_1.say_hello()
snoopy = Dog()
Test2.say_hello()
