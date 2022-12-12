from Mouse import Mouse
from Keyboard import Keyboard
from Display import Display
from Computer import Computer
from Order import Order


Mouse1  = Mouse('PS/2', 'MagnumTech')
Keyboard1 = Keyboard('PS/2', 'MagnumTech')
Display1 = Display('PHILIPS', '1024 x 1050')
Computer1 = Computer('GABRIEL', Mouse1, Keyboard1, Display1)

Mouse2  = Mouse('USB 2.0', 'Genius')
Keyboard2 = Keyboard('USB 2.0', 'Logitech')
Display2 = Display('PHILIPS', '2024 x 2050')
Computer2 = Computer('Leandro', Mouse2, Keyboard2, Display2)

Mouse3  = Mouse('USB 3.0', 'MagnumTech')
Keyboard3 = Keyboard('USB 3.0', 'hIPERx')
Display3 = Display('LG', '3024 x 3050')
Computer3 = Computer('Juana', Mouse3, Keyboard3, Display3)

Mouse4  = Mouse('Bluetooh', 'LogitechRS')
Keyboard4 = Keyboard('Bluetooh', 'Logitech')
Display4 = Display('Samsung', '4044 x 4050')
Computer4 = Computer('Jose', Mouse4, Keyboard4, Display4)

Computers = [Computer1, Computer2, Computer3, Computer4]
Order1 = Order(Computers)

print(Order1)