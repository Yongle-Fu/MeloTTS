from melo.api import TTS
import os
from glob import glob
from pydub import AudioSegment

# Speed is adjustable
speed = 1.0

# CPU is sufficient for real-time inference.
# You can set it manually to 'cpu' or 'cuda' or 'cuda:0' or 'mps'
device = 'auto' # Will automatically use GPU if available

# English 
text = "Time limit of this CES sleep aid session has been reached"
model = TTS(language='EN', device=device)
speaker_ids = model.hps.data.spk2id
print('Speaker IDs:', speaker_ids)

# American accent
# output_path = 'output/en-us.wav'
# model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)

# British accent
# output_path = 'output/en-br.wav'
# model.tts_to_file(text, speaker_ids['EN-BR'], output_path, speed=speed)

# text = "The sleep aid session will last 15 minutes."
# output_path = 'output/en-us-ces-15.wav'
# model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)
# exit()

# text = "Level 1"
# output_path = 'output/en-us-level-1.wav'
# model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)

# text = "Level 2"
# output_path = 'output/en-us-level-2.wav'
# model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)

# text = "Level 3"
# output_path = 'output/en-us-level-3.wav'
# model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)

# # British accent
# output_path = 'output/en-br-ces-15.wav'
# # model.tts_to_file(text, speaker_ids['EN-BR'], output_path, speed=speed)

# 蓝牙未连接	Bluetooth not connected
# 一档	Level 1
# 二挡	Level 2
# 三挡	Level 3
# 四挡	Level 4
# 五档	Level 5
# 六档	Level 6
# 七档	Level 7
# 八档	Level 8
# 九档	Level 9
# 十档	Level 10
# 本次CES助眠时长已达上限	Time limit of this CES sleep aid session has been reached
# 该模式不支持使用CES功能	This mode does not support the use of the CES Sleep aid feature
# CES助眠	CES Sleep Aid
# 蓝牙已连接	Bluetooth Connected
# CES助眠已关闭	CES Sleep Aid turned off
# 未找到可播放的音乐	No playable music found
# 配对中	Bluetooth Pairing
# 蓝牙未配对	Bluetooth not paired
# 请连接APP获取完整功能	Please connect to the App to access all features
# 请佩戴设备	Please put on your device
# 关机	Powered Off
# 开机	Powered On
# 欢迎使用EASLEEP，请按主机前方右侧按键开启CES助眠，继续按右键增加档位，调节到额头微微酥麻即可	Welcome to Easleep, press the plus button on the front-right side of the control box to activate CES sleep aid, Continue pressing the right button to increase the intensity until your forehead feels a slight tingling.
# 欢迎使用EASLEEP	Welcome to Easleep

en_text_map = {  
  "BT_UNCONNECT": "Disconnected",
  "CES_1": "Level 1",
  "CES_2": "Level 2",
  "CES_3": "Level 3",
  "CES_4": "Level 4",
  "CES_5": "Level 5",
  "CES_6": "Level 6",
  "CES_7": "Level 7",
  "CES_8": "Level 8",
  "CES_9": "Level 9",
  "CES_10": "Level 10",
  "CES_LONG_TIME_NTY": "Time limit of this C E S sleep aid session has been reached",
  "CES_NOSUP": "This mode does not support the use of the C E S Sleep aid feature",
  "CES_STARTED": "C E S  Turned on",
  "CONNECTED": "Connected",
  "FINISH_TUNING_CES": "C E S Turned off",
  "NO_MUSIC": "No playable music found",
  "PAIRING": "Pairing",
  "PAIRING_TIMEOUT": "Pairing timeout",
  "PLEASE_CONNECT_APP": "Please connect to the App to access all features",
  "PLEASE_WEAR_DEVICE": "Please put on your device",
  "POWER_OFF": "Powered Off",
  "POWER_ON": "Powered On",
  "START_TUNING_CES": "Welcome to Easleep, press the plus button on the front-right side of the control box to activate C E S, sleep aid, Continue pressing the right button to increase the intensity until your forehead feels a slight tingling.",
  "WELCOME_EASLEEP": "Welcome to Easleep",
}

