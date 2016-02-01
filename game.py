from sys import exit

room_discrip = "From what you can see, it looks like your in a hospital room. You see a large door, you also notice a notebook on a desk."

def start():

	print "You wake up in a dimly lit room. You notice your lying down on a table straped down."
	print "What do you do?" 
	print "1. Try to struggle free."
	print "2. Look around at your surroundings."
	print "3. Scream for help."
	
	choice = raw_input("> ")

	
	if choice == "1":
		print "You start wriggling your arms and legs in a attempt to free yourself, you realise that the table your laying on has wheels."
		print "What do you do?"
		print "1. Try to tip over the table."
		print "2. Nothing."

		choice2 = raw_input("> ")

		if choice2 == "1":
			print "Your able to plant your foot on something firm push yourself and the cart against a wall. The cart crashes against the wall and flips over."
			print "the sideing of the table snaps off freeing your right arm."
			print "You manage to free your limbs and you stand up."

			Dim_room()

		else:
			start()

	elif choice == "2":
		print room_discrip
		surround = false


	elif choice == "3":
		print "You scream for help."
		print "Suddenly you a monstrous sound echo out side the door."
		print "Thunderous steps approach the door"
		print "The steps stop right in front of the door"
		print "What do you do?"
		print "1. Hello?"
		print "2. Stay quiet."	

		choice2 = raw_input("< ")

		if choice2 == "1":
			print "You calmly say \"Hello?\""
			print "You hear nothing but dead silence."
			start()
			
		elif choice2 == "2":
			print "After a few moments, the monstrous steps continue walking past the door."
			start()

		else:
			start()	
start()			