import time

def delay_decorator(function):
	def wrapper_funciton():
		time.sleep(2)
		#Do something before fucntion / run it twice
		# function()
		function()
		#Do something after
	return wrapper_funciton()

@delay_decorator
def say_hello():
	print("Hello")

def say_bye():
	print("Bye!")

def say_greetings():
	print("How are you?")

