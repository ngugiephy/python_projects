import argparse

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("num", type=int)

	args = parser.parse_args()

	# result = fib(args.num)
	print("The no is : " + str(args.num) )

if __name__ == "__main__":
	Main()