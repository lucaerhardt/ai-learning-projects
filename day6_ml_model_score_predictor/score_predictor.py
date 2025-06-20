from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

hours = [[1], [2], [3], [4], [5], [6], [7]]
scores = [45, 50, 55, 60, 65, 70, 75]

model = LinearRegression()
model.fit(hours, scores)

print("Predicted score for 8 hours:", model.predict([[8]])[0])

plt.scatter(hours, scores, color='blue')
plt.plot(hours, model.predict(hours), color='red')
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Study Hours vs Score")
plt.show()
