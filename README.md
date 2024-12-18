# House Price Prediction

This project uses **Linear Regression** to predict house prices based on the area of the house. It trains the model using a dataset and evaluates its performance using the R-squared metric.
## video demo 
https://youtu.be/wzDIi84WqyE?si=G9EhpZBtsjoYhGZV

## Features

- Predict house prices based on the area (in square meters).
- Visualize the relationship between area and price with a scatter plot and a regression line.
- Evaluate the model's performance using the R-squared score.
- View the model's coefficient and intercept.

## Technologies Used

- **Python 3.x**
- Libraries:
  - `pandas`: For data manipulation.
  - `numpy`: For numerical computations.
  - `matplotlib`: For plotting and visualization.
  - `scikit-learn`: For building the linear regression model and performance evaluation.

## Dataset

The dataset is stored in a file named `house_prices.csv`. It contains two columns:
- `Area`: The size of the house in square meters.
- `Price`: The price of the house in your chosen currency.

## How to Run the Project

1. **Install Dependencies**:
   Ensure you have the required libraries installed. Run the following command to install them if needed:
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```

2. **Prepare the Dataset**:
   - Ensure the `house_prices.csv` file is in the same directory as the script.
   - The file should have columns named `Area` and `Price`.

3. **Run the Script**:
   Execute the script in your terminal:
   ```bash
   python <script_name>.py
   ```

4. **Input House Area**:
   - When prompted, input the area of the house (e.g., `120` for 120 m²).
   - The script will predict the price based on the trained model.

## Visualization

The project generates two visualizations:

1. Scatter plot of the training data (`Area` vs. `Price`).
2. Regression line plotted over the scatter plot to represent the model's predictions.

## Model Details

- **Coefficient**: Indicates how much the price increases for each additional square meter.
- **Intercept**: The base price when the area is 0.
- **R-squared Score**: Measures how well the model fits the data (closer to 1 is better).

## Example Output

```
input Area: 120
Predicted price: 250000.00
Model R2 Score: 0.89
Model Coefficient: 2100.5
Model Intercept: 45000.0
```

## File Structure

```
.
├── house_prices.csv      # Dataset file
├── <script_name>.py      # Python script
└── README.md             # Project documentation
```

## License

This project is for educational purposes and does not come with a specific license.

---

Feel free to modify and extend this project to include additional features like multi-variable regression or advanced visualizations!
