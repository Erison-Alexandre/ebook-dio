import os
from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.editor import TextClip

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(file_extension='mp4', res='360p').first()
        video.download(output_path)
        return video.default_filename
    except Exception as e:
        print("Erro ao baixar o vídeo:", e)
        return None

def download_subtitle(youtube_url, output_path):
    try:
        yt = YouTube(youtube_url)
        caption = yt.captions.get_by_language_code('pt')
        if caption:
            caption_str = caption.generate_srt_captions()
            with open(os.path.join(output_path, 'subtitle.srt'), 'w', encoding='utf-8') as file:
                file.write(caption_str)
            return True
        else:
            print("Não foi encontrada legenda em português para este vídeo.")
            return False
    except Exception as e:
        print("Erro ao baixar legenda:", e)
        return False

def add_subtitle(video_path, subtitle_path, output_path):
    try:
        video = VideoFileClip(video_path)
        subtitle = TextClip(subtitle_path, fontsize=24, color='white').set_position(('center', 'bottom')).set_duration(video.duration)
        video = video.set_subclip(0, video.duration)
        video = video.set_audio(video.audio)
        video = video.set_subtitles(subtitle)
        video.write_videofile(os.path.join(output_path, 'video_with_subtitle.mp4'), codec='libx264', audio_codec='aac')
        return True
    except Exception as e:
        print("Erro ao adicionar legenda ao vídeo:", e)
        return False

def main():
    url = input("Insira a URL do vídeo do YouTube: ")
    output_folder = input("Insira o caminho para a pasta de saída: ")

    video_filename = download_video(url, output_folder)
    if video_filename:
        subtitle_downloaded = download_subtitle(url, output_folder)
        if subtitle_downloaded:
            subtitle_path = os.path.join(output_folder, 'subtitle.srt')
            video_path = os.path.join(output_folder, video_filename)
            output_video_path = os.path.join(output_folder, 'video_with_subtitle.mp4')
            add_subtitle(video_path, subtitle_path, output_folder)
            print("Legenda adicionada com sucesso!")
            print("O vídeo com legenda está salvo em:", output_video_path)
            os.remove(video_path)
            os.remove(subtitle_path)
        else:
            print("Não foi possível adicionar legenda ao vídeo.")
            os.remove(os.path.join(output_folder, video_filename))
    else:
        print("Não foi possível baixar o vídeo.")

if __name__ == "__main__":
    main()
