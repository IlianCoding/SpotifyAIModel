# Project Report

## Objective
The goal was to predict the track popularity using a dataset that includes various features. We aimed to apply different machine learning models to determine the best-performing approach for this prediction task.

## Data Summary
Upon reviewing the dataset, we observed that it consists of several features, but many of these may lack a strong correlation with track_popularity. This lack of correlation impacts the model's predictive power, as the available features do not capture enough information to accurately model the target variable. Key observations include:

- **Feature Relevance**: Limited correlation between features and track_popularity potentially limits model performance.
- **Predictive Complexity**: Track popularity is likely influenced by numerous external, complex factors, which are not easily captured through simple machine learning techniques.

## Models and Results

### K-Nearest Neighbors (KNN) Regressor
- **Strengths**: Simplicity and effectiveness with well-distributed data.
- **Weaknesses**: Sensitive to irrelevant features and the curse of dimensionality, which limited predictive accuracy.
- **Performance**: Showed moderate performance but struggled with generalization, particularly in validation and test sets.
- **Hyperparameters**: Showed little improvements in the accuracy of the validation and test set, but in general not any notable improvements.

### RandomForestRegressor
- **Strengths**: Able to capture interactions between features and manage overfitting.
- **Weaknesses**: Limited by the lack of important predictive features, leading to underfitting on the validation and test data.
- **Performance**: Achieved moderate R² on training data but did not generalize well to unseen data, suggesting insufficient complexity for this task.
- **Hyperparameters**: Tuning the hyperparameters did not significantly improve the model’s performance, indicating that the model’s limitations were not due to hyperparameter settings. The model also contains a high number of features, which may have contributed to overfitting.

### Linear Regressor
- **Strengths**: Fast to train and interpretable results.
- **Weaknesses**: Unable to capture non-linear relationships, resulting in poor predictive accuracy.
- **Performance**: This model had the weakest performance, indicating that the relationships in the data are non-linear and more complex than linear regression can handle.
- **Hyperparameters**: We didn't implement hyperparameter tuning for the linear regression because of the low performance of the model.

### ExtraTreesRegressor
- **Strengths**: Captures complex interactions and reduces overfitting with feature randomization.
- **Weaknesses**: Similar to RandomForest, it was limited by the dataset’s lack of strongly predictive features.
- **Performance**: Showed similar results to RandomForest, slightly better in capturing variance but still unable to generalize accurately.
- **Hyperparameters**: Tuning the hyperparameters did not significantly improve the model’s performance, indicating that the model’s limitations were not due to hyperparameter settings.

## Conclusion
Traditional regression models, including KNN, RandomForestRegressor, LinearRegressor, and ExtraTreesRegressor, were insufficient for accurately predicting track_popularity. A neural network-based approach with a more comprehensive feature set may offer improved predictive capabilities.