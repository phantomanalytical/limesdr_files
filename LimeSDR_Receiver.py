import numpy as np
import matplotlib.pyplot as plt
from gnuradio import gr, blocks, analog
import osmosdr

#Basic Gnu Radio flowgraph for LimeSDR
class LimeSDR_Receiver(gr.top_block):
    def __init__(self, freq, sample_rate, gain):
        gr.top_block.__init__(self)

        #LimeSDR Source
        self.source = osmosdr.source(args="soapy=0")

        #Source Params
        self.source.set_center_freq(freq)
        self.source.set_sample_rate(sample_rate)
        self.source.set_gain(gain)

        #Sink for file output and processing
        self.sink = blocks.file_sink(
            gr.sizeof_gr_complex,
            "/tmp/lime_capture.bin"
        )

        #Connect Blocks
        self.connect(self.source, self.sink)

# Entry point
if __name__ == "__main__":
    freq = 1e9 #1 GHz
    sample_rate = 1e6 # 1 MSps
    gain = 50 # 50 dB

    tb = LimeSDR_Receiver(freq, sample_rate, gain)
    print("Starting flowgraph...")
    tb.run()
    print("Flowgraph finished. Check /tmp/lime_capture.bin for output.")
