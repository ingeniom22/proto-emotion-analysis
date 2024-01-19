from fastapi import FastAPI, File, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI

client = OpenAI()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    try:
        # Save the uploaded audio file
        with open(file.filename, "wb") as audio_file:
            audio_file.write(file.file.read())

        audio_file = open("recorded_audio.wav", "rb")
        transcription = client.audio.transcriptions.create(
            model="whisper-1", file=audio_file, response_format="text"
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": 
                    """
                    Anda adalah seorang Psikolog. Tugas anda adalah memberikan analisis persentase emosi dari pesan user.
                    Contoh: Marah 10%, Sedih 75%, Gugup 15%. Anda boleh menggunakan kategori emosi lain yang lebih tepat. 
                    Gunakan Bahasa Indonesia yang baik dan benar.
                    """,
                },
                {"role": "user", "content": transcription},
            ],
        )

        response = response.choices[0].message.content

        print(response)

        # return templates.TemplateResponse(
        #     "index.html",
        #     {"request": request, "transcription": transcription, "response": response},
        # )

        return {
            "message": "Audio file received",
            "transcription": transcription,
            "response": response,
        }

    except Exception as e:
        print(e)
        return JSONResponse(content={"error": str(e)}, status_code=500)
