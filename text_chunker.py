def transform_chunk(chunk):
    chunk = chunk.encode('utf-8').decode('latin-1', 'replace')
    chunk = chunk.strip().replace("\n", "%0D%0A").replace(" ", "+").replace('"', '%22')
    return f"{chunk}"

def generate_chunks(text, default_chunk_size=5000):
    chunks = []
    while text:
        if len(text) > default_chunk_size:
            end = text.rfind(".", 0, default_chunk_size) + 1
            chunk = text[:end]
            text = text[end:].lstrip()
        else:
            chunk = text
            text = ""
        chunks.append(transform_chunk(chunk))
    return chunks