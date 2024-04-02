from gtts import gTTS

text = "Execution Context Stack"
tts = gTTS(text=text, lang="en")

# 导出的文件名跟 text 保持一致，是个变量
tts.save(f"Store/{text}.mp3")
