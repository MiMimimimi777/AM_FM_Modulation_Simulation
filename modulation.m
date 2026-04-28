function [am, dsb, ssb, fm] = modulation(mt, t, fc)
    ct = cos(2*pi*fc*t);         % 载波
    ka = 0.5;                    % AM 调制度
    kf = 10;                     % FM 频偏系数
    
    am = (1 + ka*mt) .* ct;      % AM
    dsb = mt .* ct;              % DSB
    
    % SSB (希尔伯特变换)
    mt_hilbert = hilbert(mt);
    ssb = real(mt_hilbert .* exp(1j*2*pi*fc*t));
    
    % FM
    fm_int = cumsum(mt)/length(t)*max(t);
    fm = cos(2*pi*fc*t + kf*fm_int);
end