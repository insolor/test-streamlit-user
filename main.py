import streamlit as st

if not st.user:
    st.error(
        "Identity provider not configured. "
        "See [User authentication](https://docs.streamlit.io/develop/concepts/connections/authentication)"
    )
    st.stop()

if not st.user.is_logged_in:
    st.button("Log in with Google", on_click=st.login)
    st.stop()

st.button("Log out", on_click=st.logout)
st.markdown(f"Welcome! {st.user}")
