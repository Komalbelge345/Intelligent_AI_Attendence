import streamlit as st
from src.components.header_home import header_dashboard
from src.ui.base_layout import style_backgroud_dashboard
from src.ui.base_layout import style_base_layout
from src.components.footer import footer_dashboard
from src.database.db import create_teacher
from src.database.db import check_teacher_exits,teacher_login
def teacher_screen():
   
    style_backgroud_dashboard()
    style_base_layout()
    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()

    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()

def login_teacher(username,password):
    if not username or not password:
        return False
    teacher = teacher_login(username,password)
    if teacher:
        st.session_state.user_role ='teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in=True
        return True

    return False
def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"""Welcome ,{teacher_data['name']}""")
         
def teacher_screen_login():
        c1,c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    
        with c1:
            header_dashboard()
    
        with c2:
           if st.button("Go back to Home",key="loginbackbtn",shortcut="Ctrl+Backspace",width='stretch') :
                st.session_state['login_type']=None
          
                st.rerun() 

        st.header('Login using password',text_alignment='center')
        st.space()
        st.space()
        teacher_username = st.text_input("Enter username",placeholder='komalbelge')
        teacher_password = st.text_input("Enter password",type='password',placeholder="Enter password")

        st.divider()

        btnc1,btnc2 = st.columns(2)

        with btnc1:
            if st.button("Login",icon=':material/passkey:',shortcut="Ctrl+Backspace",width='stretch'):
                if login_teacher(teacher_username,teacher_password):
                    st.toast("welcome back!",icon="👋")
                    import time
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid username and password!")

        with btnc2:  
            if st.button("Register Instead",icon=':material/passkey:',type="primary",width='stretch'):
                st.session_state['teacher_login_type']="register"



        footer_dashboard() 



def register_teacher(teacher_username,teacher_name,teacher_password,teacher_confirm_password):
    if not teacher_username or not teacher_password or not teacher_confirm_password:
        return  False,"All Fields are required!"

    if check_teacher_exits(teacher_username):
        return False,"Username already taken"

    if(teacher_password!=teacher_confirm_password):
        return False,"Password doesn't match"
    try:
        create_teacher(teacher_username,teacher_password,teacher_name)
        return True,"Sucessfully Created! Login Now"
    except Exception as e:
        return False,"Unexpected Error!"
def teacher_screen_register():

        c1,c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    
        with c1:
            header_dashboard()
    
        with c2:
            if st.button("Go back to Home",key="loginbackbtn",shortcut="Ctrl+Backspace") :
                st.session_state['login_type']=None  

                st.rerun()  
        st.header('register your teacher profile',text_alignment='center')
        st.space()
        st.space()
        teacher_username = st.text_input("Enter username",placeholder='komalbelge',key='username')
        teacher_name = st.text_input("Enter name",placeholder='komalbelge',key='name')
        teacher_password = st.text_input("Enter password",type='password',placeholder="Enter password",key='password')
        teacher_confirm_password = st.text_input("Enter password",type='password',placeholder="Enter password",key='confirmpassword')
        
        st.divider()
        
        btnc1,btnc2 = st.columns(2)
        
        with btnc1:
            if st.button("Register Now",icon=':material/passkey:',type="primary",shortcut="Ctrl+Backspace",width='stretch'):
                success,message = register_teacher(teacher_username,teacher_name,teacher_password,teacher_confirm_password)
                if success:
                    st.success(message)
                    import time 
                    time.sleep(2)
                    st.session_state['teacher_login_type']='login'
                    st.rerun()

                else:
                    st.error(message)    

        with btnc2:  
            if st.button("Login Instead",icon=':material/passkey:',width='stretch'):
                st.session_state['teacher_login_type']='login'
        
        
        footer_dashboard()   
         