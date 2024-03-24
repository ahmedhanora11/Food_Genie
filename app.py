# app.py
from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key
genai.configure(api_key=os.environ["API_KEY"])

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calorie_calc')
def calorie_calc():
    return render_template('calorie_calc.html')

@app.route('/food_donation')
def food_donation():
    return render_template('food_donation.html')


@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    calorie_prompt = request.form['calorie']
    vitamins_prompt = request.form['vitamins']  # Retrieve the new prompt for vitamins and proteins
    meals_prompt = request.form['meals']
    storage_prompt = request.form['storage']
    height_prompt = request.form['height']
    weight_prompt = request.form['weight']
    age_prompt = request.form['age']

    # Build the full prompt
    full_prompt = f"Main prompt: {prompt}"
    if calorie_prompt:
        full_prompt += f"\nWhat is the calorie of {calorie_prompt}"
    if vitamins_prompt:
        full_prompt += f"\nWhat are the vitamins and proteins in {vitamins_prompt} in a simple way"
    if meals_prompt:
        full_prompt += f"\nProvide healthy meals that includes: {meals_prompt}"
    if storage_prompt:
        full_prompt += f"\nhow to store {storage_prompt} in my kitchen so it stays fresh for the longest time possible, make it simple not many words"
    if height_prompt:
        full_prompt += f"\nCalculate the daily needed calorie intake for height {height_prompt} cm , weight {weight_prompt} kg, and age {age_prompt} years old"

    
    response = model.generate_content(full_prompt)
    generated_text = response.text
    return render_template('result.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
