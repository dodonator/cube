def alphabet():
	result = []
	alph = range(65,92)
	for zahl in alph:
		result.append(chr(zahl))
	return result

AP = alphabet()

def cubeVigenereCodieren(x,y,z):
	xArray = list(x)
	yArray = list(y)
	zArray = list(z)
	result = ''
	for i in range(len(xArray)):
		tmpResult = AP.index(xArray[i]) + AP.index(yArray[i]) + AP.index(zArray[i])
		tmpResult = tmpResult % 26
		tmpResult = AP[tmpResult]
		result += tmpResult
	return result


x = raw_input('x: ')
y = raw_input('y: ')
z = raw_input('z: ')

print cubeVigenereCodieren(x,y,z)