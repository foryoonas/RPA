import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def addtext(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] + 0.5, y[i], ha='center')

plt.rcParams['font.family'] = 'AppleGothic'  

# CSV 파일 읽기
data = pd.read_csv('/Users/seol-yun-a/Desktop/202310467/RPA/5week/singer_youtube.csv')

# 바 차트 그리기
plt.figure(figsize=(15, 10))
plt.bar(data['name'], data['youtube count'], color=('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple'))
plt.title('YouTube Channel Subscriber Count by Singer')
plt.xlabel('Singer')
plt.ylabel('YouTube Count')

# 텍스트 추가
addtext(data['name'], data['youtube count'])

# 차트 보여주기
plt.show()
