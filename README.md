### AI 音频预处理工具
#### 功能描述
* 包含常见的AI音频预处理功能，如音频重采样、音频去空白、音频时长获取等。
                 
#### pip安装
```shell
pip install audioprep
```

##### 获取音频时长
```
    from audioprep import duration
    rs = duration.get_audio_duration('test.wav')
    print(f"音频时长: {rs}秒")
```

##### 移除开头和结尾静音
```
    from audioprep import silence
    res = silence.trim_silence("530.mp3", "530_after.mp3")
    print(res)
```

##### 移除所有静音
```
    from audioprep import silence
    res = silence.remove_long_silence("530.mp3", "530_after.mp3",silence_thresh='-40dB', min_silence_len=3)
    print(res)
```

##### 音频重采样
```
    from audioprep import resample
    res = resample.resample_audio("530.mp3", 16000)
    print(res)
```

