import io
import math

import librosa


def get_audio_duration(input_source):
    """
    最准确的音频时长计算方法
    使用 len(y) / sr 直接计算，基于实际解码的音频数据
    """
    try:
        if isinstance(input_source, str):
            y, sr = librosa.load(input_source, sr=None, duration=None)
        elif isinstance(input_source, io.BytesIO):
            # 字节流
            input_source.seek(0)
            y, sr = librosa.load(input_source, sr=None, duration=None)
        else:
            raise ValueError("Unsupported input type")

        duration = len(y) / sr
        return ceil_to_2decimal(duration)

    except Exception as e:
        print(f"Error in most accurate method: {e}")
        return 0


def ceil_to_2decimal(number):
    if not number:
        return None
    return math.ceil(number * 100) / 100


if __name__ == '__main__':
    rs = get_audio_duration('./voices/tvb_shot.wav')
    print(f"音频时长: {rs}秒")
