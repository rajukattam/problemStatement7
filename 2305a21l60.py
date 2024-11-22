#creating a oc transformer model
import streamlit as st
import math as m 

st.markdown('<h1>Open circut transformer efficiency</h1>',unsafe_allow_html=True)

with st.form('form2'):
    col1,col2,col3=st.columns(3)
    V0=st.number_input('V0(V)')
    I0=st.number_input('I0(A)')
    W0=st.number_input('W0(W)')
    if V0 and I0 == 0:
        st.write('invalid inputs')
    submitted=st.form_submit_button('compute')

if submitted:
    cos0 = W0/(V0*I0)
    sin0 = m.sqrt(1-cos0**2)
    Iw = I0 * cos0
    Iu = I0 * sin0
    if V0 and I0 != 0:
        R0 = V0 / Iw
        X0 = V0 / Iu
        st.write('R0:',R0,'ohm')
        st.write('X0:',X0,'ohm')
    
    
    