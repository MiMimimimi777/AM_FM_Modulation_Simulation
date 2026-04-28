%% 通信原理实验：AM DSB SSB FM 调制解调仿真
clear; clc; close all;

%% 1. 参数设置
fc = 50;       % 载波频率
fm = 2;        % 信号频率
Fs = 2000;     % 采样率
t = 0:1/Fs:1;  % 时间轴

%% 2. 原始基带信号（余弦波）
mt = cos(2*pi*fm*t);

%% 3. 四种调制
[am_mod, dsb_mod, ssb_mod, fm_mod] = modulation(mt, t, fc);

%% 4. 加入高斯白噪声
SNR = 10;
am_noisy = awgn_channel(am_mod, SNR);
dsb_noisy = awgn_channel(dsb_mod, SNR);
ssb_noisy = awgn_channel(ssb_mod, SNR);
fm_noisy = awgn_channel(fm_mod, SNR);

%% 5. 解调
am_demod = demodulation(am_noisy, t, fc, 'AM');
dsb_demod = demodulation(dsb_noisy, t, fc, 'DSB');
ssb_demod = demodulation(ssb_noisy, t, fc, 'SSB');
fm_demod = demodulation(fm_noisy, t, fc, 'FM');

%% 6. 绘图
plot_waveform(t, mt, am_mod, am_noisy, am_demod, 'AM');
plot_waveform(t, mt, dsb_mod, dsb_noisy, dsb_demod, 'DSB');
plot_waveform(t, mt, ssb_mod, ssb_noisy, ssb_demod, 'SSB');
plot_waveform(t, mt, fm_mod, fm_noisy, fm_demod, 'FM');

%% 7. 不同 SNR 性能对比
SNR_list = 0:5:20;
MSE_am = zeros(size(SNR_list));
MSE_dsb = zeros(size(SNR_list));
MSE_ssb = zeros(size(SNR_list));
MSE_fm = zeros(size(SNR_list));

for i = 1:length(SNR_list)
    amn = awgn_channel(am_mod, SNR_list(i));
    dsn = awgn_channel(dsb_mod, SNR_list(i));
    ssn = awgn_channel(ssb_mod, SNR_list(i));
    fmn = awgn_channel(fm_mod, SNR_list(i));
    
    adm = demodulation(amn, t, fc, 'AM');
    ddm = demodulation(dsn, t, fc, 'DSB');
    sdm = demodulation(ssn, t, fc, 'SSB');
    fdm = demodulation(fmn, t, fc, 'FM');
    
    MSE_am(i) = mean((adm - mt).^2);
    MSE_dsb(i) = mean((ddm - mt).^2);
    MSE_ssb(i) = mean((sdm - mt).^2);
    MSE_fm(i) = mean((fdm - mt).^2);
end

figure;
plot(SNR_list, MSE_am, 'r-o', SNR_list, MSE_dsb, 'g-s', ...
     SNR_list, MSE_ssb, 'b-^', SNR_list, MSE_fm, 'm-d');
legend('AM','DSB','SSB','FM');
xlabel('SNR (dB)');
ylabel('均方误差 MSE');
title('不同信噪比下调制性能对比');
grid on;