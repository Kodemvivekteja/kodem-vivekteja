import streamlit as st

# Function to calculate efficiency and copper losses
def Tran_Eff(VA, CL, FCL, K, PF):
    # Calculate the Efficiency (Eff)
    Eff = (K * VA * PF) / (K * VA * PF + CL + (K ** 2) * FCL)
    
    # Calculate the Copper Losses (CUL)
    CUL = (K ** 2) * FCL
    
    # Return the results
    return Eff, CUL

# Streamlit Web Application
st.title("Transformer Efficiency and Copper Losses Calculator")

st.write("""
    This application calculates the efficiency and copper losses of a transformer 
    based on the input parameters:
    - Transformer Rating (VA)
    - Core Losses (CL) in watts
    - Full Load Copper Losses (FCL) in watts
    - Loading on Transformer (K) as a percentage (0 to 1)
    - Power Factor (PF)
""")

# Input Fields for the user to enter the values
VA = st.number_input("Enter the Transformer Rating (VA)", min_value=1.0, step=1.0)
CL = st.number_input("Enter the Core Losses (CL) in Watts", min_value=0.0, step=1.0)
FCL = st.number_input("Enter the Full Load Copper Losses (FCL) in Watts", min_value=0.0, step=1.0)
K = st.number_input("Enter the Loading on Transformer (K) as a fraction (e.g., 0.8)", min_value=0.0, max_value=1.0, step=0.01)
PF = st.number_input("Enter the Power Factor (PF)", min_value=0.0, max_value=1.0, step=0.01)

# When the user clicks the button, perform the calculation
if st.button("Calculate Efficiency and Copper Losses"):
    if VA > 0 and CL >= 0 and FCL >= 0 and 0 <= K <= 1 and 0 <= PF <= 1:
        # Calculate Efficiency and Copper Losses
        Eff, CUL = Tran_Eff(VA, CL, FCL, K, PF)
        
        # Display the results
        st.subheader(f"Calculated Efficiency: {Eff * 100:.2f}%")
        st.subheader(f"Calculated Copper Losses (CUL): {CUL:.2f} watts")
    else:
        st.error("Please enter valid values for all inputs.")

