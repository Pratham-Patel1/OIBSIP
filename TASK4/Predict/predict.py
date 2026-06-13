import joblib

model = joblib.load(
    "../Model/spam_detector.pkl"
)

vectorizer = joblib.load(
    "../Model/vectorizer.pkl"
)

message = input(
    "Enter Email Message: "
)

message_vector = vectorizer.transform(
    [message]
)

prediction = model.predict(
    message_vector
)

if prediction[0] == 1:
    print("\nSpam Email")
else:
    print("\nNot Spam Email")