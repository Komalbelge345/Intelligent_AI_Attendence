import streamlit as st
import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector



    sp =


    facerec=