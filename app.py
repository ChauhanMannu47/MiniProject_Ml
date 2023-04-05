 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache_data()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married,Dependents,Education,EmploymentStatus, ApplicantIncome,CoApplicantIncome, LoanAmount, LoanAmountTerm, Credit_History,PropertyStatus):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1

    if Dependents == "0":
        Dependents=1
    elif Dependents == "1":
        Dependents=1
    elif Dependents == "2":
        Dependents=3
    else:
        Dependents=4

    if Education == "Graduate":
        Education = 1
    else:
        Education=0
    
    if EmploymentStatus=="Yes":
        EmploymentStatus=1
    else:
        EmploymentStatus=0
    

 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  

    if PropertyStatus == "Urban":
        PropertyStatus=1
    elif PropertyStatus == "Semi-Urban":
        PropertyStatus=2
    else:
        PropertyStatus=3
 
    # LoanAmount = LoanAmount / 1000
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married,Dependents,Education,EmploymentStatus, ApplicantIncome,CoApplicantIncome, LoanAmount, LoanAmountTerm, Credit_History,PropertyStatus]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    Dependents=st.selectbox('Dependents',("0","1","2","3+"))
    Education=st.selectbox('Education Status',("Graduate","Not Graduate"))
    EmploymentStatus=st.selectbox('EmploymentStatus',("Yes","No"))
    ApplicantIncome = st.number_input("Applicants monthly income") 
    CoApplicantIncome = st.number_input("CoApplicants monthly income")
    LoanAmount = st.number_input("Total loan amount")
    LoanAmountTerm  = st.number_input("Enter Loan Amount Term")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    PropertyStatus=st.selectbox('Type Of Property',("Urban","Semi-Urban","Rural"))

    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married,Dependents,Education,EmploymentStatus, ApplicantIncome,CoApplicantIncome, LoanAmount, LoanAmountTerm, Credit_History,PropertyStatus) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()
