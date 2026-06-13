import joblib

model = joblib.load("../Model/car_price_model.pkl")

year = int(input("Enter Car Year: "))
present_price = float(input("Enter Present Price: "))
kms_driven = int(input("Enter Kilometers Driven: "))
owner = int(input("Number of Previous Owners: "))

prediction = model.predict(
    [[year, present_price, kms_driven, owner]]
)

print("\nPredicted Selling Price:")
print(round(prediction[0], 2), "Lakhs")