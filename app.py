import streamlit as st
import extra_streamlit_components as stx
from tabs.basics import basics
from tabs.components import components
from tabs.additional import additional


# This is the main script from which the presentation app will be running from.

def app() -> None:

    """
    This is the main app-function.
    :return: None.
    """

    st.title(":blue[Streamlit Overview]")

    st.header("Eine Übersicht über Streamlit")
    st.markdown("""Streamlit ist eine Python-Bibliothek beziehungsweise ein Python-Framework
    mit dem es möglich sein soll, Web-Applikationen in **kurzer Zeit** und
    **ohne Frontend-Erfahrung** zu bauen.""")
    st.markdown("""Streamlit ist primär ausgelegt auf data-science-Anwendungen,
    kann aber auch zu jedem anderen (vergleichbaren) Zweck gebraucht werden.""")
    st.markdown("""Wähle eine der folgenden Registerkarten aus und
    erfahre mehr über die Funktionen Streamlits.""")

    tab_id = stx.tab_bar(data=[
        stx.TabBarItemData(id=1, title="Basics", description="grundlegende Funktionen"),
        stx.TabBarItemData(id=2, title="Komponenten", description="weitere Widgets"),
        stx.TabBarItemData(id=3, title="Informationen", description="weitere Infos")
    ], default=1)
    st.divider()

    content_ph = st.empty()
    if tab_id == "1":
        basics(content_ph)
    elif tab_id == "2":
        components(content_ph)
    elif tab_id == "3":
        additional(content_ph)
    else:
        st.error("Etwas unvorhersehbares ist geschehen! Versuche, die Seite neu zu laden.")


if __name__ == "__main__":
    app()
