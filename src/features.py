import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.stem import PorterStemmer
import nltk

class KeywordProcessor(BaseEstimator, TransformerMixin):
    """
    A scikit-learn compatible transformer for processing keyword text data.
    
    This transformer fills missing values, replaces '%20' with spaces, 
    and applies stemming to each word using the PorterStemmer. 
    
    It handles input as a DataFrame, numpy array, or 2D array for compatibility with ColumnTransformer.
    Supports multiple columns and outputs feature names.
    """
    
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.feature_names_out = None  # Will hold the names of the features after transformation

    def fit(self, X, y=None):
        # Save feature names if input is a DataFrame
        if isinstance(X, pd.DataFrame):
            self.feature_names_out = X.columns.tolist()
        else:
            # Otherwise, create generic names for numpy arrays
            self.feature_names_out = [f'feature_{i}' for i in range(X.shape[1])]
        return self

    def transform(self, X):
        """
        Transforms the input DataFrame or 2D array by processing the keywords.

        Parameters
        ----------
        X : array-like, shape [n_samples, n_features]
            Input keyword data to be processed.

        Returns
        -------
        X_processed : np.ndarray
            Processed (stemmed) keyword data as a 2D numpy array.
        """
        # Handle both pandas DataFrame and numpy array input
        if isinstance(X, pd.DataFrame):
            X_processed = X.apply(self._process_column)
        elif isinstance(X, np.ndarray):
            X_processed = pd.DataFrame(X).apply(self._process_column)
        else:
            raise ValueError("Input type must be pandas DataFrame or numpy array")
        
        # Return as 2D numpy array
        return X_processed.values

    def _process_column(self, col):
        """Internal method to process each column by filling missing values, replacing '%20', and stemming."""
        col = col.fillna('N/A')
        col = col.str.replace('%20', ' ', regex=False)
        return col.map(lambda x: ' '.join([self.stemmer.stem(word) for word in nltk.word_tokenize(x)]))

    def get_feature_names_out(self, input_features=None):
        """
        Returns the output feature names for the transformation.
        
        If input_features is provided, it is used to override the default feature names.
        """
        if input_features is None:
            return np.array(self.feature_names_out)
        else:
            return np.array(input_features)

