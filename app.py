import streamlit as st
from langchain.embeddings import HuggingFaceInstructEmbeddings
from memory import get_memory
from _pages.form import display_form
from _pages.candidate import display_candidate
import os


@st.cache_resource
def set_up():
    # Initialization
    if "memory" not in st.session_state:
        st.session_state.memory = get_memory()
    if "instructor_embeddings" not in st.session_state:
        cwd = os.getcwd()
        st.session_state.instructor_embeddings = HuggingFaceInstructEmbeddings(
            model_name=f"{cwd}/embeddings/hkunlp_instructor-xl",
            model_kwargs={"device": "cpu"},
            cache_folder="embeddings",
        )


def set_initial_state():
    if "_page" not in st.session_state:
        st.session_state._page = "Form"


st.set_page_config(page_title="Qrew")

set_up()
set_initial_state()

if st.session_state._page == "Form":
    display_form()
else:
    display_candidate()


# TOOD: add page to view full candidate profile. Profile to be pulled from airtable.
