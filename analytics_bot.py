from openai import OpenAI
import pandas as pd
import test_key as tk

# Set up your OpenAI API key; import secret key from another file
client = OpenAI(api_key=tk.secret_key)

def analyze_excel_file(file_path):
    """
    Analyzes an Excel file using OpenAI's GPT-4o-mini model.

    Args:
        file_path (str): The path to the Excel file.

    Returns:
        str: The response from OpenAI containing insights on the data columns.
    """
    # Read the Excel file
    data_frame = pd.read_csv('data.csv')
    
    # Convert the DataFrame to a string format that can be processed by the API
    data_string = data_frame.to_string(index=False)
    
    # Call the OpenAI API to analyze the data
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=2000,
        messages=[
            {"role": "system", "content": "You are a data analytics expert in the fintech industry. "
                                           "Your detailed knowledge and understanding of the industry, along with specific insights on "
                                           "metrics and analytics, can greatly help a company in deciding if loan applications should be approved or not. "
                                           "You are good at providing specific numbers, percentages, and brief reasons for these metrics. "},
            {"role": "user", "content": f"Based on the data shared with you, analyze the data to provide insights on the different columns of data. "
                                       f"The columns of data include: Gender (male or female), Married (yes or no), dependents (0, 1, 2, 3+), "
                                       f"Education (graduate or not graduate), Self_Employed (yes or no), Applicant_Income (integer), "
                                       f"Coapplicant_Income (integer), Loan_Amount (integer), Loan_Length_Months (integer), Credit_History (yes or no), "
                                       f"Property_Area (urban, rural, semiurban), Loan_Approved (yes or no). Share descriptive statistics and metrics."}
        ]
    )
    
    # Extract and return the response from OpenAI
    return response.choices[0].message.content


# Main function to demonstrate the use
if __name__ == "__main__":
    # Replace with your local Excel file path
    file_path = "data.csv"

    analysis = analyze_excel_file(file_path)
    print("Analysis Result:")
    print(analysis)


