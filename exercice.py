#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	Puissance = (voltage**2)/resistance
	return Puissance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	# v1[0] Pour accéder au X
	# v1[1] Pour accéder au Y
	rép = v1[0] * v2[0] + v1[1] * v2[1]
	return rép == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	sum = num_elems = 0
	for v in values:
		if v >= 0:
			sum += v
			num_elems += 1
	average_sum = sum/ num_elems
	return average_sum # La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	while value != 0:
		if value >= 20:
			twenties = value//20
			value = value - twenties*20
		elif value >= 10:
			tens = value//10
			value = value - tens*10
		elif value >= 5:
			fives = value // 5
			value = value - fives*5
		elif value >= 1:
			ones = value
			value = 0 

	return (twenties, tens, fives, ones);

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
