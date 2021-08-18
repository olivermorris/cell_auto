import numpy as np
import math

from numpy.random import f




genome_path = input("Welcome to the Cinpl, please input the path to your source file.: ")
genome = np.zeros((2,100,15))
sim_grid = np.zeros((10000))
equation_list = np.zeros((10000), dtype = 'object')



def calc(f_protein, m_protein, halting):
    for f in reversed(range(0, halting)):
        #result_top = [(m_protein[i]+f_protein[f]) for i in range(0, halting)]
        for i in range(0, halting):
            match = (m_protein[i]+f_protein[f])[0],(m_protein[i]+f_protein[f])[-1]
            if match[0] == 3:
                pass

def move_calc(f_protein,  m_protein, direction, shape, move_array, cordinate_array):
    if cordinate_array[0] == 'start':
        if f_protein[0][0]+m_protein[-1][-1] == 3:
            move_calc(f_protein, m_protein, direction, shape, move_array, cordinate_array)
    



        

    





        print('result bottom',result_top)
        '''
        result_bottom = f_protein[-1]+m_protein[0]
        result_left = f_protein[:][0]+m_protein[:][-1]
        result_right = f_protein[:][-1]+m_protein[:][0]
        '''
        



   

        
            


       
        







def start_sim(grid, genome, sym, dimension, simulation_length):
    cells = list(np.where(grid> 0)[0])
    if len(cells) > 0:
        for cell in cells:  
             where_active_f = genome[0][np.where(genome[0,:,0] > 0)[0]]
             where_active_m = genome[1][np.where(genome[1,:,0] > 0)[0]]
             for f_protein in where_active_f:
                 for m_protein in where_active_m:
                     calc(f_protein[0:9].reshape((dimension, dimension)), m_protein[0:9].reshape((dimension, dimension)), dimension)

    else:
        return "Simulation Extinct"





           






genome_file = open(genome_path, "r")
m_counter = 0
f_counter = 0
for input_str in genome_file:
    input = input_str.split(',')
    if input[0] != 'header(start':
        equation_list[m_counter+f_counter] = str(input[11])
        input[11] = m_counter+f_counter
        line = [float(i) for i in input[1:-2]]
        #print(line)
        if line[9] == 0:
            genome[0][f_counter] = line
            f_counter+=1

        if line[9] == 1:
            # addin the extra values makes it fit into the data because duplicate has the direction values
            line.extend((0,0,0,0))
            genome[0][f_counter] = line
            f_counter+=1

        if line[9] == 2:
            #print('eeeef')
            line.extend((0,0,0,0))
            genome[1][m_counter] = line
            m_counter+=1
        

        
            

            
    if input[0] == 'header(start':
        #this creates the rules on start for the simulation
        sym = input[1]
        dimension = int(input[2])
        sim_grid[int(input[3])] = 1
        simulation_length = int(input[4])

print(start_sim(sim_grid, genome, sym, dimension, simulation_length))

        



