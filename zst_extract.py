import zstandard

dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
with open(r"C:\Users\Abel\Documents\Classes\Networks\Data\RS_2018-07.zst", 'rb') as ifh, open(r"C:\Users\Abel\Documents\Classes\Networks\Data\RS_2018-07", 'wb') as ofh:
    dctx.copy_stream(ifh, ofh)
