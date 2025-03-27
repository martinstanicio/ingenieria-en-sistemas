# Ancho de banda de Nyquist
The Nyquist bandwidth refers to a limitation on the data rate in a noise-free channel based solely on the bandwidth of the signal. Nyquist stated that if the rate of signal transmission is 2B, then a signal with frequencies no greater than B is sufficient to carry that signal rate. Conversely, given a bandwidth of B, the highest signal rate that can be carried is 2B. This limitation arises due to intersymbol interference, which can be caused by delay distortion.

For binary signals (two voltage levels), a bandwidth of B Hz can support a data rate of **2B bps**. However, if signals with more than two levels (multilevel signaling) are used, each signal element can represent more than one bit, and the Nyquist formulation becomes:

**C = 2B log₂ M**

where:

- C is the channel capacity.
- B is the bandwidth.
- M is the number of discrete signal levels.

For example, a voice channel with a bandwidth of 3100 Hz has a Nyquist capacity of **6200 bps** for binary signals (M=2). With multilevel signaling, such as M=8, the capacity becomes **18,600 bps** for the same bandwidth.

It's important to note that the Nyquist formulation considers a noise-free channel. In real-world scenarios, noise is a significant limiting factor, and the maximum achievable data rate is often better described by the Shannon Capacity Formula, which takes into account the signal-to-noise ratio (SNR). Nyquist's formula is particularly useful in the development of digital-to-analog encoding schemes. The term 'Nyquist bandwidth' is a key term related to channel capacity. The works of Shannon and Nyquist both place upper limits on the bit rate of a channel but based on different approaches.