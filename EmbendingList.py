import folder_paths

class EmbendingList:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {  }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Embeddings List (STRING)",)

    FUNCTION = "run"

    CATEGORY = "Embeddings Tools"

    def run(self):

        emb_files = folder_paths.get_filename_list("embeddings")
        emb_files_str = "\n".join(emb_files)

        return (emb_files_str, )


NODE_CLASS_MAPPINGS = {
    "EmbendingList": EmbendingList,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EmbendingList": "Embeddings List",
}