import streamlit as st
from streamlit.components.v1 import html


# An overview over some Streamlit components.


def clicked():
    st.balloons()
    st.markdown("""
    <script>
        windows.location.assign('https://overview.streamlit.app/#interaktive-widgets')
    </script>""", unsafe_allow_html=True)


def components(content_ph) -> None:

    """
    Function that displays the overview.
    :param content_ph: The empty Streamlit container for the content.
    :return: None.
    """

    content_ph.empty()
    with content_ph.container():

        st.markdown("""Streamlit bietet eine **Vielzahl von bereits eingebauten
        Komponenten**. Eine Auswahl soll im Folgenden dargestellt und erläutern werden.""")
        st.markdown("""Natürlich stellen die folgenden Abschnitte nur eine **Auswahl**
        dar. Um eine (nahezu) komplette Übersicht, über alle eingebauten Widgets zu bekommen,
        klicke bitte diesen Button:""")
        file = open("./custom/component_button.html")
        with st.columns(5)[2]:  # workaround to center the button (another approach below)
            st.markdown(file.read(), unsafe_allow_html=True)
        file.close()
        st.divider()

        st.subheader("Text-Komponenten")
        st.markdown("""Um Textelemente darstellen zu können, bietet
        Streamlit bereits eine umfassende Sammlung an Funktionen.""")

        st.code("st.text('Das ist ein erster Test.')")
        st.markdown("""Mit Hilfe dieses einfachen Commands kann einfacher Text dargestellt
                    werden. Das Ergebnis dieses Codestückes wäre:""")
        st.text('Das ist ein erster Test.')

        st.markdown("""Um die äußere Form des Textes ansprechender zu machen,
        können folgende Methoden genutzt werden:""")
        st.code("""st.write('Besserer Text')\nst.markdown('Text mit *Markdown*')""")
        st.write('Besserer Text')
        st.markdown('Text mit *Markdown*')

        st.markdown("""Absätze und Titel können wie folgt eingefügt werden:""")
        st.code("st.header('Titel)\nst.subheader('Absatz')")

        st.markdown("Auch LaTeX-Code kann eingefügt werden:")
        st.code(r"st.latex('\sum_{i=1}^{n}{i} = \frac{n(n+1)}{2}')")
        st.latex(r"\sum_{i=1}^{n}{i} = \frac{n(n+1)}{2}")
        st.divider()

        st.header("Verwendung von Spalten")
        st.markdown("Auch die Nutzung von Spalten wird unterstützt.")
        st.code("c1, c2 = st.columns(2)")
        c1, c2 = st.columns(2)
        c1.markdown("Dieser Code erstellt")
        c2.markdown("zwei gleich große Spalten.")
        st.markdown("Oder aber:")
        st.code("c1, c2, c3 = st.columns([1, 1, 3])")
        c1, c2, c3 = st.columns([1, 1, 3])
        c1.markdown("Dieser Code")
        c2.markdown("erstellt drei")
        c3.markdown("verschieden breite Spalten, wie zu sehen ist.")
        st.divider()

        st.header("Interaktive Widgets")
        st.markdown("Im Folgenden sollen einige interaktive Komponenten vorgestellt werden.")
        st.text("\n")

        st.markdown("Versuche Doch mal, folgenden Knopf zu drücken und schaue, was passiert.")
        st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Koulen&family=Lato&family=Nunito&family=Playfair+Display:ital@1&family=Prata&family=Raleway:ital,wght@1,100&family=Roboto&family=Roboto+Condensed&family=Teko&display=swap');
            .row-widget.stButton {text-align: center;}
            div.stButton > button:first-child {
                font-family: Roboto, sans-serif;
                font-size: 14px;
                color: #fff;
                background-color: #48cae4;
                padding: 10px 30px;
                border: solid #264653 3px;
                box-shadow: rgb(0, 0, 0) 0px 0px 0px 0px;
                border-radius: 10px;
                transition : 100ms;
                cursor: pointer;
            }
            div.stButton > button:first-child:hover {
                transition : 100ms;
                padding: 10px 33px;
                background-color: #48cae0;
                color: #264653;
                border: solid 3px #264653;
            }
        </style>
        """, unsafe_allow_html=True)
        st.button("Click me!", on_click=clicked)
        st.markdown("Ein Button kann mit folgendem Code eingefügt werden:")
        st.code("st.button('Click me!')")
        st.markdown("*Hinweis*: Dieser Button wurde mit CSS-Code künstlich verändert.")
        st.divider()

        st.code("value = st.slider(label='Wähle einen Wert:', min_value=1, max_value=10)")
        value = st.slider(label="Wähle einen Wert:", min_value=1, max_value=10)
        st.markdown("Damit kann ein Slider erzeugt werden.")
        st.markdown(f"Der Wert wird in *value* gespeichert und beträgt: **{value}**.")
        st.divider()

        st.markdown("""Um zwischen verschiedenen Möglichkeiten auszuwählen,
        stehen select-Boxen bereit.""")
        st.code('value = st.selectbox("Wähle einen Wert:", options=["1", "2", "3"])')
        value = st.selectbox("Wähle einen Wert:", options=["1", "2", "3"])
        st.markdown(f"Du hast **{value}** gewählt.")
        st.divider()

        st.markdown("""Auch radio-Boxen stehen zur Verfügung:""")
        st.code('''option = st.radio("Wähle :icecream: :pizza: :hamburger: etwas aus:",
                          options=["Eis", "Pizza", "Burger"])''')
        option = st.radio("Wähle :icecream: :pizza: :hamburger: etwas aus:",
                          options=["Eis", "Pizza", "Burger"])
        st.markdown(f"Das beste Gericht ist: **{option}**")
        st.divider()

        st.header("Sidebar")
        st.markdown("""Auch eine Sidebar lässt sich mit Streamlit implementieren.
                    Die 'with'-Notation ermöglicht eine Verwendung, die sich von der
                    herkömmlichen Streamlit-Notation kaum unterscheidet.""")
        st.code('''with st.sidebar:
            \tst.markdown("Hier könnte Ihre Werbung stehen.")''')
        with st.sidebar:
            st.markdown("Hier könnte Ihre Werbung stehen.")
            st.markdown("Auch hier können **alle** Streamlit-Komponenten eingebaut "
                        "werden. Isn't that great?")
        st.divider()

        st.markdown("Hiermit geht's wieder hoch!")
        st.markdown(open("./custom/button.html").read(), unsafe_allow_html=True)
