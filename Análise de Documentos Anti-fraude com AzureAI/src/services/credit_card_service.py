from azure.core.crdedentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analize_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.KEY)
        document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
        card_info = document_Client.begin_analyze_from_url("prebuild-creditCard", card_url)
        result = card_info.result()
        return result
    except Exception as ex:
        return None

