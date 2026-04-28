function out = demodulation(sig, t, fc, type)
    switch type
        case 'AM'
            out = abs(hilbert(sig)) - 1;  % 包络检波
        case 'DSB'
            out = sig .* cos(2*pi*fc*t);
            [b,a] = butter(2, 0.05);
            out = filtfilt(b,a,out);
        case 'SSB'
            out = sig .* cos(2*pi*fc*t);
            [b,a] = butter(2, 0.05);
            out = filtfilt(b,a,out);
        case 'FM'
            out = diff(sig);
            out = [out, out(end)];
    end
    out = out / max(abs(out));  % 归一化
end