from aiogram.dispatcher.filters.state import StatesGroup, State

# Form for Checker
class Forma(StatesGroup):
	exchange = State()
	action = State()
	bank = State()
	volume = State()