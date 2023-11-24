import streamlit as st


# Script for additional information.

def additional(content_ph) -> None:

    """
    Function for the additional information.
    :param content_ph: The empty Streamlit container for the content.
    :return: None.
    """

    # markdown settings changed
    st.markdown('''
        <style>
            [data-testid="stMarkdownContainer"] ul{
                padding-left:40px;
            }
        </style>
    ''', unsafe_allow_html=True)

    st.header("Weiterführende Links")
    st.markdown("""Diese Seite sollte Dir einen kleinen Einblick
    in das Package Streamlit geben. Ich hoffe, sie hat Dir geholfen. :-)""")
    st.markdown("**Diese Links könnten Dir helfen**:")
    st.markdown("- [Offizielle Streamlit-Seite :crown:](https://streamlit.io/)")
    st.markdown("- [Streamlit-Cloud :cloud:](https://streamlit.io/cloud)")
    st.markdown("- [Kostenlose Streamlit-Erweiterungen :heavy_plus_sign:](https://streamlit.io/components)")
