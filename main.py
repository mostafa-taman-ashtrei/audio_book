import pyttsx3
import PyPDF2

pdf_file = ''  # path to pdf file
audio_reader = pyttsx3.init()
audio_reader.setProperty('rate', 100)


with open(pdf_file, 'rb') as f:
    pdf_reader = PyPDF2.PdfFileReader(f)
    audio_reader = pyttsx3.init()
    audio_reader.setProperty('rate', 100)
    final_text = ''

    for page in range(pdf_reader.numPages):
        next_page = pdf_reader.getPage(page)
        page_text = next_page.extractText()
        print(page_text)
        final_text += page_text

    audio_reader.save_to_file(final_text, f'audiobook_{pdf_file}.mp3')
    audio_reader.runAndWait()
    print(f'Successfully converted {pdf_file} into an audio book ...')
