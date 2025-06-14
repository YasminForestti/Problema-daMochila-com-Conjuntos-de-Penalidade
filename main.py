import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env") 
INSTANCES_PATH = os.getenv('INSTANCES')

from utils.data import Data
from utils.knapsack import Knapsack
import numpy as np


data_1 = Data(f'{INSTANCES_PATH}/scenario1/correlated_sc1/300/kpfs_1.txt')

m = Knapsack(data_1)
print(m.get_cost_benefit_ratio())

# m.add_item(0)
# print(np.argsort(m.get_cost_benefit_ratio(), kind='heapsort')[::-1])
# m.add_item(98)
# m.add_item(263)
# m.remove_item(98)
# print(m.is_valid())
