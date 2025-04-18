#simulation for time to fit the model of human

from Models.Common.Human import Human
from Models.Common.Nutrition import Nutrition

diabetic1 = Human("Juan", 2, 3)
nt = Nutrition(90,15,15)

print(diabetic1)