class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion."""

	def __init__(self):
		"""Инициализирует настройки игры."""
		# Параметры экрана
		self.screen_width = 600 # 1200
		self.screen_height = 400 # 800
		self.bg_color = (0, 0, 255) # (230, 230, 230)
		# Настройки корабля
		self.ship_speed = 1.5
