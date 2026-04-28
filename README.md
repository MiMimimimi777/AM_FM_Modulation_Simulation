# 项目1｜入门：AM / FM 模拟调制仿真（通信最底层基础）

## 📌 项目简介
本项目为通信原理入门实验，基于 MATLAB 实现模拟调制解调的完整仿真，
包含 **AM、DSB、SSB、FM** 四种经典调制方式，学习通信系统最底层的信号调制、传输、加噪、解调和性能分析过程。

本项目引入 K - 近邻（KNN）机器学习算法，实现了对 AM/DSB/SSB/FM 四种调制方式的盲识别。系统无需预先获知信号的调制类型，仅通过时域和频域特征即可实现最好 90% 以上的识别准确率，为通信系统的智能化信号处理提供了轻量化解决方案。
## 🎯 实现内容
1. 生成一段基础低频信号（简单余弦波形）
2. 实现四种模拟调制：
   - AM 调制
   - DSB 调制
   - SSB 调制
   - FM 调制
3. 加入高斯白噪声，模拟真实无线信道传输干扰
4. 编写对应解调算法，将原始信号恢复出来
5. 绘制波形与频谱图：
   - 原始信号时域波形
   - 调制信号频谱
   - 解调信号波形
   - 不同信噪比下四种调制方式性能对比图

## 🛠️ 项目环境
- MATLAB R20XX 及以上版本
- 通信系统基础理论

## 📦 项目文件结构
- `main.m`               主运行程序
- `modulation.m`         调制函数
- `demodulation.m`       解调函数
- `awgn_channel.m`       加噪信道仿真
- `plot_waveform.m`      波形绘图函数
- `README.md`            项目说明文档

## ✨ 项目目标
- 理解模拟调制的基本原理
- 掌握调制信号的时域与频域特性
- 理解噪声对通信系统的影响
- 学会对比不同调制方式的性能

---
本项目用于通信方向的课程学习与实验练习。

## 仿真结果
### AM 调制解调效果


### DSB 调制解调过程


### SSB 调制解调过程
<img width="1553" height="745" alt="image" src="https://github.com/user-attachments/assets/7183b60e-d722-4035-b9ef-e355bf191b49" />

### FM 调制解调过程
<img width="1541" height="729" alt="image" src="https://github.com/user-attachments/assets/dd6a4925-5727-449b-ae25-d4da58f51f94" />

### 不同信噪比下的调制性能对比
<img width="1573" height="751" alt="image" src="https://github.com/user-attachments/assets/b789e93a-2205-4111-ab7d-673feb3dad42" />

### AI的盲识别
<img width="1605" height="759" alt="image" src="https://github.com/user-attachments/assets/0823e36d-0c0a-469e-9679-e349154ea67b" />

<img width="409" height="147" alt="image" src="https://github.com/user-attachments/assets/fb2358e0-793b-40f7-9734-10ea8a8923a4" />
