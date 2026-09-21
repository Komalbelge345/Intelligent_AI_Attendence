import streamlit as st
import numpy as np
from src.components.header_home import header_dashboard
from src.ui.base_layout import style_backgroud_dashboard
from src.ui.base_layout import style_base_layout
from src.components.footer import footer_dashboard

from PIL import Image
def student_screen():
    style_backgroud_dashboard()
    style_base_layout()
    c1,c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
        
    with c1:
                header_dashboard()
        
    with c2:
        if st.button("Go back to Home",key="loginbackbtn",shortcut="Ctrl+Backspace",width='stretch') :
            st.session_state['login_type']=None
              
            st.rerun() 
    
    st.header('Login using FaceID',text_alignment='center')
    st.space()
    st.space()

    
    photo_source = st.camera_input("Position your face in the center")
    if photo_source:
        np.array(Image.open(photo_source))
    footer_dashboard() 