from ppgan.apps import PPMSVSRPredictor
import os

input_dir = "H:/code/PaddleGAN-Old-video-coloring/Data/"
output_dir = "H:/code/PaddleGAN-Old-video-coloring/output/PPMSVSR/RHColor/"

filename = "RHColor.mp4"

# 定义视频路径
video_path = input_dir + filename

# 去掉文件名中的后缀
filename_without_extension = os.path.splitext(filename)[0]
ext=os.path.splitext(filename)[1]
output_video_path = output_dir + filename_without_extension + "/"+ filename_without_extension + "_ppmsvsr_out" + ext

sr = PPMSVSRPredictor()
# 测试一个视频文件
sr.run(video_path)  #原视频所在路径

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
final_output_path = os.path.join(output_dir, f"{filename_without_extension}_srfinial.mp4")
final_clip.write_videofile(final_output_path, codec="libx264", fps=colored_clip.fps)

# 删除临时文件
#os.remove(output_video_path)
