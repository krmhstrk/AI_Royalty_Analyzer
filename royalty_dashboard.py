# English: Import necessary libraries
# Deutsch: Notwendige Bibliotheken importieren
import streamlit as st
import pandas as pd
import plotly.express as px # For interactive charts

# --- Page Configuration (English & German) ---
# English: Set page title, icon, and layout. This should be the first Streamlit command.
# Deutsch: Seitentitel, Icon und Layout festlegen. Dies sollte der erste Streamlit-Befehl sein.
st.set_page_config(page_title="Royalty Dashboard", page_icon="🎵", layout="wide")

# --- Language Selection (English & German) ---
# English: Add a language selection in the sidebar for UI text.
# Deutsch: Sprachauswahl in der Seitenleiste für UI-Texte hinzufügen.
language_options = {
    "English": "en",
    "Deutsch (German)": "de"
}
# English: Use a key that won't cause issues if the user's system uses a different default language for display
# Deutsch: Verwenden Sie einen Schlüssel, der keine Probleme verursacht, wenn das System des Benutzers eine andere Standardsprache für die Anzeige verwendet
selected_language_key = st.sidebar.radio("Select Language | Sprache wählen:", list(language_options.keys()))
LANG = language_options[selected_language_key]

# --- Text Translations for UI elements ---
# English: A simple dictionary for UI text elements to support multiple languages.
# Deutsch: Ein einfaches Dictionary für UI-Textelemente zur Unterstützung mehrerer Sprachen.
texts = {
    "en": {
        "title": "🎵 Interactive Royalty Analysis Dashboard",
        "uploader_label": "Upload your Royalty Report Data (CSV file):",
        "data_not_loaded": "Please upload a CSV file to see the analysis. Using sample data for now.",
        "show_data_button": "Show Raw Data",
        "summary_header": "📊 Data Summary",
        "total_revenue": "Total Reported Revenue (Publisher USD):",
        "total_writer_share": "Total Calculated Writer Share (USD):",
        "total_discrepancy": "Total Discrepancy (USD):",
        "charts_header": "📈 Visualizations",
        "revenue_by_song": "Revenue by Song Title",
        "discrepancy_by_song": "Discrepancy by Song Title",
        "revenue_by_type": "Revenue by Royalty Type",
        "filter_song": "Filter by Song Title(s):",
        "filter_type": "Filter by Royalty Type(s):",
        "footer_text": "Portfolio Project - AI Royalty Analyzer"
    },
    "de": {
        "title": "🎵 Interaktives Dashboard zur Lizenzgebührenanalyse",
        "uploader_label": "Laden Sie Ihre Lizenzgebührenberichtsdaten (CSV-Datei) hoch:",
        "data_not_loaded": "Bitte laden Sie eine CSV-Datei hoch, um die Analyse anzuzeigen. Vorerst werden Beispieldaten verwendet.",
        "show_data_button": "Rohdaten anzeigen",
        "summary_header": "📊 Datenübersicht",
        "total_revenue": "Gesamte gemeldete Einnahmen (Verlag USD):",
        "total_writer_share": "Gesamter berechneter Autorenanteil (USD):",
        "total_discrepancy": "Gesamtdiskrepanz (USD):",
        "charts_header": "📈 Visualisierungen",
        "revenue_by_song": "Einnahmen nach Songtitel",
        "discrepancy_by_song": "Diskrepanz nach Songtitel",
        "revenue_by_type": "Einnahmen nach Lizenzart",
        "filter_song": "Nach Songtitel(n) filtern:",
        "filter_type": "Nach Lizenzart(en) filtern:",
        "footer_text": "Portfolio-Projekt - KI Lizenzgebühren-Analysator"
    }
}

# --- Main Title ---
st.title(texts[LANG]["title"])

# --- Data Loading Section ---
# English: Allow user to upload a CSV file.
# Deutsch: Benutzer erlauben, eine CSV-Datei hochzuladen.
uploaded_file = st.sidebar.file_uploader(texts[LANG]["uploader_label"], type=["csv"])

df = None # Initialize df
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("File uploaded successfully! | Datei erfolgreich hochgeladen!")
    except Exception as e:
        st.sidebar.error(f"Error reading file: {e} | Fehler beim Lesen der Datei: {e}")
else:
    # English: If no file is uploaded, try to load the sample data by default.
    # Deutsch: Wenn keine Datei hochgeladen wird, versuchen Sie standardmäßig, die Beispieldaten zu laden.
    try:
        # English: Make sure 'sample_royalty_data.csv' is in the same directory as the script,
        # English: or provide the full path.
        # Deutsch: Stellen Sie sicher, dass 'sample_royalty_data.csv' sich im selben Verzeichnis wie das Skript befindet,
        # Deutsch: oder geben Sie den vollständigen Pfad an.
        df = pd.read_csv("sample_royalty_data.csv")
        st.info(texts[LANG]["data_not_loaded"])
    except FileNotFoundError:
        st.error("Sample data file ('sample_royalty_data.csv') not found. Please upload a file. | Beispieldatendatei ('sample_royalty_data.csv') nicht gefunden. Bitte laden Sie eine Datei hoch.")
        st.stop() # Stop execution if sample data is not found and no file is uploaded
    except Exception as e:
        st.error(f"Error reading sample data: {e} | Fehler beim Lesen der Beispieldaten: {e}")
        st.stop()


