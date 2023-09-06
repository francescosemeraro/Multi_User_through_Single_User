import zstandard
import pathlib
import os

tags = ['_a01_t01_r01','_a01_t01_r02','_a01_t01_r03','_a01_t01_r04','_a01_t01_r05','_a01_t01_r06',
        '_a01_t02_r01','_a01_t02_r02','_a01_t02_r03','_a01_t02_r04','_a01_t02_r05','_a01_t02_r06',
        '_a01_t03_r01','_a01_t03_r02','_a01_t03_r03','_a01_t03_r04','_a01_t03_r05','_a01_t03_r06',
        '_a01_t04_r01','_a01_t04_r02','_a01_t04_r03','_a01_t04_r04','_a01_t04_r05','_a01_t04_r06',
        '_a01_t05_r01','_a01_t05_r02','_a01_t05_r03','_a01_t05_r04','_a01_t05_r05','_a01_t05_r06',
        '_a02_t01_r01','_a02_t01_r02','_a02_t01_r03','_a02_t01_r04','_a02_t01_r05','_a02_t01_r06',
        '_a02_t02_r01','_a02_t02_r02','_a02_t02_r03','_a02_t02_r04','_a02_t02_r05','_a02_t02_r06',
        '_a02_t03_r01','_a02_t03_r02','_a02_t03_r03','_a02_t03_r04','_a02_t03_r05','_a02_t03_r06',
        '_a02_t04_r01','_a02_t04_r02','_a02_t04_r03','_a02_t04_r04','_a02_t04_r05','_a02_t04_r06',
        '_a02_t05_r01','_a02_t05_r02','_a02_t05_r03','_a02_t05_r04','_a02_t05_r05','_a02_t05_r06',
        '_a03_t01_r01','_a03_t01_r02','_a03_t01_r03','_a03_t01_r04','_a03_t01_r05','_a03_t01_r06',
        '_a03_t02_r01','_a03_t02_r02','_a03_t02_r03','_a03_t02_r04','_a03_t02_r05','_a03_t02_r06',
        '_a03_t03_r01','_a03_t03_r02','_a03_t03_r03','_a03_t03_r04','_a03_t03_r05','_a03_t03_r06',
        '_a03_t04_r01','_a03_t04_r02','_a03_t04_r03','_a03_t04_r04','_a03_t04_r05','_a03_t04_r06',
        '_a03_t05_r01','_a03_t05_r02','_a03_t05_r03','_a03_t05_r04','_a03_t05_r05','_a03_t05_r06']

#subjects = ['01','02','03','04','05','06','07','08','09','10','11']
subjects = ['02','05']

for i in subjects:
    for j in tags:
        
        try:
            input_file = "s"+i+j+"_skeleton/"+"s"+i+j+'_skeleton_0.db3.zst'
            os.rename("s"+i+j+"_skeleton/"+"s"+i+j+'_skeleton_0.db3.zstd',input_file)
            with open(input_file, 'rb') as compressed:
                decomp = zstandard.ZstdDecompressor()
                output_path = "s"+i+j+'_skeleton_0.db3'
                with open(output_path, 'wb') as destination:
                    decomp.copy_stream(compressed, destination)
                print(input_file + " decompressed")
        except:
            print(input_file," missing")