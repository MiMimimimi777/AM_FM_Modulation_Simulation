# 项目1｜入门：AM / FM 模拟调制仿真（通信最底层基础）

## 📌 项目简介
本项目为通信原理入门实验，基于 MATLAB(python) 实现模拟调制解调的完整仿真，
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
- python
- 通信系统基础理论

## 📦 项目文件结构
- `main.m`               主运行程序
- `modulation.m`         调制函数
- `demodulation.m`       解调函数
- `awgn_channel.m`       加噪信道仿真
- `plot_waveform.m`      波形绘图函数
- `main.py`              python-AM/FM仿真
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
<img width="1571" height="735" alt="1777439368565" src="https://github.com/user-attachments/assets/0c5f61c2-1f5d-46fc-a003-61071d796d4a" />


### DSB 调制解调过程
<img width="1596" height="767" alt="1777439385801" src="https://github.com/user-attachments/assets/06cf725a-de7f-474f-bd34-95db1d07d665" />


### SSB 调制解调过程
<img width="1550" height="731" alt="1777439400799" src="https://github.com/user-attachments/assets/569b68ee-6a04-4048-b6bc-e476339fdba6" />


### FM 调制解调过程

<img width="1551" height="734" alt="1777439414127" src="https://github.com/user-attachments/assets/ff71b177-57de-4e67-aeb9-c1492d47f612" />

### 不同信噪比下的调制性能对比
<img width="1616" height="756" alt="1777439465432" src="https://github.com/user-attachments/assets/85983452-2d7a-4774-8a30-9d764fb639f0" />


### AI 盲识别
<img width="1609" height="766" alt="1777439487203" src="https://github.com/user-attachments/assets/0e23f4fb-1cd0-4040-b37f-9295456871ea" />


<img width="371" height="85" alt="1777439314064" src="https://github.com/user-attachments/assets/9eebc1aa-50e0-4d2b-8268-836bd6352c6b" />

### Python AM/FM仿真效果
<img width="1590" height="832" alt="image" src="https://github.com/user-attachments/assets/4bf6d86c-e2e2-4421-9b74-a58d31e204ca" />
<img width="600" height="336" alt="1777439173669" src="https://github.com/user-attachments/assets/c3ef3ccf-d35e-4865-b106-dc2e04ea8c34" />




