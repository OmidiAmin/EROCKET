# ==== Implementation of EROCKET feature selection method ========
# Cite this work as follow
"""
@INPROCEEDINGS{erocket,
  author={Omidi, M. A. and Seyfe, B. and Valaee, S.},
  booktitle={ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)}, 
  title={Reducing the Computational Complexity of Learning with Random Convolutional Features}, 
  year={2023},
  volume={},
  number={},
  pages={1-5},
  doi={10.1109/ICASSP49357.2023.10095893}}
"""

import numpy as np
from kneed import KneeLocator
from sklearn.linear_model import RidgeClassifierCV,RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def feature_selector(W):
    '''
    inpute: weight matrix W
            W is C X F, where F is the number of features
            and C is the number of classes.
            
    output: 
    unique feature indices maintain_ftr_indices_unique
    

 
    '''
    Sensitivity = 2 # Sensitivity of kneedle detection
    poly_deg = 3 # Polynomial degree of spline smoother.
    n_targ = W.shape[0]
    num_features = W.shape[1]
    argsorted_W = np.zeros((n_targ, num_features), dtype = int)
    split_points = np.zeros(n_targ, dtype = int)
    for i in range(n_targ):
        Wi = W[i,:] 
        argsorted_W[i,:] = np.argsort(Wi)
        sorted_curve = Wi[argsorted_W[i,:]]
        posit_points = np.where(sorted_curve >=0)[0] # Positive points in the sorted curve
        split_points[i] = posit_points[0]
        # positive_ftr_indices = argsorted_W_0[split_point:] # positive feature indices
        # negative_ftr_indices = argsorted_W_0[:split_point] # negative feature indices

    knees_plus = np.zeros((n_targ,))

    for i in range(n_targ):
        posit_len = len(W[i,:]) - split_points[i]
        k1 = KneeLocator(range(posit_len), 
                        W[i, argsorted_W[i, split_points[i]:].astype(int)], 
                        curve="convex", direction="increasing",
                        S = Sensitivity,
                        polynomial_degree = poly_deg)
        knee_loc = k1.knee
        knees_plus[i] = knee_loc
                
    # find knee on negative side
    knees_minus = np.zeros((n_targ,))
    for i in range(n_targ):
        negat_len = split_points[i]
        k2 = KneeLocator(range(negat_len), 
                        W[i,argsorted_W[i, : negat_len].astype(int)], 
                        curve="concave", direction="increasing",
                        S = Sensitivity,
                        polynomial_degree = poly_deg)
        knee_loc2 = k2.knee
        knees_minus[i] = knee_loc2
                
    maintain_ftr_indices = []
            
    for i in range(n_targ):
        maintain_ftr_indices = maintain_ftr_indices +\
        argsorted_W[i, split_points[i] + knees_plus[i].astype(int):].tolist() +\
        argsorted_W[i,: knees_minus[i].astype(int)].tolist()
                
    maintain_ftr_indices_unique = np.unique(maintain_ftr_indices) # union of indices
    return maintain_ftr_indices_unique, split_points, knees_minus, knees_plus


