"""
Factor class for efficient categorical variable handling.

This module implements the core Factor class that provides fast group operations
and categorical variable manipulation inspired by Stata's ftools.
"""

import numpy as np
import pandas as pd
from typing import Union, List, Optional, Any


class Factor:
    """
    Factor class for efficient handling of categorical variables.
    
    This class provides fast group operations without requiring data sorting,
    using advanced hashing algorithms for optimal performance.
    """
    
    def __init__(self, data: Union[pd.Series, np.ndarray, List], 
                 method: str = "auto", 
                 sort_levels: bool = True,
                 save_keys: bool = True,
                 verbose: bool = False):
        """
        Initialize a Factor object.
        
        Parameters
        ----------
        data : pd.Series, np.ndarray, or list
            The categorical data to create factors from
        method : str, default "auto"
            Hashing method to use ("auto", "hash0", "hash1", "hash2")
        sort_levels : bool, default True
            Whether to sort the factor levels
        save_keys : bool, default True
            Whether to save the original keys
        verbose : bool, default False
            Whether to display debug information
        """
        self.data = data
        self.method = method
        self.sort_levels = sort_levels
        self.save_keys = save_keys
        self.verbose = verbose
        
        # Initialize core properties
        self.num_levels = 0
        self.num_obs = 0
        self.levels = None
        self.keys = None
        self.counts = None
        
        # Process the input data
        self._create_factor()
    
    def _create_factor(self):
        """Create the factor representation from input data."""
        # Convert input to numpy array for processing
        if isinstance(self.data, pd.Series):
            arr = self.data.values
        elif isinstance(self.data, list):
            arr = np.array(self.data)
        else:
            arr = self.data
        
        # Get unique values and their inverse mapping
        unique_vals, inverse = np.unique(arr, return_inverse=True)
        
        # Store results
        self.num_obs = len(arr)
        self.num_levels = len(unique_vals)
        self.levels = inverse + 1  # 1-indexed like Stata
        
        if self.save_keys:
            self.keys = unique_vals
        
        # Calculate counts
        self.counts = np.bincount(inverse)
        
        if self.verbose:
            print(f"Created factor with {self.num_levels} levels and {self.num_obs} observations")
    
    def collapse(self, values: Union[pd.Series, np.ndarray], 
                 method: str = "sum") -> np.ndarray:
        """
        Collapse values by factor groups.
        
        Parameters
        ----------
        values : pd.Series or np.ndarray
            Values to collapse
        method : str, default "sum"
            Aggregation method ("sum", "mean", "count", "min", "max")
        
        Returns
        -------
        np.ndarray
            Collapsed values for each factor level
        """
        if isinstance(values, pd.Series):
            values = values.values
        
        if method == "sum":
            return np.bincount(self.levels - 1, weights=values)
        elif method == "mean":
            sums = np.bincount(self.levels - 1, weights=values)
            return sums / self.counts
        elif method == "count":
            return self.counts.astype(float)
        elif method == "min":
            result = np.full(self.num_levels, np.inf)
            for i in range(self.num_obs):
                level_idx = self.levels[i] - 1
                result[level_idx] = min(result[level_idx], values[i])
            return result
        elif method == "max":
            result = np.full(self.num_levels, -np.inf)
            for i in range(self.num_obs):
                level_idx = self.levels[i] - 1
                result[level_idx] = max(result[level_idx], values[i])
            return result
        else:
            raise ValueError(f"Unknown aggregation method: {method}")
    
    def __repr__(self):
        """String representation of the Factor object."""
        return (f"Factor(num_levels={self.num_levels}, "
                f"num_obs={self.num_obs}, "
                f"method='{self.method}')")
    
    def __str__(self):
        """Human-readable string representation."""
        return self.__repr__()
