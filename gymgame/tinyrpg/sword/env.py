from gymgame import framework
from gym import envs, spaces
from gym.envs import register
from . import config
from . import game
from .serializer import Serializer
from gymgame.tinyrpg.framework.render import Render
# from .render import Render



class EnvironmentGym(framework.EnvironmentGym):
    def __init__(self, *args, **kwargs):
        super(EnvironmentGym, self).__init__(*args, **kwargs)
        self._window = None

    def _init_action_space(self): return spaces.Discrete(1)

    def _reward(self): return 0

    def close(self, *args, **kwargs): pass  # close will trigger render(don't need it in many case)

    def _render(self, *args, **kwargs):
        if self._window is None:
            self._window = Render(self, bokeh_mode=config.BOKEH_MODE)
        else:
            self._window()



register(
    id=config.GAME_NAME,
    entry_point='gymgame.tinyrpg.sword:EnvironmentGym',
    max_episode_steps=1e+10,
    kwargs={'initializer': lambda: (game.make(), Serializer(config.GRID_SIZE)) }
)