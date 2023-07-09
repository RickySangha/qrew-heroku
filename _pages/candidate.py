import streamlit as st
from pyairtable import Table
from pyairtable.formulas import match
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

AIRTABLE_KEY = os.environ["AIRTABLE_API_KEY"]


def load_candidate_details(name):
    table = Table(
        api_key=AIRTABLE_KEY, base_id="appNHbOjDXpsU37JE", table_name="Candidates"
    )
    formula = match({"Name": name})
    candidate = table.first(formula=formula)
    return candidate


def go_back():
    st.session_state._page = "Form"


def display_candidate():
    col1, col2 = st.columns([0.2, 0.8])
    col1.button(label="Back", on_click=go_back)
    col2.header("Candidate :green[Details]", anchor=False)
    st.divider()

    candidate = load_candidate_details(st.session_state.candidate_name)

    st.subheader(candidate["fields"]["Name"], anchor=False)
    st.write(f'Country: {candidate["fields"]["Country"]}')
    st.write(f'Email: {candidate["fields"]["Email"]}')
    st.write(f'Phone: {candidate["fields"]["Phone"]}')
    st.divider()

    st.subheader(":green[Skills]", anchor=False)
    skills = candidate["fields"]["Skills"]
    skills_cols = st.columns(len(skills))
    st.write(skills)
    # for i, skill in enumerate(skills):
    #     skills_cols[i].write(skill)
    st.divider()

    st.subheader(":green[Computer Skills]", anchor=False)
    comp_skills = candidate["fields"]["Computer Skills"]
    comp_skills_cols = st.columns(len(comp_skills))
    st.write(comp_skills)
    # for i, comp_skill in enumerate(comp_skills):
    #     comp_skills_cols[i].write(comp_skill)
    st.divider()

    st.subheader(":green[Summary]", anchor=False)
    st.write(candidate["fields"]["Career Summary"])
