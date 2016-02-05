class Scene(object):

	def enter(self):
		pass

class Engine(object):
	
	def __init__(self, scene_map):
		pass

	def play(self):
		pass

class Death(Scene):
r
	def enter(self):
		pass

class CentralCorridor(Scene):

	def enter(self):
		print "You wake up after being knocked out by an alien."
		print "directly in front of you is a tall alien with a hammer."
		print "He says 'Tell me a joke and you can pass'."
		print "tell him a joke? y or n."
		joke = raw_input()

		if joke == "y":
			print "You tell himna dirty joke"
			print "the goblin dies"
			#engine moves the player to next scene
		else:
			#engine moves player to death scene	

class LaserWeaponArmory(Scene):
	
	def enter(self):
		print "you enter the amroury and grab the bomb"
		#engine moves the player to the next scene

		
class TheBridge(Scene):
	
	def enter(Scene):
		print "you plant the bomb on the bridge"
		print " a goblin pulls out a gun and trys to shoot you"
		print "what do you do?"
		print "1. dodge."
		print "2. take it like a man."
		print "3. give up."
		print ">please enter 1-3."

		action = str(raw_input())

							
class EscapePod(Scene):

	def enter(Scene):
		pass

class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()					