#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 13:23:14 2017

History:
10/16/2024: modified for BROVERETTE
11/13/2023: modified for AGRIBOT
11/28/2020: modified for OSCAR 

@author: jaerock
"""

###############################################################################
#

import os
import yaml
import sys
import const 

class Config:
    try:
        # Update to use BROVERETTE_PATH
        config_name = os.environ['BROVERETTE_PATH'] + '/config/' + const.CONFIG_FILENAME
    except:
        exit('ERROR: BROVERETTE_PATH not defined. Please source setup.bash.') 

    # Open the main config file (config-humberto.yaml or equivalent)
    with open(config_name) as file:
        config_yaml = yaml.load(file, Loader=yaml.FullLoader)
        print('=======================================================')
        print('               Configuration Settings')
        print('=======================================================')
        neural_net_yaml_name = config_yaml['neural_net']
        print('Neural Net:     \t' + neural_net_yaml_name)
        data_collection_yaml_name = config_yaml['data_collection']
        print('Data Collection:\t' + data_collection_yaml_name)
        run_neural_yaml_name = config_yaml['run_neural']
        print('Run Neural:     \t' + run_neural_yaml_name)
        print('\n')

    # neural_net config file
    neural_net_yaml = os.environ['BROVERETTE_PATH'] + '/config/neural_net/' + neural_net_yaml_name + '.yaml'
    with open(neural_net_yaml) as file:
        neural_net = yaml.load(file, Loader=yaml.FullLoader)

    # data_collection config file
    data_collection_yaml = os.environ['BROVERETTE_PATH'] + '/config/data_collection/' + data_collection_yaml_name + '.yaml'
    with open(data_collection_yaml) as file:
        data_collection = yaml.load(file, Loader=yaml.FullLoader)

    # run_neural config file
    run_neural_yaml = os.environ['BROVERETTE_PATH'] + '/config/run_neural/' + run_neural_yaml_name + '.yaml'
    with open(run_neural_yaml) as file:
        run_neural = yaml.load(file, Loader=yaml.FullLoader)

    def __init__(self): # model_name):
        pass
    
    @staticmethod
    def summary():
        print('=======================================================')
        print('                 System Configuration ')
        print('=======================================================')
        print(':::::::::::::::::::::: Neural Net :::::::::::::::::::::')
        print(yaml.dump(Config.neural_net))
        print('::::::::::::::::::: Data Collection :::::::::::::::::::')
        print(yaml.dump(Config.data_collection))
        print(':::::::::::::::::::::: Run Neural :::::::::::::::::::::')
        print(yaml.dump(Config.run_neural))


if __name__ == '__main__':
    Config.summary()
