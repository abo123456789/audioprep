import io
import subprocess
from pathlib import Path

from pydub import AudioSegment


def resample_audio(audio_input_path, sample_rate=16000, audio_output_path=None) -> str:
    file_path = Path(audio_input_path)
    ext = file_path.suffix
    output_path = file_path.with_name(file_path.stem + f'_{sample_rate}').with_suffix(ext.lower())
    try:
        subprocess.run([
            'ffmpeg', '-i', audio_input_path,
            '-ac', '1',
            '-ar', str(sample_rate),
            '-y',
            audio_output_path or output_path
        ])
    except subprocess.CalledProcessError as e:
        print(f"音频重采样失败: {e.stderr.decode()}")
    except Exception as e:
        print(f"发生错误: {str(e)}")
    return audio_output_path or output_path


def resample_audio_bytes(audio_data: bytes, target_samplerate: int = 16000) -> bytes:
    audio_segment = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
    resampled_audio = audio_segment.set_frame_rate(target_samplerate)
    output_buffer = io.BytesIO()
    resampled_audio.export(output_buffer, format="wav")
    return output_buffer.getvalue()


if __name__ == '__main__':
    res = resample_audio('./voices/tvb_shot.wav', sample_rate=16000, audio_output_path='./voices/tvb_shot_16k.mp3')
    print(f"重采样后的音频保存路径: {res}")
