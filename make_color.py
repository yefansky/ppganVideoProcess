from ppgan.apps import DeOldifyPredictor
from moviepy.editor import VideoFileClip, AudioFileClip
import os

# 创建 DeOldifyPredictor 实例
deoldify = DeOldifyPredictor()

root_dir = "f:/ppganVideoProcess"
input_dir = root_dir + "/Data/"
output_dir = root_dir + "/output/DeOldify/"

filename = "RH.mp4"

# 定义视频路径
video_path = input_dir + filename

# 去掉文件名中的后缀
filename_without_extension = os.path.splitext(filename)[0]
ext=os.path.splitext(filename)[1]
output_video_path = output_dir + filename_without_extension + "/"+ filename_without_extension + "_deoldify_out" + ext

# 使用 DeOldify 模型为视频添加颜色
deoldify.run(video_path)

# 获取原始视频的音频
audio_clip = AudioFileClip(video_path)

# 获取添加颜色后的视频
colored_clip = VideoFileClip(output_video_path)

# 检查视频和音频时长是否一致，如果不一致，则调整音频的时长
if colored_clip.duration != audio_clip.duration:
    audio_clip = audio_clip.set_duration(colored_clip.duration)

# 将原始视频的音频合并到添加颜色后的视频中
final_clip = colored_clip.set_audio(audio_clip)


# 输出合并后的视频
final_output_path = os.path.join(output_dir, f"{filename_without_extension}_finial.mp4")
final_clip.write_videofile(final_output_path, codec="libx264", fps=colored_clip.fps)

# 删除临时文件
#os.remove(output_video_path)
