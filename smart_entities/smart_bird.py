from NEAT.genome import genome
from entities.bird import bird

from timeit import default_timer as timer

import numpy as np

from sklearn.preprocessing import normalize


class smart_bird(genome):
    def __init__(self, num_inputs, num_outputs):
        super().__init__(num_inputs, num_outputs)
        
        self.start_time = -1
        self.end_time = -1

    def init_bird_entity(self, screen_size):
        self.bird_entity = bird(screen_size)
        self.screen_size = screen_size

    def reset(self):
        self.start_time = -1
        self.end_time = -1

    def start(self):
        self.start_time = timer()
    
    def end(self):
        self.end_time = timer()

    def make_observation(self, pipes):

        #Getting top pipe, bottom pipe, and bird's y position as an observation
        bird_position = self.bird_entity.hitbox.centery
        bird_velocity = self.bird_entity.y_velocity
        pipe_begin = pipes.top_pipe.left
        pipe_end = pipes.top_pipe.right
        gap_distance = pipes.bottom_pipe.top - pipes.top_pipe.bottom
        top_pipe_position = pipes.top_pipe.bottom
        bottom_pipe_position = pipes.bottom_pipe.top

        observation = np.array([bird_position, 
                                bird_velocity, 
                                pipe_begin,
                                pipe_end,
                                gap_distance,
                                top_pipe_position,
                                bottom_pipe_position], dtype=np.float32)

        mini = min(observation)
        maxi = max(observation)
        for i in range(0, len(observation)):
            observation[i] = (observation[i]-mini) / (maxi - mini)
        
        return observation