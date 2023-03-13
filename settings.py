class Settings():

    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические  настройки игры."""
        #Параметры экрана

        self.screen_width = 1100
        self.screen_height = 650
        self.bg_color = (120, 200, 255)
        #Настройки коробля
        self.ship_limit = 3
        #Параметры снаряда
        self.bullet_width = 5
        self.bullet_height = 25
        self.bullet_color = (250, 20, 60)
        self.bullets_allowed = 5

        #Настройки пришельцев.
        self.fleet_drop_speed = 5

        # Темп ускорения игры.
        self.speedup_scale = 1.3
        # Темп роста стоимости пришельцев
        self.score_scale = 1.3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки изменяющиеся во время игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 0.5

        # fleet_direction = 1 обазначает движение вправо; а  -1 влево.
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличение настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

