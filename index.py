from appliances.kitchen import DishWasher
from appliances.laundry import Dryer
from appliances.laundry import Washer
from appliances.kitchen import Refrigerator
from appliances.kitchen import CoffeeMaker
from appliances.kitchen import CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "gas")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

can_opener = CanOpener("red")
can_opener.open_can()
