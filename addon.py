cm = confusion_matrix(excel_data['Answer'], excel_data['Generated Reply'], labels=['yes', 'no'])
TN, FP, FN, TP = cm[0,0], cm[0,1], cm[1,0], cm[1,1]

# Create readable table
df = pd.DataFrame(
    [[TN, FN], [FP, TP]],
    index=["Actual No", "Actual Yes"],
    columns=["Predicted No", "Predicted Yes"]
)

print("Confusion Matrix:")
print(df)
print("\n")

Accuracy = (TN+TP)/(TN+FP+FN+TP)
print("Model's Classification Accuracy :", Accuracy)

Precision = (TP/(TP+FP))
Recall = (TP/(TP+FN))

print("Model's Precision :", (TP/(TP+FP)))
print("Model's Recall :", (TP/(TP+FN)))

F1 = (2*Precision*Recall)/(Precision+Recall)
print("F1 Score: ", F1)
