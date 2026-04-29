# ==============================
# 通信仿真全功能 Python 版
# 1:1 平替 MATLAB
# AM调制 + FM调制 + 噪声 + 解调 + FFT + 画图 + AI识别
# ==============================

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# ----------------------
# 1. 基础参数设置
# ----------------------
fs = 1000       # 采样率
t = np.linspace(0, 1, fs, endpoint=False)
fc = 100        # 载波频率
fm = 2          # 基带信号频率

# ----------------------
# 2. AM调制
# ----------------------
mt = np.cos(2 * np.pi * fm * t)
carrier = np.cos(2 * np.pi * fc * t)
am_signal = (1 + 0.5 * mt) * carrier

# ----------------------
# 3. 加噪声 AWGN
# ----------------------
def awgn(signal, snr_db):
    sig_pow = np.mean(signal ** 2)
    noise_pow = sig_pow / (10 ** (snr_db / 10))
    noise = np.random.normal(0, np.sqrt(noise_pow), signal.shape)
    return signal + noise

am_noisy = awgn(am_signal, 10)

# ----------------------
# 3.5 AM解调（包络检波）
# ----------------------
envelope = np.abs(am_noisy)
b, a = signal.butter(5, 10/(fs/2), 'low')
demod_signal = signal.filtfilt(b, a, envelope)

# ----------------------
# 3.6 FM调制（频率调制）
# ----------------------
kf = 50         # 频率偏差 (Hz)
phase = 2 * np.pi * kf * np.cumsum(mt) / fs  # 累积相位
fm_signal = np.cos(2 * np.pi * fc * t + phase)

fm_noisy = awgn(fm_signal, 10)

# ----------------------
# 4. FM解调（鉴频器）
# ----------------------
# 使用导数法进行FM解调
# 瞬时频率 = (1/2π) * dφ/dt
fm_derivative = np.diff(np.unwrap(np.angle(signal.hilbert(fm_noisy))))
b_fm, a_fm = signal.butter(5, 15/(fs/2), 'low')
fm_demod_signal = signal.filtfilt(b_fm, a_fm, fm_derivative)

# ----------------------
# 5. FFT 频谱分析
# ----------------------
def plot_fft(signal, fs, title):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1/fs)[:N//2]
    amp = 2.0/N * np.abs(yf[:N//2])
    plt.plot(xf, amp)
    plt.title(title)
    plt.grid(True)

# ----------------------
# 6. 波形画图（增加FM部分）
# ----------------------
plt.figure(figsize=(16, 18))

plt.subplot(6, 1, 1)
plt.plot(t[:300], mt[:300])
plt.title("基带信号", fontsize=12, pad=10)
plt.grid(True)

plt.subplot(6, 1, 2)
plt.plot(t[:300], am_signal[:300])
plt.title("AM调制信号", fontsize=12, pad=10)
plt.grid(True)

plt.subplot(6, 1, 3)
plt.plot(t[:300], fm_signal[:300])
plt.title("FM调制信号", fontsize=12, pad=10)
plt.grid(True)

plt.subplot(6, 1, 4)
plt.plot(t[:300], am_noisy[:300])
plt.title("AM加噪声", fontsize=12, pad=10)
plt.grid(True)

plt.subplot(6, 1, 5)
plt.plot(t[:300], fm_noisy[:300])
plt.title("FM加噪声", fontsize=12, pad=10)
plt.grid(True)

plt.subplot(6, 1, 6)
plt.plot(t[1:300], demod_signal[1:300], label='AM解调', alpha=0.7)
plt.plot(t[1:300], fm_demod_signal[1:300], label='FM解调', alpha=0.7)
plt.title("解调信号对比", fontsize=12, pad=10)
plt.legend()
plt.grid(True)

plt.subplots_adjust(hspace=1.5)
plt.show()

# ----------------------
# 7. AI调制识别（KNN + 交叉验证）
# ----------------------
def extract_feature(sig):
    f1 = np.mean(np.abs(sig))
    f2 = np.var(sig)
    f3 = np.mean(np.abs(np.diff(sig)))
    f4 = np.max(np.abs(fft(sig)))
    return [f1, f2, f3, f4]

# 生成更大规模数据集 + 低SNR
from sklearn.model_selection import cross_val_score

features = []
labels = []

# AM信号样本 (标签: 0)
for _ in range(300):
    sig = awgn(am_signal, np.random.randint(1, 15))  # 降低SNR到1-15dB
    features.append(extract_feature(sig))
    labels.append(0)

# FM信号样本 (标签: 1)
for _ in range(300):
    sig = awgn(fm_signal, np.random.randint(1, 15))
    features.append(extract_feature(sig))
    labels.append(1)

features = np.array(features)
labels = np.array(labels)

# 使用5折交叉验证（更准确）
knn = KNeighborsClassifier(n_neighbors=5)
cv_scores = cross_val_score(knn, features, labels, cv=5)
acc = cv_scores.mean()

print("=" * 50)
print(f"AI 调制识别准确率 = {acc*100:.2f}%（5折交叉验证）")
print(f"准确率范围: {cv_scores.min()*100:.2f}% ~ {cv_scores.max()*100:.2f}%")
print("=" * 50)

# ========================
# 实时识别演示
# ========================
# 用所有数据训练最终模型
knn_final = KNeighborsClassifier(n_neighbors=5)
knn_final.fit(features, labels)

# 随机选择 AM 或 FM 进行识别演示
test_type = np.random.choice([0, 1])
test_snr = np.random.randint(2, 12)

if test_type == 0:
    test_signal = awgn(am_signal, test_snr)
    true_label = "AM"
else:
    test_signal = awgn(fm_signal, test_snr)
    true_label = "FM"

# 提取特征并预测
test_feature = extract_feature(test_signal)
prediction = knn_final.predict([test_feature])[0]
confidence = knn_final.predict_proba([test_feature]).max()

pred_label = "AM" if prediction == 0 else "FM"
result_symbol = "✓ 正确" if pred_label == true_label else "✗ 错误"

print("\n【AI 实时识别演示】")
print(f"真实信号类型: {true_label} (SNR: {test_snr}dB)")
print(f"AI 预测结果: {pred_label}")
print(f"识别置信度: {confidence*100:.2f}%")
print(f"识别状态: {result_symbol}")
print("=" * 50)
