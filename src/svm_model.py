from sklearn.svm import SVC
from sklearn.metrics import classification_report
import joblib

def train_svm(X_train, y_train, X_test, y_test):
    model = SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))
    joblib.dump(model, "models/svm_model.pkl")
    return model
