def gaussian_spectrum_1D(rand_signal,epsilon,sample_period=1.0):
    '''low pass filter a 1D-signal with PSD=exp(-||k||^2 / (2 epsilon))'''
    import numpy as np
    # compute fourier transform
    fft_rand_signal = np.fft.fft( rand_signal )
    
    # compute frequencies corresponding to fourier transform
    frq_rand_signal = np.fft.fftfreq( rand_signal.size, sample_period )
    
    # compute and normalize amplitude filter: sqrt(PSD)
    filter_low = np.sqrt(np.exp(- frq_rand_signal**2 / (2*epsilon)))
    filter_low = filter_low / np.sum(filter_low)
    
    # filter fourier transform and inverse transformation
    filter_fft_rand_signal = fft_rand_signal*filter_low
    filter_rand_signal = np.real(np.fft.ifft( filter_fft_rand_signal ))
    
    # return filtered signal
    return filter_rand_signal

