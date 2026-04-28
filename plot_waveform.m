function plot_waveform(t, mt, mod_sig, noisy_sig, demod_sig, name)
    figure('Name', name);
    subplot(4,1,1); plot(t, mt); title('原始信号');
    subplot(4,1,2); plot(t, mod_sig); title([name '调制信号']);
    subplot(4,1,3); plot(t, noisy_sig); title('加噪声后');
    subplot(4,1,4); plot(t, demod_sig); title('解调输出');
end