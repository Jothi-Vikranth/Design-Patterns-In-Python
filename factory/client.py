"Factory Use Case Example Code"

from chair_factory import ChairFactory

# The Client
CHAIR = ChairFactory.get_chair("SmallChair")
if CHAIR is not None :
    print(CHAIR.get_dimensions())
else :
    print('Nothing to show')
    