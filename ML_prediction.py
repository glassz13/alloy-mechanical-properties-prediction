# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("mechanical_properties.csv")

# Define features (X) and targets (y)
X = data[["Composition", "Temperature (K)", "Strain Rate"]]

y_YM = data["Young's Modulus (GPa)"]
y_YS = data["Yield Strength (GPa)"]
y_UTS = data["UTS (GPa)"]

# Split train-test sets ONLY ONCE
X_train, X_test, y_YM_train, y_YM_test = train_test_split(
    X, y_YM, test_size=0.3, random_state=42
)

# For other targets, we reuse the same indices
y_YS_train = y_YS.loc[y_YM_train.index]
y_YS_test = y_YS.loc[y_YM_test.index]

y_UTS_train = y_UTS.loc[y_YM_train.index]
y_UTS_test = y_UTS.loc[y_YM_test.index]

# Train Random Forest models for each property
rf_YM = RandomForestRegressor(n_estimators=100, random_state=42)
rf_YS = RandomForestRegressor(n_estimators=100, random_state=42)
rf_UTS = RandomForestRegressor(n_estimators=100, random_state=42)

rf_YM.fit(X_train, y_YM_train)
rf_YS.fit(X_train, y_YS_train)
rf_UTS.fit(X_train, y_UTS_train)

# Make predictions
y_YM_pred = rf_YM.predict(X_test)
y_YS_pred = rf_YS.predict(X_test)
y_UTS_pred = rf_UTS.predict(X_test)

# Evaluate performance
def evaluate(y_true, y_pred, name):
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"\n{name}")
    print(f"  MAE: {mae:.3f}")
    print(f"  R2:  {r2:.3f}")

evaluate(y_YM_test, y_YM_pred, "Young's Modulus")
evaluate(y_YS_test, y_YS_pred, "Yield Strength")
evaluate(y_UTS_test, y_UTS_pred, "UTS")

# Feature importance for Young's Modulus
feature_importances = pd.Series(
    rf_YM.feature_importances_, index=X.columns
).sort_values(ascending=False)

print("\nFeature Importances (Young's Modulus):")
print(feature_importances)

# Visualize predictions
def plot_predictions(y_true, y_pred, title):
    plt.figure(figsize=(6,6))
    sns.scatterplot(x=y_true, y=y_pred)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title(title)
    plt.grid()
    plt.show()

plot_predictions(y_YM_test, y_YM_pred, "Young's Modulus Prediction")
plot_predictions(y_YS_test, y_YS_pred, "Yield Strength Prediction")
plot_predictions(y_UTS_test, y_UTS_pred, "UTS Prediction")
