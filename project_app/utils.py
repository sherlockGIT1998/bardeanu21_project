import numpy as np
import pandas as pd
import json
import pickle
import warnings
warnings.filterwarnings("ignore")
import config


class KmeanCluster:
    def __init__(self,nsites,volume,density,symmetry__number,symmetry__symprec,formation_energy_per_atom,energy_above_hull,band_gap,total_magnetization,is_stable,is_metal,theoretical,symmetry__crystal_system,symmetry__symbol,symmetry__point_group,ordering):
        self.nsites=nsites,
        self.volume=volume,
        self.density=density,
        self.symmetry__number=symmetry__number,
        self.symmetry__symprec=symmetry__symprec,
        self.formation_energy_per_atom=formation_energy_per_atom,
        self.energy_above_hull=energy_above_hull,
        self.band_gap=band_gap,
        self.total_magnetization=total_magnetization,
        self.is_stable=is_stable,
        self.is_metal=is_metal,
        self.theoretical=theoretical,
        self.symmetry__crystal_system=symmetry__crystal_system,
        self.symmetry__symbol=symmetry__symbol,
        self.symmetry__point_group=symmetry__point_group,
        self.ordering=ordering

        symmetry__crystal_system="symmetry__crystal_system_"+symmetry__crystal_system
        symmetry__symbol='symmetry__symbol_'+symmetry__symbol
        symmetry__point_group='symmetry__point_group_'+symmetry__point_group
        ordering='ordering_'+ordering

        symmetry__crystal_system_index=np.where(self.json_data["columns"]==symmetry__crystal_system)[0]
        symmetry__symbol_index=np.where(self.json_data["columns"]==symmetry__symbol)[0]
        symmetry__point_group_index=np.where(self.json_data["columns"]==symmetry__point_group)[0]
        ordering_index= np.where(self.json_data["columns"]==ordering)[0]
        
    def load_model(self):
        with open("KMean_model.pkl", "rb") as f:
            self.model=pickle.load(f)

        with open("KMean_model.json",'r') as f:
            self.json_data=json.load(f)

    def Prediction(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.nsites                                   
        test_array[1] = self.volume                                 
        test_array[2] = self.density                                
        test_array[3] = self. symmetry__number                         
        test_array[4] = self.symmetry__symprec                      
        test_array[5] = self.formation_energy_per_atom              
        test_array[6] = self.energy_above_hull                      
        test_array[7]= self.band_gap                     
        test_array[8]= self.total_magnetization                               
        test_array[9]= self.json_data['is_stable'][self.is_stable]                              
        test_array[10]= self.json_data['is_metal'][self.is_metal]                             
        test_array[11]= self.json_data['theoretical'][self.theoretical]                                 
        test_array[self.symmetry__crystal_system_index]= 1                   
        test_array[self.symmetry__symbol_index]=1                              
        test_array[self.symmetry__point_group_index]=1          
        test_array[self.ordering_index]=1 
        print('test_array',test_array)
        cluster=self.model.predict([test_array])
        return cluster
    
if __name__=="__main__":

    nsites=44.000000                                   
    volume=487.283476                                 
    density=4.292537                                
    symmetry__number=0.100000                         
    symmetry__symprec=0.1                    
    formation_energy_per_atom=-1.43             
    energy_above_hull=0.02086                      
    is_stable=0                              
    band_gap=0.0000                              
    is_gap_direct=1                           
    is_metal=0                                 
    total_magnetization=1                   
    theoretical=1                            
    symmetry__crystal_system='Hexagonal'      
    symmetry__symbol='C2/c'                    
    symmetry__point_group='2/m'            
    ordering='AFM' 
        

        

    output= KmeanCluster(nsites,volume,density,symmetry__number,symmetry__symprec,formation_energy_per_atom,energy_above_hull,band_gap,total_magnetization,is_stable,is_metal,theoretical,symmetry__crystal_system,symmetry__symbol,symmetry__point_group,ordering)
    cluster=output.Prediction()
    print("cluster :",cluster)    