#
from PIL import Image
import encode
import decode



dataEncoder = encode.encode()
dataDecoder = decode.decode()  	#decoder object


def main():
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n\n> "))
	if (a == 1):
		dataEncoder.encodeTextInImage()
		print("Your stegan is ready!!!!")

	elif (a == 2):
		hideData = dataDecoder.decodeTextFromImage()
		print("Decoded data : "+hideData)
	else:
		raise Exception("Enter correct input")






















# Driver Code
if __name__ == '__main__' :

	# Calling main function
	main()
