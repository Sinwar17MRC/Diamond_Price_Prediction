# Diamond Price Prediction Web APP

This project is a Diamond Price Prediction Web Application developed using Flask, HTML, CSS, and JavaScript, with a machine learning model integrated to predict diamond prices based on various attributes. The app allows users to enter details such as carat, cut, color, clarity, and dimensions, then utilizes a pre-trained machine learning model to provide an estimated price. The model is trained on a comprehensive diamond dataset, leveraging attributes that impact diamond valuation. This tool aims to help users gain insights into the diamond market and make informed purchasing or valuation decisions.

The app features a responsive front end, crafted with a user-friendly interface, including a prediction form, error handling, and a stylish design. The project showcases the seamless integration of machine learning in web applications, utilizing Flask APIs to serve predictions.

## Table of Content
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Dataset and Model Training](#Dataset-and-Model-Training)
- [Frontend Design](#frontend-design)
- [Future Improvements](#future-improvements)
- [Contact Information](#contact-information)

 ## Features
- **User Input**: Interface for the user to enter the specifications of the diamond (geometry, physical weight, color).
- **Prediction**: Estimation of the diamond's price based on the given data.
- **Informative Resources**: Links to resources on how to choose a diamond for rings and evaluate diamond quality.
- **Shopping Experience**: Includes a link to Blue Nile, a specialized shop in the gems market.
- **Educational Resources**: The app provides insights into the machine learning algorithm used for price prediction.
- **Stability Check**: Allows users to check the stability of the server to ensure prediction functionality is accessible.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript.
- **Backend**: Flask (for serving the machine learning model).
- **Python Libraries**: Scikit-learn, Pandas, NumPy.
- **Deployment**: Docker, Google Cloud Service.
- **Version Control**: Git, GitHub.

## Usage

1. **Accessing the App**:
   - Once the application is running, open your browser and navigate to `(https://app-486638708818.europe-west1.run.app/)`.
2. **Interacting with the home Page**:
   - After opening the link, you're now in the ome page.
   - You can access to a page explaining all about the diamonds and how to buy one through the **Read more** button.
   - If you're willing to directly predict the price of a diamond, you acan access the predict page through the **predict** button.
   - Scroll down to discover all features on the other sections in the home page( checking **API status**, Discovering th markdown of the model...).
   - In the bottom of the page you find the **About us** part.
   - you can contact the team through the **Contact** bar on the navbar or Through the LinkedIn profiles linked in the About US section.
     
2. **Entering Diamond Specifications**:
   - On the **Predict** page, you’ll find a form to input various diamond attributes:
     - **Carat**: Enter the diamond's weight in carats.
     - **Cut**: Select the cut quality from options like Ideal, Premium, Very Good, Good, or Fair.
     - **Color**: Choose the diamond color grade, ranging from D (best) to J.
     - **Clarity**: Choose the clarity rating from options like IF (best), VVS1, VS2, etc.
     - **Depth, Table, Length (X), Width (Y), and Height (Z)**: Enter the diamond’s physical dimensions as required.

3. **Submitting for Prediction**:
   - After filling in all the specifications, click the **Predict Price** button to send the information to the server.
   - The app will validate the inputs, display any error messages if needed, and then send the data to the machine learning model.

4. **Viewing the Result**:
   - A modal popup will display the estimated price of the diamond based on your inputs.
   - Click the **Close** button on the modal to exit and make another prediction, if desired.

## Dataset and Model Training

- **Dataset**:
  - The dataset includes essential diamond attributes like:
    - Carat (weight)
    - Cut quality
    - Color grade
    - Clarity
    - Physical dimensions (Depth, Table, Length, Width, Height)
  - These features help the model accurately predict diamond prices based on market-relevant characteristics.

- **Model Training Process**:
  - Multiple regression algorithms were tested, including:
    - **Linear Regression**
    - **Ridge Regression**
    - **Lasso Regression**
    - **ElasticNet**
  - The model was trained and evaluated using metrics such as:
    - **Root Mean Squared Error (RMSE)**
    - **R² Score**
  - The best-performing model was saved and integrated into the app for real-time predictions.
 
 ## Frontend Design

- The app features a clean, user-friendly interface built with HTML, CSS, and JavaScript.
- **Form Validation**: User inputs are validated for required fields and valid ranges.
- **Modal Display**: Predictions are displayed in a popup modal for better user experience.
- **Links to Resources**: Educational and shopping resources are provided to enhance user engagement.

 ## Future Improvements

- **Additional Algorithms**: Experiment with advanced machine learning algorithms to improve prediction performance.
- **Enhanced User Interface**: Include more interactive elements, data visualizations, and real-time insights.
- **User Authentication**: Add authentication for a personalized experience where users can save and compare predictions.

## Contact Information

For questions, feedback, or contributions, please contact:

- **BZIZ Imad** - [LinkedIn](https://www.linkedin.com/in/imad-bziz-97aa80285?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_ap)
- **Youssef Aabbad** - [LinkedIn](https://www.linkedin.com/in/youssef-aabbad-60b1a9297?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)




  
