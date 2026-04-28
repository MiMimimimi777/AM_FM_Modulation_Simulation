# 项目1｜入门：AM / FM 模拟调制仿真（通信最底层基础）

## 📌 项目简介
本项目为通信原理入门实验，基于 MATLAB 实现模拟调制解调的完整仿真，
包含 **AM、DSB、SSB、FM** 四种经典调制方式，学习通信系统最底层的信号调制、传输、加噪、解调和性能分析过程。

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
<img width="1760" height="809" alt="QQ_1777389533412" src="https://github.com/user-attachments/assets/11eb1cfe-2c41-4ef5-999e-deacbfae74a1" />



### DSB 调制解调过程
<img width="1768" height="801" alt="QQ_1777389508665" src="https://github.com/user-attachments/assets/94851790-2af1-465a-8965-8976fd4c995e" />

### SSB 调制解调过程
<img width="1750" height="801" alt="image" src="https://github.com/user-attachments/assets/96f78d96-ee80-44d7-89b0-7facf3a07e57" />

### FM 调制解调过程
<img width="1770" height="798" alt="image" src="https://github.com/user-attachments/assets/d687839e-3b53-44a2-bfc8-393c14a5907c" />

### 不同信噪比下的调制性能对比
<img width="1774" height="822" alt="image" src="https://github.com/user-attachments/assets/6360faee-1434-4cab-8965-c1791535df80" />
