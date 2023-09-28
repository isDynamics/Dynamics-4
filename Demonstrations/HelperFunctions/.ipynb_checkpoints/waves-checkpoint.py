import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import os

def create_grid_pos(x_size=5, y_size=5):
    '''
    Create grid positions to be populated by points
    '''
    # x_size: number of grid points in horizontal direction
    # y_size: number of grid points in vertical direction
    # x_pos: horizontal coordinates of grid points
    # y_pos: vertical coordinates of grid points
    x_pos = np.zeros((y_size, x_size))
    y_pos = np.zeros((y_size, x_size))

    for x in range(x_size):
        y_pos[:,x] = np.arange(y_size)

    for y in range(y_size):
        x_pos[y,:] = np.arange(x_size)

    return x_pos, y_pos

def longitudinal_travelling_wave(x_positions, y_positions, frames_per_cycle=20, wave_len=10,  amplitude=1, phase = 0, num_frames=100):
    '''
    Calculate positions of generated points in each frame using longitudinal wave equation
    '''
    # frames_per_cycle = number of frames per cycle
    # num_frames = frames to be generated
    k = 2 * np.pi / wave_len
    omega = 2 * np.pi / frames_per_cycle 
    x_frames = np.zeros((num_frames, x_positions.shape[0], x_positions.shape[1]))
    y_frames = np.zeros((num_frames, y_positions.shape[0], y_positions.shape[1]))

    for t in range(num_frames):
        y_frames[t,:,:] = y_positions
        for x in range(x_positions.shape[1]):
            x_frames[t,:,x] = x_positions[:,x] + amplitude * np.sin(k * x_positions[:,x] - omega * t + phase)

    return x_frames, y_frames


def update(frame_num, scat, x, y):
    idx = frame_num % x.shape[0]
    scat.set_offsets(np.column_stack((x[idx,:,:].flatten(), y[idx,:,:].flatten())))
    return scat
    