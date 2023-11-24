import streamlit as st


# The basic information will be displayed from here.

def basics(content_ph) -> None:

    """
    Function for the basic information.
    :param content_ph: The empty Streamlit container for the content.
    :return: None.
    """

    content_ph.empty()
    with content_ph.container():
        st.subheader("Installation Streamlits")
        st.markdown("""Streamlit kann durch folgende Befehle installiert und
        getestet werden:""")

        st.code("pip install streamlit\nstreamlit hello")
        st.markdown("Es sollte sich eine Willkommens-Seite im Browser öffnen.")
        st.divider()

        st.subheader("Aufbau einer Web-Anwendung")
        st.markdown("""Um eine Streamlit-Anwendung zu bauen, sind die erwünschten
        Komponenten (Text, Markdown, Charts, etc., siehe Komponenten) an der
        **jeweiligen Stelle im Code** zu platzieren, wo sie auch später in der
        App zu finden sein sollen.""")
        st.markdown("Das folgende Codestück liefert den entsprechenden Output:")
        st.code("st.text('Erste Zeile')\nst.text('Zweite Zeile')")
        st.text('Erste Zeile')
        st.text('Zweite Zeile')
        st.divider()

        st.markdown("Dieses Codestück erzeugt einen anderen Output:")
        st.code("st.text('Zweite Zeile')\nst.text('Erste Zeile')")
        st.text('Zweite Zeile')
        st.text('Erste Zeile\n')
        st.divider()

        st.markdown("""Sollen manche Komponenten **erzeugt und eventuell wieder
        gelöscht werden** (beispielsweise eine Login-Form), so kann ein **leerer
        Container als Platzhalter** erzeugt werden. Dieser kann beliebig oft
        geleert und mit unterschiedlichsten Komponenten gefüllt werden.""")
        st.code("placeholder = st.empty()")
        st.markdown("Dieser Code erzeugt einen leeren Container.")
        st.markdown("Die 'with'-Notation ermöglicht das Füllen eines Containers.")
        st.code("placeholder.empty()  # zum leeren\n"
                "with placeholder.container():\n"
                "\tst.text('Dieser Text könnte wieder gelöscht werden.')")
        st.divider()

        st.markdown("""Übrigens, der Content-Bereich, welchen Du gerade liest,
        ist auch ein st.empty()-Container. Je nach dem, welchen Tab Du wählst, wird
        der Platzhalter unterschiedlich gefüllt.""")
        st.divider()

        st.subheader("Ausführung eines Streamlit-Scripts")
        st.markdown("""Beim Bau der Web-Applikation ist vor allem der
        **Ausführungsmechanismus Streamlits zu beachten**. Sobald an einer
        interaktiven Komponente (Checkbox, Button, Slider, etc.) Änderungen
        vorgenommen werden (etwas anderes wird ausgewählt, Button wird
        geklickt), startet die Ausführung **der gesamten Anwendung** von vorn!
        Dies ist bei der Konstruktion im Hinterkopf zu behalten.""")
        st.markdown("""Ein Beispiel: ändere die Konfiguration der unten stehenden
        Auswahl und schaue dabei in den rechten oberen Rand des Fensters. Dort
        sollte zu erkennen sein, dass die App läuft und von Neuem beginnt.""")
        st.radio("Wähle :icecream: :pizza: :hamburger: etwas aus:", options=["Eis", "Pizza", "Burger"])
        st.markdown("""Dieser Prozess ist zwar kaum spürbar, kann aber
        Auswirkungen auf Animationen haben. Wird die Animierungsgeschwindigkeit während
        des Ausführens durch einen Slider geändert, so würde die Animation von vorne beginnen.
        Dies ist durch eine Änderung des Codes (if-Statements) abwendbar.""")
        st.markdown("Eine ausführliche Referenz: "
                    "[Streamlit-Session-State](https://docs.streamlit.io/library/api-reference/session-state).")
        st.divider()

        st.subheader("Deploying eines Streamlit-Scripts")
        st.markdown("""Du möchtest Dein erstelltes Streamlit-Script ausführen und Deine
        WebApp begutachten? Gib dazu folgenden Befehl in Deine Konsole ein:""")
        st.code("streamlit run <Scriptname>.py", language="bash")
        st.markdown("Auf Deinem localhost wird die Website zu sehen sein.")
        st.divider()

        st.markdown("""**Streamlit ist nicht schwer zu verstehen, oder? :smile:
        Gehe zum nächsten Tab und schaue Dir ein paar Komponenten an.**""")
        file = open("./custom/button.html")
        st.markdown(file.read(), unsafe_allow_html=True)
        file.close()
        st.markdown("""Das ist übrigens ein eigens gebauter HTML-Button.
        Auch die Einbindung eigenen HTML-Codes ist in Streamlit möglich. :wink:""")
