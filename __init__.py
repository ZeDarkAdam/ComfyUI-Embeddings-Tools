from .EmbeddingsNameLoader import EmbeddingsNameLoader
from .EmbendingList import EmbendingList

NODE_CLASS_MAPPINGS = {
    "EmbeddingsNameLoader": EmbeddingsNameLoader,
    "EmbendingList": EmbendingList,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EmbeddingsNameLoader": "Load Embeddings by Name",
    "EmbendingList": "Embeddings List",
}
