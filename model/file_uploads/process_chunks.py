

def process_chunks(prompt, content, chunk_size=2000, lookback=100, separator=' '):

    text_chunks = []
    content_length = len(content)
    start_index = 0

    while start_index < content_length:
        end_index = start_index + chunk_size

        if end_index < content_length:
            last_separator_index = content.rfind(separator, start_index, end_index)
            if last_separator_index != -1:
                end_index = last_separator_index

        chunk = content[start_index:end_index].strip()
        if lookback > 0 and start_index > 0:
            lookback_start = max(0, start_index - lookback)
            lookback_text = content[lookback_start:start_index].strip()
            chunk = lookback_text + separator + chunk

        text_chunks.append(chunk)
        start_index = end_index

    # Combine the prompt with each chunk in a JSON object
    result = [{'prompt': prompt, 'chunk': chunk} for chunk in text_chunks]
    return result
