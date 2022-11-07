# This is a PRIVATE file to check if any of the hash from my previous files I have handed during the subject,
# are in a specific list of hashes.

# list with all my hashes
hashes = [
    "eca97dacb967deada67f2607f78f8dc5f06be792d4ef09f830ed159d73d68845",
    "80017b94931e576a4da912de45cd3283484f38c31884df97bd02833e1b540346",
    "f72faf0ac116a963937795a2a38016e84bd563d0334e78221413acf50974052e",
    "ba19cdfe7803ff3f31cb40cf0c92a1b106b7ec07f4bd5646fe54c09444684e3d",
    "e52d104f946a4d6fd80d4299d6152db8a30ad4617758363b7cbde33512e61124",
    "aa2ff1049d67ed6e6de5e117d81e828c46224077b0ef4e530b2c2fccd578914b",
    "ba19cdfe7803ff3f31cb40cf0c92a1b106b7ec07f4bd5646fe54c09444684e3d",
    "b06734157f0c602676d8e5cf73a8dd01895ca9fcf38798f65b1368390889cd86",
    "a69dcb4d1b0b631293a555734e4c7d8f54a55fc659ad96fc6c2350c6e66102e9",
    "21812754c37f9d606a29120c8570f9d1f72a30316df0524857391f26a526163f",
    "8f7ad49f7133ad2eecf4433f006d22c2f54d8dff64d2ae301db5c1a45902aa1d",
    "28e9e09d8bc426aec9aa3d1146829234df6d5c059298798a8fa7700e67c2f75e",
    "d402a9b1eb8984a0c2d470ac95ead9e0248f776f403be9480b573ebb034fd1a3",
    "90487bd7c5d36607817362d1c18b22d382d7219eccd4eddc5992e3fa20606dc6",
    "3ec36461497afebaf8a1d9da7cc70bf138d93bee047123fd454685fbcdde8e5b",
    "9585ebf537dc260d4c8e228a0bce8bb1376cd993b7ea7c3c56ec71180741929d",
    "00025780a4f99638d423a99ef7716923e679374ad41a819f5bb0e2526ebc2e43"
]

list_hashes_file = "SGSSI-22.CB.02.txt"

for hash in hashes:
    if hash in open(list_hashes_file).read():
        print("Hash found: " + hash)

print("All hashes checked")

