import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
from IPython.display import display

def split_Xy(df, column):
    X_df = df.drop(columns=column)
    y_df = df[column]
    return X_df, y_df

def model_performs(X_df, y_df, model):
    pred = model.predict(X_df)
    acc = model.score(X_df, y_df)
    conf = confusion_matrix(y_df, pred)
    mat = pd.DataFrame(confusion_matrix(y_df, pred), index=['actual_didnt_churn', 'actual_churned'],
                       columns=['pred_didnt_churn', 'pred_churned'])
    rubric_df = pd.DataFrame([['True Negative', 'False positive'], ['False Negative', 'True Positive']],
                             columns=mat.columns, index=mat.index)
    cf = rubric_df + ': ' + mat.values.astype(str)
    tp = conf[1, 1]
    fp = conf[0, 1]
    fn = conf[1, 0]
    tn = conf[0, 0]
    tpr = tp / (tp + fn)
    fpr = fp / (fp + tn)
    tnr = tn / (tn + fp)
    fnr = fn / (fn + tp)
    clas_rep = pd.DataFrame(classification_report(y_df, pred, output_dict=True)).T
    clas_rep.rename(index={'0': "didnt churn", '1': "churned"}, inplace=True)
    print(f'''
    The accuracy for our model is {acc:.4%}
    The True Positive Rate is {tpr:.3%},    The False Positive Rate is {fpr:.3%},
    The True Negative Rate is {tnr:.3%},    The False Negative Rate is {fnr:.3%}
    ________________________________________________________________________________
    ''')
    print('''
    The positive is  'churned'
    Confusion Matrix
    ''')
    display(cf)
    print('''
    ________________________________________________________________________________
    
    Classification Report:
    ''')
    display(clas_rep)


def dec_tree(model, X_df):
    plt.figure(figsize=(24, 12))
    plot_tree(
        model,
        feature_names=X_df.columns.tolist(),
        class_names=['died', 'survived'],
    )
    plt.show()


def compare(model1, model2, X_df, y_df):
    pred1 = model1.predict(X_df)
    pred2 = model2.predict(X_df)
    acc1 = model1.score(X_df, y_df)
    acc2 = model2.score(X_df, y_df)
    conf1 = confusion_matrix(y_df, pred1)
    mat1 = pd.DataFrame(confusion_matrix(y_df, pred1),
                        index=['actual_didnt_churn', 'actual_churned'],
                        columns=['pred_didnt_churn', 'pred_churned'])
    rubric_df = pd.DataFrame([['True Negative', 'False positive'], ['False Negative', 'True Positive']],
                             columns=mat1.columns, index=mat1.index)
    cf1 = rubric_df + ': ' + mat1.values.astype(str)
    conf2 = confusion_matrix(y_df, pred2)
    mat2 = pd.DataFrame(confusion_matrix(y_df, pred2),
                        index=['actual_didnt_churn', 'actual_churned'],
                        columns