# --- Main Analysis Area (only if DataFrame is loaded) ---
if df is not None and not df.empty:
    # English: Basic data validation for expected columns.
    # Deutsch: Grundlegende Datenvalidierung für erwartete Spalten.
    expected_cols = ['Song Title', 'Reported Revenue (Publisher USD)', 'Calculated Writer Share (USD)', 'Discrepancy (USD)', 'Royalty Type']
    if not all(col in df.columns for col in expected_cols):
        missing_cols = [col for col in expected_cols if col not in df.columns]
        st.error(f"The CSV is missing expected columns: {', '.join(missing_cols)}. Please ensure your CSV has: {', '.join(expected_cols)}")
        # Deutsch: Die CSV-Datei enthält nicht die erwarteten Spalten: {', '.join(missing_cols)}. Bitte stellen Sie sicher, dass Ihre CSV-Datei folgende Spalten enthält: {', '.join(expected_cols)}
    else:
        # --- Show/Hide Raw Data ---
        if st.sidebar.checkbox(texts[LANG]["show_data_button"], False):
            st.subheader("Raw Data | Rohdaten")
            st.dataframe(df)

        # --- Filters in the Sidebar ---
        st.sidebar.header("Filters | Filter")
        unique_songs = sorted(df['Song Title'].unique())
        selected_songs = st.sidebar.multiselect(texts[LANG]["filter_song"], unique_songs, default=unique_songs)

        unique_royalty_types = sorted(df['Royalty Type'].unique())
        selected_royalty_types = st.sidebar.multiselect(texts[LANG]["filter_type"], unique_royalty_types, default=unique_royalty_types)

        # Apply filters
        filtered_df = df[df['Song Title'].isin(selected_songs) & df['Royalty Type'].isin(selected_royalty_types)]

        if filtered_df.empty:
            st.warning("No data matches your current filter selection. | Keine Daten entsprechen Ihrer aktuellen Filterauswahl.")
        else:
            # --- Summary Metrics ---
            st.header(texts[LANG]["summary_header"])
            total_revenue = filtered_df['Reported Revenue (Publisher USD)'].sum()
            total_writer_share = filtered_df['Calculated Writer Share (USD)'].sum()
            total_discrepancy = filtered_df['Discrepancy (USD)'].sum()

            col1, col2, col3 = st.columns(3)
            col1.metric(texts[LANG]["total_revenue"], f"${total_revenue:,.2f}")
            col2.metric(texts[LANG]["total_writer_share"], f"${total_writer_share:,.2f}")
            col3.metric(texts[LANG]["total_discrepancy"], f"${total_discrepancy:,.2f}", delta_color="inverse" if total_discrepancy != 0 else "off")

            # --- Visualizations ---
            st.header(texts[LANG]["charts_header"])

            # Chart 1: Revenue by Song Title
            fig_revenue_song = px.bar(
                filtered_df.groupby('Song Title')['Reported Revenue (Publisher USD)'].sum().reset_index(),
                x='Song Title',
                y='Reported Revenue (Publisher USD)',
                title=texts[LANG]["revenue_by_song"],
                labels={'Reported Revenue (Publisher USD)': 'Revenue (USD)'}
            )
            st.plotly_chart(fig_revenue_song, use_container_width=True)

            # Chart 2: Discrepancy by Song Title
            fig_discrepancy_song = px.bar(
                filtered_df.groupby('Song Title')['Discrepancy (USD)'].sum().reset_index(),
                x='Song Title',
                y='Discrepancy (USD)',
                title=texts[LANG]["discrepancy_by_song"],
                labels={'Discrepancy (USD)': 'Discrepancy (USD)'},
                color='Discrepancy (USD)',
                color_continuous_scale=px.colors.diverging.RdYlGn_r
            )
            st.plotly_chart(fig_discrepancy_song, use_container_width=True)

            # Chart 3: Revenue by Royalty Type (Pie Chart)
            fig_revenue_type_pie = px.pie(
                filtered_df.groupby('Royalty Type')['Reported Revenue (Publisher USD)'].sum().reset_index(),
                names='Royalty Type',
                values='Reported Revenue (Publisher USD)',
                title=texts[LANG]["revenue_by_type"]
            )
            st.plotly_chart(fig_revenue_type_pie, use_container_width=True)
elif df is not None and df.empty:
    st.warning("The uploaded/sample CSV file is empty. | Die hochgeladene/Beispiel-CSV-Datei ist leer.")


# --- Footer ---
st.markdown("---")
st.markdown(f"<p style='text-align: center;'>{texts[LANG]['footer_text']}</p>", unsafe_allow_html=True)
