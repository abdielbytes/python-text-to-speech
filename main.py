from utils.pdf_extractor import extract_text_from_pdf
from utils.text_splitter import split_text
from utils.tts_converter import text_to_speech
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


# Make sure output folders exist
os.makedirs("audio_chunks", exist_ok=True)
os.makedirs("audiobook", exist_ok=True)

# Step 1: Extract text from PDF
text = extract_text_from_pdf("convert.pdf")
print("text extracted")

# Step 2: Split text
chunks = split_text(text, max_length=4096)

print("chunks made")

# Step 3: Convert chunks to audio
def convert_chunk(index, chunk):
    if not chunk.strip():  # Skip empty/whitespace-only chunks
        return f"Skipped empty chunk {index}"
    
    filename = f"audio_chunks/chunk_{index}.mp3"
    text_to_speech(chunk, filename)
    return filename


with ThreadPoolExecutor(max_workers=30) as executor:
    futures = [executor.submit(convert_chunk, i, chunk) for i, chunk in enumerate(chunks)]

    for future in as_completed(futures):
        print(f"✅ Created: {future.result()}")

print("✅ Audio chunks created. Now combine them in Audacity or another audio tool.")
