# delta time for each loop in milliseconds
DELTA_TIME = 16.0

# screen size
SCREEN_WIDTH = int(1280 * 0.8)
SCREEN_HEIGHT = int(768 * 0.8)

# time between spawns in milliseconds
SPAWN_DURATION = 500

# max slime allowed
MAX_SPAWN = 5

# time before disappearing
SPAWN_TIME = 3000

# speed
SPEEDS = [2, 3, 4, 5, 6]

# spawn positions from top left
SPAWN_POSITIONS = [(163, 259), (294, 290), (196, 241), (558, 220), (670, 216), (952, 315),
                   (1030, 281), (1086, 365), (328, 518), (433, 461), (569, 532), (144, 655),
                   (307, 683), (880, 577), (926, 581), (1088, 588)]
SPAWN_POSITIONS = list(map(lambda x: (int(0.8*x[0]), int(0.8*x[1])), SPAWN_POSITIONS))
