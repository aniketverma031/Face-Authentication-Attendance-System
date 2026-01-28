import numpy as np

def motion_detected(prev_frame, curr_frame, threshold=30000):
    diff = np.sum(np.abs(prev_frame.astype("int") - curr_frame.astype("int")))
    return diff > threshold
