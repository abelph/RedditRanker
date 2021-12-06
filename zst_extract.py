import zstandard

dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
# Change to paths where data ZST file is located and output should be stored
with open(r"C:\Users\abelp\Documents\Classes\Networks\Data\RS_2020-11.zst", 'rb') as ifh, \
        open(r"C:\Users\abelp\Documents\Classes\Networks\Data\RS_2020-11", 'wb') as ofh:
    dctx.copy_stream(ifh, ofh)
