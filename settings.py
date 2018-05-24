class Settings():
    # 存储外星人入侵的所有设置的类
    def __init__(self):
        """初始化游戏的设置"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 675
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed_factor = 1.5

        # bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        #alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction=1(right) or -1(left)
        self.fleet_direction = 1
