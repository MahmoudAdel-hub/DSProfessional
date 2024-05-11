import streamlit as st
import joblib
from xgboost import XGBClassifier
import numpy as np



def predict(point1):
    for _ in point1[0][:5]:
        if _ < 0:
            raise ValueError("Please enter positive values for calories, carbohydrate, sugar, and servings.")
    
    mo = 0
    for _1 in point1[0][4:]:
        if _1 <= 1 and _1 >= 0:
            mo += _1
            
        elif _1 > 1:
            raise ValueError("Please enter 1 for the recipe category, and 0 if not.")
            break
    
    if mo == 1:
        model = joblib.load('recipe.pkl')
        # Make your prediction using the loaded model
        # Replace the next line with your prediction logic
        prediction = model.predict(point1)  # Placeholder prediction
        
        return prediction
    
    elif mo == 0:
        raise ValueError("Please choose only one category.")
        


def main(): 
    st.title("Recipe Traffic Predictor")
    html_temp = """
    <style>
       .stApp {
        color: white;
    }
    .prediction-box {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 15px;
        margin-top: 20px;
    }
    .estimate {
        font-weight: bold;
    }
    .bound {
        margin-top: 5px;
    }
    </style>
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">House Price Predictor App </h2>
    </div>
    """

    calories = int(st.text_input("calories", "0")) 
    carbohydrate = int(st.text_input("carbohydrate", "0")) 
    sugar = int(st.text_input("sugar", "0")) 
    protein = int(st.text_input("protein", "0")) 
    servings = int(st.text_input("servings", "0")) 
    category_Breakfast = int(st.text_input("category_Breakfast", "0"))
    category_Chicken = int(st.text_input("category_Chicken", "0"))
    category_Dessert = int(st.text_input("category_Dessert", "0"))
    category_Lunch_Snacks = int(st.text_input("category_Lunch/Snacks", "0"))
    category_Meat = int(st.text_input("category_Meat", "0"))
    category_One_Dish_Meal = int(st.text_input("category_One Dish Meal", "0"))
    category_Pork = int(st.text_input("category_Pork", "0"))
    category_Potato = int(st.text_input("category_Potato", "0"))
    category_Vegetable = int(st.text_input("category_Vegetable", "0"))
    
    
    point = np.array([[calories, carbohydrate, sugar, servings, category_Breakfast,
       category_Chicken, category_Dessert, category_Lunch_Snacks,
       category_Meat, category_One_Dish_Meal, category_Pork,
       category_Potato, category_Vegetable, 0]])

        
    if st.button("Predict"): 

        prediction = predict(point)

        if prediction == 1   :         
            st.success('Great Recipe !')
        else :
            st.success('Not Great Recipe !')        
        

if __name__ == '__main__': 
    # Run Streamlit app
    main()
