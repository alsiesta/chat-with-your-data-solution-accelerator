import streamlit as st
import os
import logging
import sys
from dotenv import load_dotenv
from azure.monitor.opentelemetry import configure_azure_monitor


load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

logging.captureWarnings(True)
logging.basicConfig(level=os.getenv("LOGLEVEL", "INFO").upper())
# Raising the azure log level to WARN as it is too verbose - https://github.com/Azure/azure-sdk-for-python/issues/9422
logging.getLogger("azure").setLevel(os.environ.get("LOGLEVEL_AZURE", "WARN").upper())
# We cannot use EnvHelper here as Application Insights needs to be configured first
# for instrumentation to work correctly
if os.getenv("APPINSIGHTS_ENABLED", "false").lower() == "true":
    configure_azure_monitor()

logger = logging.getLogger(__name__)
logger.debug("Starting admin app")


st.set_page_config(
    page_title="Admin",
    page_icon=os.path.join("images", "favicon.ico"),
    layout="wide",
    menu_items=None,
)

mod_page_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(mod_page_style, unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.image(os.path.join("images", "logo.png"))

st.write("# Chatting Sie mit Ihren eigenen Daten.")

st.write(
    """
         * Verwenden Sie den Tab `Daten hochladen`, wenn Sie neue Daten (PDFs, Websites usw.) aufnehmen möchten.
         * Mit `Daten erkunden` erfahren Sie, wie Ihre Daten segmentiert wurden.
         * Klicken Sie auf `Daten löschen` und diese werden gelöscht.
         * Nutzen Sie den Tab `Konfiguration`, um die zugrundeliegenden Eingabeaufforderungen, Protokollierungseinstellungen und andere Details anzupassen.
         """
)
