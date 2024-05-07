import folder_paths
import re


class EmbeddingsNameLoader:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "text": ("STRING", {"multiline": True}),
                              }}

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("STRING", )

    FUNCTION = "run"

    CATEGORY = "Embeddings Tools"

    def run(self, text):

        emb_files = folder_paths.get_filename_list("embeddings")

        output_text = text

        for file_name in emb_files:

            base_name = file_name.split('\\')[-1].split('.')[0]

            #output_text = output_text.replace(base_name, f"embedding:{base_name}")
            
            pattern = re.compile(re.escape(base_name), re.IGNORECASE)
            output_text = pattern.sub(f"embedding:{base_name}", output_text)

        return (output_text, )


NODE_CLASS_MAPPINGS = {
    "EmbeddingsNameLoader": EmbeddingsNameLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EmbeddingsNameLoader": "Load Embeddings by Name",
}