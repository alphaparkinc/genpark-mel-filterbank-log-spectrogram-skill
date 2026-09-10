import math

class MelFilterbank:
    """
    Log-Mel Spectrogram Filterbank.
    Converts linear frequencies to Mel scale: m = 2595 * log10(1 + f/700).
    Constructs triangular bandpass filters.
    """
    def hz_to_mel(self, hz):
        return 2595.0 * math.log10(1.0 + hz / 700.0)

    def mel_to_hz(self, mel):
        return 700.0 * (10.0**(mel / 2595.0) - 1.0)

    def compute_filterbank(self, num_filters=4, n_fft=16, sample_rate=8000):
        low_mel = self.hz_to_mel(0)
        high_mel = self.hz_to_mel(sample_rate / 2)
        mel_points = [low_mel + i * (high_mel - low_mel) / (num_filters + 1) for i in range(num_filters + 2)]
        hz_points = [self.mel_to_hz(m) for m in mel_points]
        bin_points = [int((n_fft + 1) * hz / sample_rate) for hz in hz_points]

        fbank = []
        for m in range(1, num_filters + 1):
            f_m_minus = bin_points[m - 1]
            f_m = bin_points[m]
            f_m_plus = bin_points[m + 1]
            filter_row = [0.0] * (n_fft // 2 + 1)
            for k in range(f_m_minus, f_m):
                if f_m > f_m_minus and k < len(filter_row):
                    filter_row[k] = (k - f_m_minus) / (f_m - f_m_minus)
            for k in range(f_m, f_m_plus):
                if f_m_plus > f_m and k < len(filter_row):
                    filter_row[k] = (f_m_plus - k) / (f_m_plus - f_m)
            fbank.append(filter_row)
        return fbank
