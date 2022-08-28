# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    
    # TODO - implement this in part 2
    
    
    ''' First: We created new beliefs by multiplying all current beliefs
                by p_hit if observed and p_miss otherwise.
    '''
    new_beliefs = []
    for place, belief in zip(grid, beliefs):
        new = []
        for i in range(len(belief)):
            p = color==place[i]
            new.append(belief[i] * (p*p_hit+(1-p)*p_miss))
        new_beliefs.append(new)
        
        
    ''' Second: We need the new beliefs to be a probability distribution
                by dividing each element in the new beliefs by
                the sum of all new beliefs (Normalization).
    '''
    total = sum([sum(list_) for list_ in new_beliefs])
    normalized_new_beliefs = []
    for n_beliefs in new_beliefs:
        normalized_new_beliefs.append([item/total for item in n_beliefs])
        
    return normalized_new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height 
            new_j = (j + dx ) % width
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)