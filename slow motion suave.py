from moviepy.editor import VideoFileClip
from moviepy.video.fx import speedx

input_video = "D:\\Nova pasta\\video_sharpen\\slow.mp4"
output_slow = "D:\\Nova pasta\\video_sharpen\\video em slow.mp4"
slow_factor = 4

clip = VideoFileClip(input_video)

# Aplicar câmera lenta com speedx
slow_clip = clip.fx(speedx.speedx, factor=1/slow_factor)

# Ajustar duração (opcional, mas recomendado para manter sincronização)
slow_clip = slow_clip.set_duration(clip.duration * slow_factor)

slow_clip.write_videofile(output_slow, codec="libx264", audio_codec="aac")
print("Vídeo em câmera lenta suave gerado com sucesso!")
