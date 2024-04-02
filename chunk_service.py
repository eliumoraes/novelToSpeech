def transform_chunk(chunk):
    chunk = chunk.strip().replace("\n", "%0D%0A").replace(" ", "+").replace('"', '%22')
    return f"{chunk}"

def generate_chunks(text):
    chunks = []
    while text:
        if len(text) > 5000:
            end = text.rfind(".", 0, 5000) + 1
            chunk = text[:end]
            text = text[end:].lstrip()
        else:
            chunk = text
            text = ""
        chunks.append(transform_chunk(chunk))
    return chunks