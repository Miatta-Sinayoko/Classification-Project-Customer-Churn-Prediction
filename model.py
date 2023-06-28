import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib.pyplot as plt
from IPython.display import display, display_html
from sklearn.dummy import DummyClassifier

# Split our X and y

def split_Xy(df, column):
    '''
    Split the data into X (features) and y (target) DataFrames.

    Parameters:
    - df: DataFrame containing the data.
    - column: Name of the column representing the target variable.

    Returns:
    - X_df: DataFrame containing the features.
    - y_df: DataFrame containing the target variable.
    '''
    X_df = df.drop(columns=column)
    y_df = df[[column]]
    return X_df, y_df


def model_performs(X_df, y_df, model):
    '''
    Fit the model, make predictions, and evaluate its performance.

    Parameters:
    - X_df: DataFrame containing the features.
    - y_df: DataFrame containing the target variable.
    - model: Trained classification model.
    '''
    # Make predictions
    pred = model.predict(X_df)

    # Calculate accuracy
    acc = model.score(X_df, y_df)

    # Calculate confusion matrix
    conf = confusion_matrix(y_df, pred)
    mat = pd.DataFrame(conf, index=['actual_didnt_churn', 'actual_churned'],
                       columns=['pred_didnt_churn', 'pred_churned'])

    # Create a rubric DataFrame for interpretation of confusion matrix
    rubric_df = pd.DataFrame([['True Negative', 'False Positive'], ['False Negative', 'True Positive']],
                             columns=mat.columns, index=mat.index)
    cf = rubric_df + ': ' + mat.values.astype(str)

    # Calculate true positive rate, false positive rate, true negative rate, and false negative rate
    tn, fp, fn, tp = conf.ravel()
    tpr = tp / (tp + fn)
    fpr = fp / (fp + tn)
    tnr = tn / (tn + fp)
    fnr = fn / (fn + tp)

    # Generate classification report
    clas_rep = pd.DataFrame(classification_report(y_df, pred, output_dict=True)).T
    clas_rep.rename(index={'0': "didnt churn", '1': "churned"}, inplace=True)

    # Print the performance metrics and display the confusion matrix and classification report
    print(f'''
    The accuracy for our model is {acc:.4%}
    The True Positive Rate is {tpr:.3%},    The False Positive Rate is {fpr:.3%},
    The True Negative Rate is {tnr:.3%},    The False Negative Rate is {fnr:.3%}
    ________________________________________________________________________________
    ''')
    print('''
    The positive is 'churned'
    Confusion Matrix
    ''')
    display(cf)
    print('''
    ________________________________________________________________________________
    
    Classification Report:
    ''')
    display(clas_rep)


def dec_tree(model, X_df):
    '''
    Plot a decision tree.

    Parameters:
    - model: Trained decision tree model.
    - X_df: DataFrame containing the features.
    '''
    plt.figure(figsize=(24, 12))
    plot_tree(
        model,
        feature_names=X_df.columns.tolist(),
        class_names=['didnt churn', 'churned']
    )
    plt.show()      
