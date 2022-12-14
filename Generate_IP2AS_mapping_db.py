from bz2 import BZ2File
from gzip import GzipFile
import os
from pyasn import mrtx, __version__


def open_archive(fpath):
    """Open a bz2 or gzip archive."""
    # Thanks to Chris poliquin for this method (https://github.com/poliquin)
    mode = "rb"
    GZIP_MAGIC, BZ2_MAGIC = b"\x1f\x8b", b"\x42\x5a\x68"  # magic numbers
    with open(fpath, mode) as fh:
        hdr = fh.read(max(len(BZ2_MAGIC), len(GZIP_MAGIC)))
    if hdr.startswith(BZ2_MAGIC):
        return BZ2File(fpath, mode)
    elif hdr.startswith(GZIP_MAGIC):
        return GzipFile(fpath, mode)
    else:
        raise TypeError("Cannot determine file type '%s'" % fpath)


if __name__ == '__main__': 
    data_dir = 'data/'   # the Routeviews Prefix-to-AS mappings downloaded from CAIDA
    files = os.listdir(data_dir)
    dump_file = []
    for file in files:
        if file.endswith('.gz'):
            dump_file.append(file)
    dump_file.reverse()   #获取最近日期的

    data = open_archive(data_dir+dump_file[0])
    prefixes = {}
    for d in data:
        d = d.decode()
        d = d.split('\n')[0]
        items = d.split('\t')
        ip,length,asn = items
        prefix = ip + '/' + length
        prefixes[prefix] = asn

    name = dump_file[0].split('-')[2]
    out_file = "data/ipasn_%s.dat" % (name)
    mrtx.dump_prefixes_to_file(prefixes, out_file, dump_file)
