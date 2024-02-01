# Machine Learning Project: Predicting Student Performance

This machine learning project predicts student math scores based on various factors. The project includes data ingestion, transformation, model training, and prediction. Additionally, there is a web application for user interaction.

## Project Structure

### `mlproject` (Parent folder for the project)

- **`artifacts`**: Folder containing saved models, preprocessors, and other relevant artifacts.

- **`notebook`**: Folder for Jupyter notebooks.

- **`src`**: Source code folder.

  - **`components`**: Subfolder containing core components of the project.

    - `data_ingestion.py`: Handles loading and splitting the dataset.
    - `data_transformation.py`: Applies preprocessing to the input data.
    - `model_training.py`: Manages the training and evaluation of machine learning models.

  - **`pipeline`**: Subfolder containing the prediction pipeline.

    - `predict_pipeline.py`: Loads the trained model and preprocessor for making predictions.

  - `utils.py`: Contains utility functions used across the project, including saving and loading objects and model evaluation.

- **`templates`**: HTML templates for the web application.

- `app.py`: Main Flask application for user interaction.

- `README.md`: Project overview, usage instructions, and information about the structure.

- `requirements.txt`: List of dependencies for the project.

- `setup.py`: Setup script for packaging the project.


## How to Use

1. **Clone the repository:**

    ```bash
    git clone https://github.com/EkeminiUmanah/mlproject.git
    cd mlproject
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask application:**

    ```bash
    python app.py
    ```
