# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This project uses a Random Forest classification model to predict whether a person's annual income is greater than $50,000 or less than or equal to $50,000. The model was trained using scikit-learn's RandomForestClassifier with a random state of 42. Categorical variables were processed using one-hot encoding before training the model.

## Intended Use

This model is intended as an educational example of building and deploying a machine learning classification model. The project includes data preprocessing, model training, evaluation, testing performance on different groups in the data, and deployment through a REST API. The model is not intended to be used for real-world decisions involving employment, credit, benefits, or other decisions that could significantly affect a person.

## Training Data

The model was trained using the Census Income dataset provided with the project. The dataset contains demographic and employment-related information including, age, education, occupation, work class, maritial status, race, sex, hours worked per week, and native country. The target variable is salary, which identifies whether income is greater than $50,000 or less than or equal to $50,000

The data was divided into training and testing sets using an 80/20 split with a random state of 42. Categorical variables were converted using one-hot encoding before the model was trained.

## Evaluation Data

Twenty percent of the Census Income dataset was reserved for testing and not used to train the model. The same preprocessing and categorical encoder learned from the training data were used on the test data.

In addition to evaluating the model on the entire test set, performance was tested separately for the different values within categorical variables such as work class, education, occupation, race, sex, relationship, marital status, and native country.

## Metrics

This model was evaluated using precision, recall, and F1 score. Precision measures how many of the model's positive predicitons were correct. Recall measures how many of the actual positive cases the model correctly identified. The F1 score combines precision and recall into one measure.

On the test dataset, the model achieved:
Precision: 0.7419
Recall: 0.6384
F1 score: 0.6863

Performance was also calculated for the the individual values within each categorical feature and saved into slice_output.txt. These results show that the model performs differently across some groups and categories.

## Ethical Considerations

The Census dataset includes sensitive demographic information such as race and sex. Because of this, it is important to consider that the model may perform differently across demographic groups and could reflect patterns or biases that already exist in the data.

This model should not be used to make decisions about employment, financial eligibility, access to services, or other important outcomes for individuals. Additional testing for bias and fairness would be necessary before a model like this could be considered for real-world use.

## Caveats and Recommendations

The model's performance varies across the different categories in the data, and some categories have far fewer records than others. Results for categories with very few records may not accurately represent how well the model would perform on a larger group. For example, a category with only a few test records could recieve perfect precision, recall, and F1 scores even though there is not enough data to know whether the model would consistantly perform that well.

The dataset also contains unknown values represented by ?, which could affect the model's performance. With more time, different methods for handling these unknown values could be explored. Other classification models, hyperparameter tuning, cross-validation, and additional testing for differences in performance across demographic groups could be considered.