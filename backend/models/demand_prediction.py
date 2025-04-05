import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def train_demand_model():
    data = np.array([10, 20, 30, 40, 50, 60, 70]).reshape(-1, 1)
    model = Sequential([
        LSTM(50, activation='relu', input_shape=(1, 1)),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    X = np.array([0, 1, 2, 3, 4, 5]).reshape(-1, 1, 1)
    y = np.array([20, 30, 40, 50, 60, 70])
    model.fit(X, y, epochs=200)
    return model

if __name__ == "__main__":
    model = train_demand_model()
    model.save("demand_model.h5")  # Save trained model