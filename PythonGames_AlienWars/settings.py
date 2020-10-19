
class Settings():
	"""存储《外星人入侵》的所有设置的类"""
	
	def __init__(self):
		"""初始化游戏的设置"""
		
		#	屏幕设置
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = 230,230,230
		
		#	以什么样的速度加快游戏的节奏
		self.speed_up_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()
		
		#	子弹设置
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 50
		
		#	飞船设置
		self.ship_limit = 3
		
	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		#	飞船移动速度
		self.ship_speed_factor = 5
		#	子弹移动速度
		self.bullet_speed_factor = 10
		#	外星人移动速度
		self.alien_speed_factor = 1
		
		#	外星人下移速度
		self.fleet_drop_speed = 10
		
		#	fleet_direction为1表示向右移动，为-1表示向左移动
		self.fleet_direction = 1
		
		#	计分
		self.alien_points = 50
	
	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed_factor *= self.speed_up_scale
		self.bullet_speed_factor *= self.speed_up_scale
		self.alien_speed_factor *= self.speed_up_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		print ("self.alien_points = " + str(self.alien_points))
