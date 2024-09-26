class GameState:
    consecutive_draws = 0

    @classmethod
    def increment_draws(cls):
        cls.consecutive_draws += 1
