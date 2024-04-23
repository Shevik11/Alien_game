class Settings:

    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = 'white'

        self.ship_speed = 1
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 2
        self.bullet_width = 1500
        self.bullet_height = 15
        self.bullet_color = 'green'
        self.bullets_allowed = 3


        self.alien_speed = 1.0
        self.fleet_drop_speed = 15
        # fleet_direction. 1 - right; -1 - left;
        self.fleet_direction = 1

        self.speedup_scale = 1.05
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


