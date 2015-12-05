class Minion:
	def __init__(self, attack, health):
		self.attack = attack
		self.health = health
	def isDead(self):
		return self.health <= 0

def calculate_boombot(minions):
	kill_perc = []
	for x in range(len(minions)):
		percentage = 1.0
		#hits 1
		m = minions[x]
		if m.health == 1:
			percentage /= len(minions)
		elif m.health == 2:
			percentage = percentage / len(minions) * 0.75
		elif m.health == 3:
			percentage = percentage / len(minions) * 0.5
		elif m.health == 4:
			percentage = percentage / len(minions) * 0.25
		else:
			percentage = 0.0
		kill_perc.append(percentage)
	return kill_perc

def consolidate_percentages(percentages):
	length = len(percentages)
	c_percentages = []
	for x in range(length):
		best = 0
		for y in range(length):
			if percentages[y][x] > best:
				best = percentages[y][x]
		c_percentages.append(best)
	return c_percentages

def recurse_boombot(minions, boombots_left):
	all_percentages = []
	for x in range(len(minions)):
		minions_copy = list(minions)
		current_minion = minions_copy[x]
		if current_minion.attack > 0:
			current_minion.health -= 1
			if current_minion.isDead():
				minions_copy.pop(x)
			percentage = calculate_boombot(minions_copy)
			if current_minion.isDead():
				percentage.insert(x, 1)
			current_minion.health += 1
			all_percentages.append(percentage)
		else:
			all_percentages.append([0.0] * len(minions))
	print all_percentages
	print consolidate_percentages(all_percentages)


def main():
	num_boombots = raw_input("How many boom bots? ")
	num_minions = raw_input("How many enemy minions? ")
	hero_health = raw_input("What is the enemy hero health? ")
	minions = [Minion(0, int(hero_health))]

	for x in range(int(num_minions)):
		attack = raw_input("Enter attack of minion "+str(x)+": ")
		health = raw_input("Enter health of minion "+str(x)+": ")
		minions.append(Minion(int(attack), int(health)))

	recurse_boombot(minions, num_boombots)

main()