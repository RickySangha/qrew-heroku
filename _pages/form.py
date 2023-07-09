import streamlit as st


def get_candidates(query, num):
    if query:
        memory = st.session_state.memory
        instructor_embeddings = st.session_state.instructor_embeddings
        return memory.get_relavent(
            query=query, index_name="resumes", embedding=instructor_embeddings, num=num
        )


def set_page(name):
    st.session_state._page = "Candidate"
    st.session_state.candidate_name = name


def display_form():
    st.title(":green[Qrew] Candidate Finder :sunglasses:", anchor=False)

    form = st.form(key="form")
    num = form.number_input(
        "Number of results to return", value=1, min_value=1, max_value=10
    )
    query = form.text_area(
        label="query", placeholder="Enter the job description", key="job_description"
    )
    submitted = form.form_submit_button(label="Search")
    if submitted:
        candidates = get_candidates(query=query, num=num)
        st.subheader("Candidates found in order of relevance:", anchor=False)
        for i, candidate in enumerate(candidates):
            candidate_name = candidate.metadata["Name"]
            expander = st.expander(f'{i+1} - {candidate.metadata["Name"]}')
            expander.write(candidate.page_content)
            expander.divider()
            col1, col2 = expander.columns([0.7, 0.3])
            col1.write("Retrieve more details on this candidate")
            col2.button(
                label="More Details",
                key=i,
                use_container_width=True,
                on_click=set_page,
                kwargs={"name": candidate_name},
            )