cn_text_map = {
  "BT_UNCONNECT": "蓝牙未连接",
  "CES_1": "一档",
  "CES_2": "二挡",
  "CES_3": "三挡",
  "CES_4": "四挡",
  "CES_5": "五档",
  "CES_6": "六档",
  "CES_7": "七档",
  "CES_8": "八档",
  "CES_9": "九档",
  "CES_10": "十档",
  "CES_LONG_TIME_NTY": "本次CES助眠时长已达上限",
  "CES_NOSUP": "该模式不支持使用CES功能",
  "CES_STARTED": "CES助眠",
  "CONNECTED": "蓝牙已连接",
  "FINISH_TUNING_CES": "CES助眠已关闭",
  "NO_MUSIC": "未找到可播放的音乐",
  "PAIRING": "配对中",
  "PAIRING_TIMEOUT": "蓝牙未配对",
  "PLEASE_CONNECT_APP": "请连接APP获取完整功能",
  "PLEASE_WEAR_DEVICE": "请佩戴设备",
  "POWER_OFF": "关机",
  "POWER_ON": "开机",
  "START_TUNING_CES": "欢迎使用EASLEEP，请按主机前方右侧按键开启CES助眠，继续按右键增加档位，调节到额头微微酥麻即可",
  "WELCOME_EASLEEP": "欢迎使用EASLEEP",
}

# 输入文件路径
input_path = "input/*.mp3"
# 输出文件路径的目录
output_ces_session_directory = "output/easleep-ces-session"
output_directory = "output/easleep-sounds-en-default"
wav_output_directory = "output/easleep_wav"

# 确保输出目录存在
os.makedirs(output_ces_session_directory, exist_ok=True)
os.makedirs(output_directory, exist_ok=True)
os.makedirs(wav_output_directory, exist_ok=True)

# 获取所有MP3文件的路径
mp3_files = glob(input_path)

speaker_id = speaker_ids['EN-Default']
print(f"speaker_id={speaker_id}")
print(f"Processing {len(mp3_files)} MP3 files...")


ces_cn_session_map = {
  "DAY": "已进入 日间模式",
  "NIGHT": "已进入 夜间模式",
  "SMART": "已进入 智能助眠模式",
  "FLASH": "已进入 闪睡模式",
  "DEEP": "已进入 深睡模式",
  "NAP": "已进入 午休模式",
  "TRAVEL": "已进入 差旅模式",
}
ces_en_session_map = {
  "DAY": "Day mode",
  "NIGHT": "Night mode",
  "SMART": "Smart sleep aid mode",
  "FLASH": "Relaxation mode",
  "DEEP": "Deep sleep mode",
  "NAP": "Nap mode",
  "TRAVEL": "Travel mode",
}
# 遍历ces_session_map, 生成对应的MP3文件
# for key, value in ces_en_session_map.items():
#     # 定义输出WAV文件路径
#     wav_path = os.path.join(wav_output_directory, f"{key}.wav")
#     text = value
#     print(f"Processing {key}... text={text}")
#     model.tts_to_file(text, speaker_id, wav_path, speed=speed)
#     # WAV => MP3
#     audio = AudioSegment.from_file(wav_path)
#     mp3_path = os.path.join(output_ces_session_directory, f"CES_{key}.mp3")
#     audio.export(mp3_path, format="mp3")
# exit()    

# 遍历每个MP3文件并转换为WAV格式
for mp3_file in mp3_files:
    # 获取文件名（不含扩展名）
    file_name = os.path.splitext(os.path.basename(mp3_file))[0]
    if file_name not in en_text_map:
        print(f"Skipping {file_name}...")
        continue
    # if file_name != 'BT_UNCONNECT' and file_name != 'CONNECTED' and file_name != 'PAIRING' and file_name != 'PAIRING_TIMEOUT' and file_name != 'CES_STARTED' and file_name != 'FINISH_TUNING_CES':
    #     print(f"Skipping 2 {file_name}...")
    #     continue
    # if file_name != 'CES_STARTED' and file_name != 'FINISH_TUNING_CES':
    #     print(f"Skipping 2 {file_name}...")
    #     continue
    if file_name != 'CES_LONG_TIME_NTY'  and file_name != 'CES_NOSUP' and file_name != 'START_TUNING_CES':
        print(f"Skipping 2 {file_name}...")
        continue
    # 定义输出WAV文件路径
    wav_path = os.path.join(wav_output_directory, f"{file_name}.wav")
    text = en_text_map[file_name]
    print(f"Processing {file_name}... text={text}")
    model.tts_to_file(text, speaker_id, wav_path, speed=speed)
    # WAV => MP3
    audio = AudioSegment.from_file(wav_path)
    mp3_path = os.path.join(output_directory, f"{file_name}.mp3")
    audio.export(mp3_path, format="mp3")

