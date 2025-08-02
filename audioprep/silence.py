import io
import os
import subprocess

from pydub import AudioSegment
from pydub.silence import detect_silence


def trim_silence_from_bytesio(byte_buffer, output_format='wav', silence_thresh=-50, chunk_size=100) -> io.BytesIO:
    if not byte_buffer:
        return byte_buffer
    byte_buffer.seek(0)
    audio = AudioSegment.from_file(byte_buffer, format=output_format)

    silence_ranges = detect_silence(audio, min_silence_len=chunk_size, silence_thresh=silence_thresh)
    trimmed_audio = audio
    if silence_ranges:
        start_trim_begin = silence_ranges[0][0]
        start_trim_end = silence_ranges[0][1]
        print('before length audio:', len(audio))
        print("start_trim_begin:", start_trim_begin, "start_trim_end:", start_trim_end)
        if start_trim_begin == 0:
            print('开头存在空白音')
            trim_begin = start_trim_end
        else:
            trim_begin = 0
        end_trim_begin = silence_ranges[-1][0]
        end_trim_end = silence_ranges[-1][1]  # 最后一段静音结束的时间
        print("end_trim_begin:", end_trim_begin, "end_trim_end:", end_trim_end)
        if end_trim_end == len(audio):
            print('结尾存在空白音')
            trim_end = end_trim_begin
        else:
            trim_end = len(audio)
        trimmed_audio = audio[trim_begin:trim_end]
        print('after length audio:', len(trimmed_audio))
    output_stream = io.BytesIO()
    trimmed_audio.export(output_stream, format=output_format)

    return output_stream


def trim_silence(input_path, output_path, silence_thresh=-90, chunk_size=100):
    """
    Detect and trim silence from audio file

    Args:
        input_path (str): Path to input audio file
        output_path (str): Path to save output audio file
        silence_thresh (int): Silence threshold in dB (default: -50)
        chunk_size (int): Minimum silence length in ms (default: 100)

    Returns:
        bool: True if processing successful, False otherwise
    """
    try:
        # Check if input file exists
        if not input_path or not os.path.exists(input_path):
            print(f"Input file does not exist: {input_path}")
            return False

        # Load audio from file
        audio = AudioSegment.from_file(input_path)

        # Detect silence ranges
        silence_ranges = detect_silence(audio, min_silence_len=chunk_size, silence_thresh=silence_thresh)

        trimmed_audio = audio
        if silence_ranges:
            start_trim_begin = silence_ranges[0][0]
            start_trim_end = silence_ranges[0][1]
            print('Before length audio:', len(audio))
            print("Start trim begin:", start_trim_begin, "start trim end:", start_trim_end)

            if start_trim_begin == 0:
                print('开头存在空白音 (Silence at beginning)')
                trim_begin = start_trim_end
            else:
                trim_begin = 0

            end_trim_begin = silence_ranges[-1][0]
            end_trim_end = silence_ranges[-1][1]  # 最后一段静音结束的时间
            print("End trim begin:", end_trim_begin, "end trim end:", end_trim_end)

            if end_trim_end == len(audio):
                print('结尾存在空白音 (Silence at end)')
                trim_end = end_trim_begin
            else:
                trim_end = len(audio)

            trimmed_audio = audio[trim_begin:trim_end]
            print('After length audio:', len(trimmed_audio))

        output_format = os.path.splitext(output_path)[1][1:].lower()  # Get format from file extension
        if not output_format:
            output_format = 'wav'  # Default format

        trimmed_audio.export(output_path, format=output_format)
        print(f"Audio saved to: {output_path}")
        return output_path

    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        return None


def remove_long_silence(input_file, output_file, silence_thresh='-40dB', min_silence_len=3):
    cmd = [
        'ffmpeg', '-y', '-i', input_file,
        '-af', f'silenceremove=stop_periods=-1:stop_duration={min_silence_len}:stop_threshold={silence_thresh}',
        output_file
    ]
    subprocess.run(cmd, check=True)
    print(f"处理完成，已保存为 {output_file}")
    return output_file


if __name__ == '__main__':
    res = remove_long_silence("./voices/test_empt.MP3", "./voices/after_test_empt.MP3")
    print(res)
