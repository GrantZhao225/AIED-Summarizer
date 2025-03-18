import openai

def course_context():
    pdf_text = extract_text_from_pdf("course_notes.pdf")
    html_text = extract_text_from_html("lecture_slides.html")
    return pdf_text[:2000] + "\n\n" + html_text[:2000]

def summarizer(text, context):
    prompt = f"""
    You are an AI summarizer for lecture transcripts.
    
    Course Context: {context}
    
    Transcript Chunk: {text}
    
    Provide a concise summary highlighting key concepts and examples.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are an expert in summarizing educational lectures."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]