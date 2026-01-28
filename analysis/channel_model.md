# Channel Model

The communication channel is modeled as an additive white Gaussian noise (AWGN) channel to establish a theoretical baseline for microwave digital communication analysis. This model isolates the impact of noise on system performance while avoiding hardware-specific impairments, allowing clear validation of modulation behavior and error performance.

In the AWGN model, noise is represented as a zero-mean Gaussian random process with constant power spectral density across the system bandwidth. This assumption is commonly used in microwave and RF system analysis to characterize thermal noise effects introduced by receivers and front-end electronics.

While real microwave channels may exhibit additional impairments such as multipath fading, frequency-selective distortion, or phase noise, the AWGN model provides a fundamental reference case. Performance under this simplified channel serves as a benchmark against which more complex channel models can later be compared.

The primary limitation of this channel model is its inability to capture propagation-related fading or hardware non-idealities. However, for validating theoretical modulation performance and noise-limited behavior, the AWGN model is both appropriate and widely accepted.